#Import required libraries/modules
import sys
import socket

#target_host = 127.0.0.1  # Localhost IP address
#port_range = 1-1024  # Port range to scan

#Prompt the user for the target host and port range
target_host = input("Enter the target host (IP address or hostname): ")
port_range = input("Enter the port range (e.g., 1-65535): ").split('-')
# Convert the port range to integers
port_range = [int(port_range[0]), int(port_range[1])]
# Check if the port range is valid and if not, exit the program
if port_range[0] < 1 or port_range[1] > 65535 or port_range[0] > port_range[1]:
    print("Invalid port range. Please enter a valid range (1-65535).")
    sys.exit() 

# Define the port_scanner function
def port_scanner(target_host, port_range):
    
    try:
        # Loop through the specified port range
        for port in range(port_range[0], port_range[1] + 1):
            # Create a socket object using IPv4 and TCP protocol
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set a timeout for the socket connection to keep it from hanging indefinitely
            s.settimeout(5)  # 5 second timeout
            # Attempt to connect to the target host and port
            result = s.connect_ex((target_host, port))
            # Check if the connection was successful (result == 0 means success)
            if result == 0:
                print(f"Port {port} is open")
            else:
                print(f"Port {port} is closed")
            # Close the socket connection
            s.close()
    # Handle problems that may occur during the socket connection, close the socket and exit the program
    except socket.error as err:
        print(f"Socket error: {err}")
        exit()
    # Handle any other exceptions that may occur, close the socket and exit the program
    except Exception as error:
        print(f"An unexpected error occurred: {error}")
        exit()
    finally:
        # Close the socket connection if it is still open
            s.close()

#Run the port_scanner function
port_scanner(target_host, port_range)