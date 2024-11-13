import socket
import threading

def client_listener(client_socket, client_address):
    print(f"Nueva conexion: {client_address}")
    
    while True:
        
        message = client_socket.recv(1024).decode() # recibimos mensaje del cliente
        
        if not message: #si no hay mensaje seguimos esperando
            break
        
        print(f"Mensaje recibido del cliente {client_address}: {message}")
        
        if message == "DESCONEXION":
            print(f"Cliente {client_address} desconectado.") #mostramos cuando se desconectara un cliente
            client_socket.close()
            break
        else:
            response = message.upper() #convertimos mensaje a mayuscula
            client_socket.send(response.encode()) #enviamos mensaje
            

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000)) #indicamos el puerto y la ip 
    server_socket.listen()
    print("servidor corriendo en el puerto 500")

    while True:
        client_socket, client_address = server_socket.accept() #recibe peticiones para conexion de nuevos clientes
        
        client_thread = threading.Thread(target=client_listener, args=(client_socket, client_address)) #se crea un hilo con su conexion para cada cliente, asi podemos interactuar con varios
        client_thread.start()


if __name__ == "__main__":
    start_server()
