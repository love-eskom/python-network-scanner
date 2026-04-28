import os
import json 
import threading
import socket

class PortScanner: 
    def __init__(self, target): 
        self.target = target 
        self.open_ports = []
        self.lock = threading.Lock() 
        self.SERVICE_MAP = {
            20: "FTP Data",
            21: "FTP",
            22: "SSH",
            23: "Telnet",
            25: "SMTP",
            53: "DNS",
            67: "DHCP Server",
            68: "DHCP Client",
            69: "TFTP",
            80: "HTTP",
            110: "POP3",
            123: "NTP",
            143: "IMAP",
            161: "SNMP",
            389: "LDAP",
            443: "HTTPS",
            445: "SMB",
            3306: "MySQL",
            3389: "RDP",
            5432: "PostgreSQL",
            8080: "HTTP-Alt"
        }
        
    def scan_port(self, port): 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.settimeout(.4) 

        result = s.connect_ex((self.target, port)) 

        s.close()
        
        if result == 0: 
            return True 
        else: 
            return False 
        
    def threaded_scan(self, port):
        if self.scan_port(port):
            with self.lock:
                self.open_ports.append(port)
        
    def scan_range(self, start_port, end_port):
        self.open_ports = []
        threads = []
        
        for port in range(start_port, end_port + 1):
            thread = threading.Thread(target=self.threaded_scan, args=(port,))
            threads.append(thread)
            thread.start()
            
        for thread in threads:
            thread.join()

        return sorted(self.open_ports)

    def banner_grab(self, port):
        try:
            s = socket.socket()
            s.settimeout(1)
            s.connect((self.target, port))
            banner = s.recv(1024).decode().strip()
            s.close()
            return banner
        except:
            return "Unknown"
        
    def get_service_name(self, port):
        return self.SERVICE_MAP.get(port, "Unknown service")
    
    def export_json(self, filename="results/scan_results.json"):
        os.makedirs("results", exist_ok=True)
        results = []
        
        for port in self.open_ports:
            results.append({
                "port": port,
                "service": self.get_service_name(port),
                "banner": self.banner_grab(port)
            })
            
        with open(filename, "w") as f:
            json.dump(results, f, indent=4)
        return filename