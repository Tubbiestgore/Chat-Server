import socket

from threading import Thread
from colorama import Fore, Style

# Server Configuration
S_HOST = "0.0.0.0" # Configure IP - Any Available Network Interface
S_PORT = 6622      # Configure Port - Just random number
separator_token = "<SEP>" # Used to sepearate client name and messages

# Client Configuration
client_sockets = {} # Empty Dictionary to Store Client Data
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.MAGENTA, Fore.RED, Fore.YELLOW]  # Available colors for clients - Can Add to List

# This function is designed to listen for client messages. 
# It takes that from the 'CS' socket, and then when a message is recieved, broadcasts it to all the other clients.
def listen_for_client(cs, address):
    client_color = client_sockets[cs]
    
    while True: # Loop to handle client messages and communication
        try:
            message = cs.recv(1024).decode() # Receives data from 'CS' socet and decodes it
        
        # Method to catch exceptions/Errors    
        except Exception as exception:
            print(f"[!] Error: {exception}")
            del client_sockets[cs]
            break
        
        else:
            if not message:
                del client_sockets[cs]
                break
            
            # Method to print the message with correct color and address, replaces separator_token with a ':'
            message = message.replace(separator_token, ": ")
            print(client_color + f"{address} - {message}" + Style.RESET_ALL)
            
            # Sends message to all connected clients except for the sender (cs)
            for client_socket in client_sockets:
                if client_socket != cs:
                    client_socket.send((client_color + f"{address} - {message}" + Style.RESET_ALL).encode()) 

# Server Setup
skt = socket.socket() # Creates a Socket for the Server
skt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Allows for the Reuse of the server address/port
skt.bind((S_HOST, S_PORT)) # Binds the socekt to the specified server address/port
skt.listen(5) # Starts Listening with a max queue of 5 pending connections
print(f"[*] Listening as {S_HOST}:{S_PORT}") # Prints listening message

# Handling Connections
while True: # Loop to accept incoming client connections
    
    # Accepts and recieves client socket and address - prints to server.py
    client_socket, client_address = skt.accept()
    print(f"[+] {client_address} connected.")

    # Assign a color to the client
    client_color = colors[len(client_sockets) % len(colors)]
    client_sockets[client_socket] = client_color

    # Creates a new thread to hanlde communication with client 
    thread = Thread(target=listen_for_client, args=(client_socket, client_address))
    thread.daemon = True
    thread.start() # Start the Thread

