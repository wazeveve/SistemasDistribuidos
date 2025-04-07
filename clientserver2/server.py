import socket as s
import threading as th

def clientManager(conn, address):

    print(f"Conexão estabelecida - {address}")

    try:
        while True:
            mens = conn.recv(1024).decode('utf-8')
            if not mens:
                break
            print(f"Endereço: {address} - mensagem: {mens}")
    except:
        pass #escape de erro para thread
    finally:
        print(f"Desconectando: {address}")

def server():
        HOST = "10.13.8.15"
        PORT = 50000

        socketConn = s.socket(s.AF_INET, s.SOCK_STREAM)
        socketConn.bind((HOST, PORT))
        socketConn.listen()

        print(f"Servidor {HOST} Online!")

        

        try:
                while True:
                        conn, address = socketConn.accept() 
                        if (address[0] == "10.13.8.3") :
                            socketConn.shutdown()
                            socketConn.close()
                            

                        thread = th.Thread(target = clientManager, args=(conn,address))

                        thread.start()

                        print(f"conexões ativas: {th.active_count() - 1}")

        except:
                print(f"Desligando o servidor: [{HOST}]")

        finally:
             socketConn.close()

server()
            