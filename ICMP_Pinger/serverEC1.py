import random
from socket import *
# Creates a UDP socket
serverSock = socket(AF_INET, SOCK_DGRAM)
# Assigns IP address and port number to the socket
serverSock.bind(('', 11046))

while True:
  # Generates random number from 0 to 9
  rand=random.randint(0, 10)
  # Receives the client packet from the address coming in
  message,address = serverSock.recvfrom(1024)
  # Capitalizes the message from the client
  message = message.upper()
  # If generated random number is less is than 4, we consider the packet lost
  if rand < 4:
    continue  
  # If not, the server responds to the client
  serverSock.sendto(message, address)