import socket
import threading

 
def administrar_clientes(socket_cliente):
    peticion = socket_cliente.recv(1024)
    print "[*] Mensaje recibido: %s" % peticion
    #respuesta = Popen(peticion, shell=True, stdout=PIPE).stdout.read()
    # confirmar al cliente, que el mensaje fue recibido
    #socket_cliente.send(respuesta)
    #socket_cliente.close()
 
ip = "0.0.0.0"
puerto = 39421
max_conexiones = 10
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

 
 
servidor.bind((ip, puerto))
servidor.listen(max_conexiones)
 
print "[*] Esperando conexiones en %s:%d" % (ip, puerto)
 
while True:
    cliente, direccion = servidor.accept()
    print "[*] Conexion establecida con %s:%d" % (direccion[0], direccion[1])
    administrador_de_clientes = threading.Thread(target=administrar_clientes, args=(cliente,))
    administrador_de_clientes.start()
