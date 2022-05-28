# Import socket module
from socket import *
serverAddress = ""
# serverPort= 2603

def webServer(serverPort=6789):
#Prepare a sever socket
#Fill in start 
# 10.16.154.196 NYU Bobsts
# 192.168.1.109 Home 
# http://10.16.154.196:2603/HelloWorld.html 
# http://192.168.1.109:2603/HelloWorld.html
		serverSocket = socket(AF_INET, SOCK_STREAM)
		serverSocket.bind((serverAddress, serverPort))
		serverSocket.listen(1)
		print ('the web server is up on port:', serverPort)
		#Fill in end

		while True:
			#Establish the connection

			print ('Ready to serve...')
			
			# Set up a new connection from the client
			#Fill in start 
			connectionSocket, addr =serverSocket.accept()   
			#Fill in end

			try:
				#Fill in start 
				message =connectionSocket.recv(1024)  
				#Fill in end

				filename = message.split()[1]
				
				f = open(filename[1:])
				#Fill in start
				outputdata =f.read()  
				#Fill in end
				print (outputdata)
				#Send one HTTP header line into socket
				#Fill in start#
				connectionSocket.send('HTTP/1.1 200 OK\n\n'.encode())
				# connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")
				# connectionSocket.send(bytes("Hello from the server!", "utf-8"))
				#Fill in end

				# Send the content of the requested file to the connection socket
				for i in range(0, len(outputdata)):
					connectionSocket.send(outputdata[i].encode())
				# connectionSocket.send("\r\n".encode())
				connectionSocket.close()

			except IOError:
				# Send HTTP response message for file not found
				#Fill in start
				connectionSocket.send("HTTP/1.1 404 Not Found\n\n".encode())
				#Fill in end
				# Close the client connection socket
				#Fill in start
				connectionSocket.close()
				#Fill in end
		serverSocket.close()

if __name__ == "__main__":
  webServer(6789)
