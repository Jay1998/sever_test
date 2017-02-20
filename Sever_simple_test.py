#!usr/bin/python 
 
import socket 
 
host='' 
port=51423 
 
s=socket.socket (socket.AF_INET ,socket.SOCK_STREAM) 
s.setsockopt(socket.SOL_SOCKET ,socket.SO_REUSEADDR ,1) 
s.bind((host,port)) 
s.listen(1) 
 
print("Server is running on port %d ;Press Ctrl-c to terminate." % port )
 
while 1: 
    clientsock,clientaddr=s.accept() 
    clientfile=clientsock.makefile('rw',0) 
    clientfile.write("welcome ,"+str(clientaddr)+"\n" ) 
    clientfile.write("Please enter a string:") 
    clientfile.write("\n") 
    line=clientfile.readline().strip() 
    clientfile.write("You entered string is:%s .\n"%line) 
    clientfile.close() 
    clientsock.close() 