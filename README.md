# tcpweb

<p align="center">
  <img src="https://github.com/1yc4n0rn0t/tcpweb/blob/main/image.png" alt="Image" style="height: 350px; vertical-align: middle; margin-left: 10px;" />
</p>


## dump your tcp traffic live in a browser, then download pcap for analyzing

[![Python](https://img.shields.io/badge/python-3670A0?style=Social&logo=python&logoColor=ffdd54)](https://img.shields.io/badge/python-3670A0?style=Social&logo=python&logoColor=ffdd54)
[![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=Social&logo=html5&logoColor=white)](https://img.shields.io/badge/html5-%23E34F26.svg?style=Social&logo=html5&logoColor=white)

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

```
   sudo apt install python3-pip 
   sudo apt install python3-virtualenv 
   python3 -m venv venv 
   pip install -r requirements.txt 
   python3 app.py or sudo python3 app.py  
```
##### Most likely, you will need to configure the python file to update the network interface to your interface <line 14> - interface name i.e. eth0

```
# Set your network interface here
interface_name = 'enx54b20312dd9c'  # Change this to your interface name (e.g., eth0, enx54b20312dd9c)

```

#### You can also cURL images into the captured_images directory and they will display live on the main web interface, but can be viewed from the subdomain /images/<image.type>

Follow the steps below to set up the project in a virtual environment.

### Step 1: Clone the Repository

### Step 2 Follow installation method

### Step 3 Run the file 

##### Note - You made need to enter your system password when you run the file, depending on your tcpdump permissions

```
├── app.py                # Main Flask web application
├── templates/
    ├── index.html              
├── requirements.txt       # List of Python dependencies
└── README.md              # Project documentation```
