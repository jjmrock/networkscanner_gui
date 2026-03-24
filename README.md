Here’s a clean and professional **README.md** for your project 👇

---

# Smart / Pro Port Scanner

## Overview

The Smart Port Scanner is a Python-based GUI application designed to scan a target system (IP address or domain) and identify open ports along with their associated services. It helps users understand network exposure and detect potential security risks.

---

## Features

* Graphical User Interface using CustomTkinter
* Quick Scan (common ports) and Full Scan (1–65535 ports)
* Multithreaded scanning for faster performance
* Displays results in a structured table (Port, Service, Risk)
* Real-time progress bar
* Stop scan functionality
* Export scan results to CSV
* Basic risk detection (e.g., Telnet flagged as insecure)

---

## Technologies Used

* Python
* CustomTkinter (GUI)
* Socket Programming (network scanning)
* Threading and Queue (performance optimization)
* CSV module (data export)

---

## Installation

1. Clone or download the project
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the application:

```
python main.py
```

---

## How It Works

1. Enter a target (IP address or domain name)
2. Select scan type (Quick or Full)
3. Click "Scan" to start scanning
4. View results in the table
5. Export results if needed

---

## Example

If you scan a system:

| Port | Service | Risk     |
| ---- | ------- | -------- |
| 23   | Telnet  | Insecure |
| 80   | HTTP    | OK       |

---

## Use Cases

* Learning cybersecurity concepts
* Basic network reconnaissance
* Checking open ports on a system
* Educational demonstrations

---

## Limitations

* Only supports TCP connect scan
* Basic service detection
* No advanced vulnerability scanning

---

## Future Improvements

* Banner grabbing (service version detection)
* OS detection
* Advanced scan types (SYN scan)
* Graph visualization of results
* Integration with security tools

---

## Disclaimer

This tool is intended for educational purposes only. Use it only on systems you own or have permission to test.

---

## Author

Developed as a cybersecurity learning project.
