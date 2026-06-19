# Port Scanner

A multithreaded port scanner built in Python that scans a target host for open ports and tells you what service is running on each one.

Built this as part of my cybersecurity learning journey — Day 1 project.

*********************************

## What it does

- Scans ports on any host (default: localhost)
- Detects common services (HTTP, SSH, FTP, RDP, SMB, etc.)
- Uses threading so it's fast (1024 ports in ~5 seconds)
- Saves results to a scan_report.txt file
- Accepts custom host and port range from the command line
  
 ********************

## How to run it

Basic scan:
python scanner.py

Custom target and range:
python scanner.py --host 127.0.0.1 --start 1 --end 1024

---

## Example output
****************************************
Port Scanner

Target : 127.0.0.1

Ports  : 1 - 1024

Time   : 2024-01-01 12:00:00
[OPEN] Port 135 --> Windows RPC

[OPEN] Port 445 --> SMB
*****************************************

2 open port(s) found.
Report saved to scan_report.txt

*******

## Requirements

Python 3.x — no external libraries needed, everything used is built into Python.

*******

## Disclaimer

Only scan hosts you own or have explicit permission to scan.
