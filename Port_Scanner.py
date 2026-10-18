import socket
from datetime import datetime

# Let's write down the target's IP address, i will use local host.
target_host = "127.0.0.1"

#Range of ports, which we are going to scan. for example 1 to 100
start_port = 8000
end_port = 9000

print(f"Scanning is starting on target {target_host}")
print(f"time: {datetime.now()}")

try:
    for port in range(start_port, end_port + 1):
        #Creating a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #add timeout so it can not stop on one port
        s.settimeout(0.2)

        #trying to connect
        result = s.connect_ex((target_host, port))

        # if result is 0 it means port is open
        if result == 0:
            print(f"Port {port}: Its OPEN")

        s.close()

except KeyboardInterrupt:
    print("\n Scanning is stopped by the user")
except socket.gaierror:
    print("\n Host not found")
except socket.error:
    print("\n Could not connect to the server")

print("Scanning is finished")