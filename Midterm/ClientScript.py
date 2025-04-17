#Import required libraries
import socket

#Define the target host and port (Host and port of the server)
host = "127.0.0.1"  # Localhost IP address
port = 6000  # Port number to connect to

#Create a socket that will use IPv4 addressing and TCP protocol to match the server socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to the server
s.connect((host, port))

#Send data to the server
s.sendall(b"Hello from the client!") #b signifies data will be sent in 8 bit bytes
#Receive a response from the server
data = s.recv(1024)  # Buffer size of 1024 bytes
print(f"Received from server: {data.decode()}")

#close the connection and the client socket
s.close()
print("Connection closed.")
