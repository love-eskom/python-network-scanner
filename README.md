# Python Network Scanner

<div align="center">

**LAB-002 · NETWORKING & SOFTWARE ENGINEERING**

> **BUILD. DETECT. DEFEND.**

A multithreaded TCP port scanner developed in Python to explore network connectivity, port discovery, service identification and network reconnaissance through practical socket programming.

</div>

---

## Overview

This project is a command-line network scanning tool that probes a target host across a specified range of TCP ports and identifies accessible services.

Built as a practical networking and cybersecurity project, it applies Python socket programming, concurrency and network service identification to automate port-scanning tasks.

The project demonstrates how networking concepts can be translated into a functional software tool.

## Features

- **TCP Port Scanning** — Identify accessible TCP ports on a specified target.
- **Multithreading** — Concurrent scanning to improve scanning efficiency.
- **Custom Port Ranges** — Specify the starting and ending ports to scan.
- **Banner Grabbing** — Attempt to retrieve service banners for identification.
- **Service Identification** — Map commonly associated port numbers to services.
- **JSON Export** — Save scan results in a structured format.
- **Command-Line Interface** — Configure scans using `argparse`.
- **Performance Metrics** — Measure and report scan execution time.

## Technologies

| Technology         | Application                    |
| ------------------ | ------------------------------ |
| Python 3           | Core implementation            |
| Socket Programming | TCP connection testing         |
| Threading          | Concurrent port scanning       |
| JSON               | Structured result export       |
| Argparse           | Command-line argument handling |

## How It Works

The scanner follows a straightforward workflow:

1. Accept a target host and port range through command-line arguments.
2. Initiate TCP connection attempts against the specified ports.
3. Execute scan operations concurrently using threads.
4. Identify accessible ports and associated services.
5. Attempt banner grabbing where supported.
6. Compile scan results and execution metrics.
7. Export results to JSON when configured.

## Usage

### Scan a target across a custom port range

```bash
python main.py --target 127.0.0.1 --start 20 --end 100
```

### Arguments

| Argument   | Description                   |
| ---------- | ----------------------------- |
| `--target` | Target IP address or hostname |
| `--start`  | Starting port number          |
| `--end`    | Ending port number            |

## Engineering Concepts

This project explores the intersection of software development and networking through:

- TCP connection establishment and port states.
- Client-server communication using Python sockets.
- Concurrency and multithreaded execution.
- Network service identification.
- Command-line application design.
- Structured data serialization.
- Execution-time measurement and performance considerations.

## Learning Outcomes

Developing this tool strengthened my understanding of how TCP connectivity can be programmatically tested and how network scanning utilities operate.

It also provided practical experience with Python concurrency, socket programming, command-line interfaces and building reusable tools for network investigation.

## Disclaimer

This tool is intended for educational purposes and authorized security testing only.

Only scan systems you own or have explicit permission to assess. Unauthorized scanning may violate organizational policies or applicable laws.

---

**BUILD. DETECT. DEFEND.**

_Software · Networks · Security_
