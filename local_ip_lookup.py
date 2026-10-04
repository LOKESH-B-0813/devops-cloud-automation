# local_ip_lookup.py - Extracts host machine IPv4 address
import socket
print(f"Local Host IP: {socket.gethostbyname(socket.gethostname())}")
