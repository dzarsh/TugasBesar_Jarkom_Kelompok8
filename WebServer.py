#import socket module
from socket import *

def TCPserver():
    #mengaitkan ke alamat dan port tertentu
    serverHost = 'localhost'
    serverPort = 8080
    
    #membuat TCP socket
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    #mendengarkan koneksi dari client
    serverSocket.bind((serverHost, serverPort))
    serverSocket.listen()

    while True:
        #menerima koneksi dari client
        print("Server Ready....")
        connectionSocket, addr = serverSocket.accept()

        #meminta 
        request = connectionSocket.recv(1024).decode()
        print("Dari client: "+request)

        #memberi respon 
        response = handleRequest()
        connectionSocket.send(response.encode())

        #menutup koneksi
        connectionSocket.close()

    #menutup server
    serverSocket.close()
    
def handleRequest():
    try: 
        responseLine = "HTTP/1.1 200 OK\r\n"
        contentType = "Content-type: text/HTML\r\n\r\n"

        file = open("docs_HTML/idx.html",'r')
        messageBody = file.read()
        file.close()

        response = responseLine+contentType+messageBody
        return response

    except IOError:
        responseLine = "HTTP/1.1 404 Not Found\r\n"
        contentType = "Content-type: text/HTML\r\n\r\n"
    
        file = open("docs_HTML/idx1.html", 'r')
        messageBody = file.read()
        file.close()

        response = responseLine+contentType+messageBody
        return response
    
if __name__ == '__main__':
    TCPserver()
