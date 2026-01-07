import socket

# Port 9000 par listen karega
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 9000))
s.listen(1)

print("[Final Server] Waiting...")
conn, addr = s.accept()

data = conn.recv(1024).decode()
print(f"Final Server received: {data}")

conn.close()