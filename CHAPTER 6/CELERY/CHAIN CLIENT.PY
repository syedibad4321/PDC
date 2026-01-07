import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8000)) # Middle node se connect

client.send(b"Hello from Chain Start!")
print("[Client] Message Sent.")
client.close()