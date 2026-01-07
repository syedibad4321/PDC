import socket

# 1. Socket banana
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. IP aur Port Bind karna
host = 'localhost'
port = 12345
server_socket.bind((host, port))

# 3. Listen karna (Wait mode)
server_socket.listen(1)
print(f"Server is listening on port {port}...")

# 4. Connection Accept karna
conn, address = server_socket.accept()
print(f"Connection from: {address}")

# 5. Data Receive karna
data = conn.recv(1024).decode()
print(f"Message received: {data}")

# 6. Jawab wapis bhejna (Acknowledgement)
conn.send("Message Received Beta!".encode())

# 7. Close
conn.close()