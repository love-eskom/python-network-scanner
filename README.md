# Python Network Scanner
LAB-002

PYTHON NETWORK SCANNER

BUILD • DETECT • DEFEND
---
A multithreaded Python-based network port scanner built for cybersecurity learning and portfolio demonstration.

## Features

- Multithreaded TCP port scanning
- Scan custom port ranges
- Banner grabbing / service fingerprinting
- Common service detection via port mapping
- Export scan results to JSON
- CLI argument support using argparse
- Scan performance timing metrics

## Technologies Used
- Python 3
- Socket Programming
- Threading
- JSON
- Argparse

## Disclaimer
This tool is intended for educational and authorized security testing only.
Do not scan systems you do not own or have permission to test.

## Example Usage

python main.py --target 127.0.0.1 --start 20 --end 100
