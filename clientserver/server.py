import socket as s

HOST = '127.0.0.1'
PORT = 50001

with s.socket(s.AF_INET, s.SOCK_STREAM) as server:

    #disponibilidade & abertura de rede

    server.bind((HOST, PORT))

    server.listen() #garantir a disponibilidade de entrada de cliente

    print("O Servidor esta online e aguardando")

    connection, address = server.accept()

    print(f"Conectado por: {address}")

    data = connection.recv(1024).decode('utf-8')

    connection.send(data.encode())


    

