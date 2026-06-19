import socket
import threading
import argparse
import datetime

SERVICES = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 135: "Windows RPC",
    143: "IMAP", 443: "HTTPS", 445: "SMB", 3306: "MySQL",
    3389: "RDP", 8080: "HTTP-Alt"
}

open_ports = []
lock = threading.Lock()

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            service = SERVICES.get(port, "Unknown")
            with lock:
                open_ports.append((port, service))
                print(f"  [OPEN] Port {port} --> {service}")
    except:
        pass

def main():
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("--host", default="127.0.0.1", help="Host to scan")
    parser.add_argument("--start", type=int, default=1, help="Start port")
    parser.add_argument("--end", type=int, default=1024, help="End port")
    args = parser.parse_args()

    print(f"\n{'='*40}")
    print(f"  Port Scanner")
    print(f"  Target : {args.host}")
    print(f"  Ports  : {args.start} - {args.end}")
    print(f"  Time   : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*40}\n")

    threads = []
    for port in range(args.start, args.end + 1):
        t = threading.Thread(target=scan_port, args=(args.host, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"\n{'='*40}")
    print(f"  {len(open_ports)} open port(s) found.")
    print(f"{'='*40}\n")

    # Save report
    with open("scan_report.txt", "w") as f:
        f.write(f"Scan Report - {args.host}\n")
        f.write(f"Time: {datetime.datetime.now()}\n\n")
        for port, service in sorted(open_ports):
            f.write(f"[OPEN] Port {port} --> {service}\n")
    print("  Report saved to scan_report.txt\n")

main()