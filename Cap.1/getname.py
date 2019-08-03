import socket
hostname = 'www.python.org'
addr = socket.gethostbyname(hostname)
print ("IP address of {} is {}".format(hostname, addr))