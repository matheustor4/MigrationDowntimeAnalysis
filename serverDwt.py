import socket
import time
import datetime

UDP_IP = "0.0.0.0"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Server listen {UDP_IP}:{UDP_PORT}")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"Message from {addr}")
    now = datetime.datetime.now()
    time_str = now.strftime("%H:%M:%S.%f")
    sock.sendto(str(time_str).encode(), addr)  # 
