# Import socket module
import socket                   

# Create a socket object
s = socket.socket()          
# Get local IP address 
host = socket.gethostname() 
# Reserve a port for your service.    
port = 2603                  

s.connect((host, port))
s.send("Hello server!".encode())

with open('received_file', 'wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')

