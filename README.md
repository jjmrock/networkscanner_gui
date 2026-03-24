Overview

The Smart Port Scanner is a Python-based GUI application designed to scan a target system (IP address or domain) and identify open ports along with their associated services. It helps users understand network exposure and detect potential security risks.

Features
Graphical User Interface using CustomTkinter
Quick Scan (common ports) and Full Scan (1–65535 ports)
Multithreaded scanning for faster performance
Displays results in a structured table (Port, Service, Risk)
Real-time progress bar
Stop scan functionality
Export scan results to CSV
Basic risk detection (e.g., Telnet flagged as insecure)
Technologies Used
Python
CustomTkinter (GUI)
Socket Programming (network scanning)
Threading and Queue (performance optimization)
CSV module (data export)
Installation
Clone or download the project
Install dependencies:
pip install -r requirements.txt
Run the application:
python main.py
How It Works
Enter a target (IP address or domain name)
Select scan type (Quick or Full)
Click "Scan" to start scanning
View results in the table
Export results if needed
