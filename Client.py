import socket
 
servidor = "127.0.0.1"
puerto = 39421
 
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((servidor, puerto))
while True:
	# solicitamos la lista de archivos del home del usuario
	cliente.send("dir");
	#respuesta = cliente.recv(4096)
	#respuesta = cliente.recv(4096)
	#print respuesta
