import time 
import argparse 
from scanner import PortScanner 

parser = argparse.ArgumentParser(description="Python Network Port Scanner") 
parser.add_argument("--target", required=True, help="Target IP address") 
parser.add_argument("--start", type=int, required=True, help="Start port") 
parser.add_argument("--end", type=int, required=True, help="End port") 

args = parser.parse_args() 
scanner = PortScanner(args.target) 

start_time = time.time()
open_ports = scanner.scan_range(args.start, args.end)
end_time = time.time()
scan_duration = round(end_time - start_time, 2)

port_count = len(open_ports) 
scanner.export_json() 

if port_count == 0: 
    print("All ports are closed") 
    print("Results exported to results/scan_results.json") 

for port in open_ports: 
        service = scanner.get_service_name(port) 
        banner = scanner.banner_grab(port) 
        print(f"Port {port} OPEN | Service: {service} | Banner: {banner}")
        




print(f"\nScan completed in {scan_duration} seconds")
print(f"Open ports found: {len(open_ports)}")