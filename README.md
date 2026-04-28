# Python Network Scanner

A multithreaded Python-based network port scanner built for cybersecurity learning and portfolio demonstration.

## Features

- Multithreaded TCP port scanning
- Scan custom port ranges
- Banner grabbing / service fingerprinting
- Common service detection via port mapping
- Export scan results to JSON
- CLI argument support using argparse
- Scan performance timing metrics

## Example Usage

```bash
python main.py --target 127.0.0.1 --start 20 --end 100