__author__ = 'Rich Johnson'

import socket
import sys
import os
import re

SHUTDOWN_FLAG = False
server_address = "./recipe_grabber_socket"

# Make sure the socket does not already exist
try:
	os.unlink(server_address)
except OSError:
	if os.path.exists(server_address):
		raise

# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
print >>sys.stderr, 'starting up on %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while not SHUTDOWN_FLAG:
	print >>sys.stderr, 'waiting for a connection'
	connection, client_address = sock.accept()

	try:
		print >>sys.stderr, 'connection from', client_address

		while True:
			data = connection.recv(128)
			print >>sys.stderr, 'received "%s"' % data
			if data:
				if re.search('^KILL-9.*', data):
					SHUTDOWN_FLAG = True
					print >> sys.stderr, 'received shutdown flag'
					connection.sendall("Goodbye")
					break
				else: 
					print >>sys.stderr, 'sending data back to the client'
					connection.sendall(data)
			else:
				print >>sys.stderr, 'no more data from', client_address
				break
	finally:
		connection.close()