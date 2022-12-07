import socket
import threading

HOST = socket.gethostbyname('localhost')
PORT = 9090
clients = []


def appServer():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f'Server listening on: {HOST},{PORT}')

    except socket.error as e:
        print(f'Erro ao abrir server: {e}')

    server.bind((HOST, PORT))

    server.listen(10)

    # Escutando client
    while True:
        client, addr = server.accept()
        clients.append(client)
        print(client, addr)
        
        #Necessária pois precisamos receber outros clients
        th_broadcast = threading.Thread(target=tratandoMsg, args=[client])
        th_broadcast.start()


def tratandoMsg(client):
    while True:
        try:
            msg = client.recv(2048)
            broadcast(msg, client)
        except:
            removeClient(client)
            break


def broadcast(msg, client):
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(msg)
            except:
                print("Error sending message")
                removeClient()


def removeClient(client):
    clients.remove(client)


appServer()
