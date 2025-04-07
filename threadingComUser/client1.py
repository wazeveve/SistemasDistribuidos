import socket as s

def client():
    HOST = '127.0.0.1'
    PORT = 50000
    

    clientConn = s.socket(s.AF_INET, s.SOCK_STREAM)

    clientConn.connect((HOST,PORT))

    try:
        user = input("Digite seu usuario: ")
        clientConn.send(user.encode('utf-8'))
        while True:
            mens = input("Digite sua mensagem: (Digite q para sair)")
            if mens == 'q':
                break
           
            clientConn.send(mens.encode('utf-8'))
    finally:
        clientConn.close()
        print(f"Conexão encerrada")

client()