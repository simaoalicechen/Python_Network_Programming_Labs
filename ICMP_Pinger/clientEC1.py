import socket
from socket import AF_INET, SOCK_DGRAM
import time
#servers set as localhost
serverName = '127.0.0.1' 
#creates the socket
#Also sets the timeout at 1 sec
clientSock = socket.socket(AF_INET,SOCK_DGRAM) 
clientSock.settimeout(1) 
# new varaible to keep thr sequence number 
sequenceNumber = 1 
# Stores the rtt results
rtt=[] 

while sequenceNumber<=10:
  #records the current time
  start=time.time() 
  #getting client messages 
  message = ('PING %d %d' % (sequenceNumber, start)) 
  #The client sends a message to the server
  clientSock.sendto(message.encode(),(serverName, 11046))
  try:
    #the Client recieves message from server
    message, address = clientSock.recvfrom(1024)
    # calculates the rtt
    elapsed = (time.time()-start) 
    rtt.append(elapsed)
    print(message)
    print('Round Trip Time ==' + str(elapsed) + ' seconds')
  # if reply exceeds one second 
  except socket.timeout: 
    print(message)
    print('Request timeout')

  sequenceNumber+=1 

# we want to close the socket after 10 packets
# Results
if sequenceNumber > 10: 
  mean=sum(rtt, 0.0)/ len(rtt)
  print('')
  print('Maximum RTT is:' + str(max(rtt)) + ' seconds')
  print('Minimum RTT is:' + str(min(rtt)) + ' seconds')
  print('Average RTT is:' + str(mean)+ ' seconds')
  print('Packet loss rate is:' + str((10-len(rtt))*10)+ ' percent')
clientSock.close()

