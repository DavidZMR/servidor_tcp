import socket

def send_message(client_socket):
    while True:
        message = input("Ingrese un mensaje: ") #pedimos el mensaje
        client_socket.send(message.encode())#se envia el mensaje

        print(f"Cliente envía: {message}")

        if message == "DESCONEXION": #si se manda DESCONEXION se cierra la conexion del cliente
            print("Servidor cierra la conexión con el cliente.")
            client_socket.close()
            break

        response = client_socket.recv(1024).decode() #escucha la respuesta del server
        print(f"Servidor responde: {response}")

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5000)) #hace la conexion al servidor 
    print("conectando al server")

    send_message(client_socket)

if __name__ == "__main__":
    run_client()
