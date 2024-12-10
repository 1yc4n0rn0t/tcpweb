import subprocess
import time
import re
import os
import threading
from flask import Flask, Response, render_template, send_file, jsonify
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable cross-origin resource sharing

# Set your network interface here
interface_name = 'enx54b20312dd9c'  # Change this to your interface name (e.g., eth0, enx54b20312dd9c)

# Directory for storing captured images and pcap files
image_dir = 'captured_images'
os.makedirs(image_dir, exist_ok=True)

pcap_file = 'captured_traffic.pcap'  # File to store captured packets

# Global flag to control the capture process
capture_thread = None
capture_process = None

@app.route('/')
def index():
    return render_template('index.html', interface_name=interface_name)

def run_tcpdump():
    """
    Runs tcpdump on the specified interface and saves the packets to a .pcap file.
    """
    global capture_process
    command = ['sudo', 'tcpdump', '-i', interface_name, '-w', pcap_file, '-nn', '-v', '-l']
    print(f"Running tcpdump on interface {interface_name}...")

    capture_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Stream the output from tcpdump (for log purposes)
    while capture_process.poll() is None:
        time.sleep(1)

@app.route('/start_capture')
def start_capture():
    """Start capturing packets."""
    global capture_thread
    if capture_thread is None or not capture_thread.is_alive():
        capture_thread = threading.Thread(target=run_tcpdump)
        capture_thread.start()
        return jsonify({"status": "Capture started"}), 200
    return jsonify({"status": "Capture is already running"}), 400

@app.route('/stop_capture')
def stop_capture():
    """Stop capturing packets."""
    global capture_process
    if capture_process:
        capture_process.terminate()  # Terminate the tcpdump process
        capture_process = None
        return jsonify({"status": "Capture stopped"}), 200
    return jsonify({"status": "No capture process found"}), 400

@app.route('/download_pcap')
def download_pcap():
    """Download the captured packets as a .pcap file."""
    if os.path.exists(pcap_file):
        return send_file(pcap_file, as_attachment=True)
    return jsonify({"status": "PCAP file not found"}), 404

def run_tcpdump_live():
    """
    Runs tcpdump on the specified interface and yields the packets in real-time.
    """
    command = ['sudo', 'tcpdump', '-i', interface_name, '-nn', '-v', '-l']  # -l for line-buffered output
    print(f"Running tcpdump on interface {interface_name}...")

    # Start tcpdump as a subprocess
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Stream the output from tcpdump
    while True:
        output = process.stdout.readline()

        # If no more output and process ends, stop
        if output == b'' and process.poll() is not None:
            break

        if output:
            packet_data = output.decode('utf-8').strip()

            # Capture image URLs or raw image data from HTTP traffic (simple regex for PNG/JPEG)
            if "HTTP" in packet_data:
                image_url_match = re.search(r"(http[s]?://[^\s]+(\.(png|jpg|jpeg|gif|bmp|webp)))", packet_data)
                if image_url_match:
                    image_url = image_url_match.group(1)
                    save_image(image_url)

            # Send each line as an SSE event
            yield f"data: {packet_data}\n\n"

        # Add a small delay to prevent CPU overload
        time.sleep(0.1)

@app.route('/stream')
def stream():
    """The /stream endpoint that sends real-time packet data via Server-Sent Events (SSE)."""
    return Response(run_tcpdump_live(), content_type='text/event-stream;charset=utf-8', status=200)

def save_image(image_url):
    """Download and save image from the provided URL."""
    try:
        if image_url.startswith("http"):
            image_name = os.path.basename(image_url)

            if image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')):
                image_path = os.path.join(image_dir, image_name)

                img_data = requests.get(image_url).content
                with open(image_path, 'wb') as img_file:
                    img_file.write(img_data)

                print(f"Captured image: {image_name}")
    except Exception as e:
        print(f"Failed to capture image: {e}")

@app.route('/images')
def get_images():
    """Serve a list of all captured images."""
    image_files = os.listdir(image_dir)
    image_paths = [f"/images/{img}" for img in image_files if img.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'))]
    return jsonify(image_paths)

@app.route('/images/<image_name>')
def serve_image(image_name):
    """Serve an image file for viewing."""
    image_path = os.path.join(image_dir, image_name)
    if os.path.exists(image_path):
        return send_file(image_path)
    else:
        return "Image not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

