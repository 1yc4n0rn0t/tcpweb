# tcpweb
## dump your tcp traffic live in a browser, then download pcap for analyzing

# Network Packet Capture Web Interface

This project provides a web interface to capture and display network traffic using `tcpdump` and Flask. The captured packets can be displayed live in the browser, and the user can download the captured packets as a `.pcap` file for further analysis.

## Features
- Live packet capture displayed in a web interface.
- View network traffic (e.g., HTTP, TCP, UDP, etc.) in real-time.
- Save the captured packets to a `.pcap` file for later analysis in tools like Wireshark.
- The web interface has a "hacker-like" theme with modern UI design.

## Requirements

Before setting up this project, you need to have the following installed on your system:

- **Python 3.x** (Recommended: 3.9+)
- **tcpdump** (to capture network traffic)
- **Flask** (to run the web application)
- **flask-cors** (for cross-origin requests support)
  
### Installation

Follow the steps below to set up the project in a virtual environment.

### Step 1: Clone the Repository

```
├── app.py                # Main Flask web application
├── index.html            # HTML file for the web interface
├── static/                # Static files like CSS, JavaScript, and images
│   ├── css/              
│   └── js/
├── templates/             # HTML templates for Flask
├── requirements.txt       # List of Python dependencies
└── README.md              # Project documentation```
