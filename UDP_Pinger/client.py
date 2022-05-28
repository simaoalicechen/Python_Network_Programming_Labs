# import socket
from socket import *
import time
import sys
import datetime
def ping(host, port):
  resps = []
  sock = socket(AF_INET, SOCK_DGRAM)
  # sock.connect((host, port))
  sock.settimeout(1)
  try:
      for i in range(1, 11):
          start = time.time()
          message = 'Ping ' + str(i) + " " + time.ctime(start)
          try:
            sent = sock.sendto(message.encode(), (host, port))
            # print("Sent " + message)
            data, serverAddress = sock.recvfrom(1024)
            # print("Received: ", data.decode())
            # print("Server address: ", serverAddress)
            end = time.time()
            rtt = end - start
            # print("RTT: " + str(rtt) + " seconds\n")
            # resps.append((str(i), data.decode(), str(rtt)))
            resps.append((int(i), data.decode(), float(rtt)))
          except timeout:
            # print("#" + str(i) + " Requested has a Timeout\n")
            resps.append((int(i), 'Request timed out', 0.0))
  finally:
    print("closing socket")
    sock.close()
  return resps
if __name__ == '__main__':
  resps = ping('127.0.0.1', 12000)
  print(resps)




