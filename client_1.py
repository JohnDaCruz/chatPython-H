import socket
import threading

HOST = socket.gethostbyname('localhost')  # !!
PORT = 9090



def appClient():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
        print('Conectado ao server com sucesso!')
    except socket.error as e:
        print(f'Erro ao se conectar: {e}')

    username = input('\nUsuário: ')
    print(f'{username} conectado!')

    def enviarMsg(client, username):
        while True:
            try:
                msg = input('\n')
                client.send(f'{username}: {msg}'.encode('utf-8'))
            except:
                print('Erro ao enviar mensagem!!')
                return

    def recvMsg(client): #!!
        while True:
            try:
                msg = client.recv(2048).decode('utf-8')
                print(msg + '\n')
            except:
                print('Erro!')
                client.close()
                break
            
    th_two = threading.Thread(target=recvMsg, args=[client])
    th_one = threading.Thread(target=enviarMsg, args=[client, username])
    th_two.start()
    th_one.start()


appClient()
