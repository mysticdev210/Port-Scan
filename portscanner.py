import socket
import pyfiglet
import datetime 
import sys 



ascil_banner = pyfiglet.figlet_format("PORT SCANNER :)")
print(ascil_banner)
target = input(str("Target IP:"))
print("_" * 50)
print("Scanning Target:" + target)
print("Scanning started at:"+ str(datetime))
print("_" * 50)

try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
except KeyboardInterrupt:
    print("\nExiting Program !!!!")
    sys.exit()
except socket.gaierror:
    print("\nHostname Could Not Be Resolved !!!!")
    sys.exit()
except socket.error:
    print("\nServer not responding !!!!")
    sys.exit()