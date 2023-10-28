import socket

from threading import Thread
from datetime import datetime
from colorama import Fore

# Server Configuration
S_HOST = "127.0.0.1" # Define IP Address - LocalHost
S_PORT = 6622
separator_token = "<SEP>"

# Socket Connection
skt = socket.socket()
print(f"[*] Connecting to {S_HOST}:{S_PORT}...")
skt.connect((S_HOST, S_PORT))
print("[+] Connected.")

username = input("Enter your name: ")

# Function to listen for server messages
def listen_for_messages():
    while True: # Loops to listen for messages from the server
        message = skt.recv(1024).decode()
        print(message)

# Creates a thread to run the function
thread = Thread(target=listen_for_messages)
thread.daemon = True
thread.start()

# Choose a color for your messages
available_colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.MAGENTA, Fore.RED, Fore.YELLOW]
client_color = available_colors[int(input("Choose a color (0-5): "))]

# Function to leave the Chat Room
def leave_chat():
    leave_message = "<<< Left Chat Room >>>"
    skt.send(f"{client_color}[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {username}{separator_token}{leave_message}{Fore.RESET}".encode())
    skt.close()
    print("\nYou have left the chat room.")
    
# Method to send messages
while True:
    to_send = input()
    if to_send.lower() == 'q':
        leave_chat()
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    to_send = f"{client_color}[{date_now}] {username}{separator_token}{to_send}{Fore.RESET}"
    skt.send(to_send.encode())

