import socket
import time
import datetime

# Adjust UDP_IP to the server IP
UDP_IP = "192.168.0.101"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Adjust timeout 
sock.settimeout(0.1)


while True:
    try:
     sock.sendto(b"hora_ms", (UDP_IP, UDP_PORT))
     data, addr = sock.recvfrom(1024)
     hora_servidor = data.decode() 
     print(f"Server time (ms): {hora_servidor}")
     # Salva a hora no arquivo de texto
     with open("server_time.txt", "a") as arquivo:
         arquivo.write(str(hora_servidor) + "\n")
     #print(f"escrita ok")
    except socket.timeout:
     print("Timeout: Server did not respond")
     with open("server_time.txt", "a") as arquivo:
         arquivo.write("timeout\n")
    except socket.error as e:
     print(f"Erro de socket: {e}")
     with open("server_time.txt", "a") as arquivo:
         arquivo.write(f"erro: {e}\n")
    time.sleep(0.1)
