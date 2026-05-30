import socket
from datetime import datetime

target = input("Enter target IP or website: ")
scan_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

print("\n" + "=" * 50)
print(f"Scanning target: {target}")
print(f"Scan Time: {scan_time}")
print(f"Port range: {start_port} - {end_port}")
print("=" * 50)

open_ports = []
results = []

for port in range(start_port, end_port + 1):

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(0.1)

    result = scanner.connect_ex((target, port))

    if result == 0:

        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown"

        output = f"[OPEN] Port {port} -> {service}"
        print(output)
        results.append(output)

        open_ports.append(port)

    scanner.close()

print("\n" + "=" * 50)
print("Scan Completed")
print(f"Total Open Ports Found: {len(open_ports)}")
print("=" * 50)

with open("scan_results.txt", "w") as file:
    file.write(f"Scan Time: {scan_time}\n")
    file.write(f"Target: {target}\n")
    file.write(f"Port Range: {start_port}-{end_port}\n\n")
    

    for item in results:
        file.write(item + "\n")

print("\nResults saved to scan_results.txt")