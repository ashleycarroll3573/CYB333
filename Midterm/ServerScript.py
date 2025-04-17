#Imorting necessary libraries
import socket

# Define the target host and port
Host = "127.0.0.1"  # Localhost IP address
Port = 6000  # Port number to connect to

# Create a socket that will use IPv4 addressing and TCP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the specified host and port
s.bind((Host, Port))
# Listen for incoming connection requests
s.listen() 
print(f"Server is listening on {Host}:{Port}")
# Accept connection from a client
connection, client_addr = s.accept()
print(f"Connection established with {client_addr}")