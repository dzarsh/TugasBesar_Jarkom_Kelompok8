#import socket module
from socket import *
import sys #Modul sys digunakan untuk mengakses konfigurasi interpreter pada saat runtime dan berinteraksi dengan environment sistem operasi

serverHost = 'localhost' #menginisialisasi host
serverPort = 8080 #menginisialisasi nomor port

#membuat TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

#membuat function handleRequest untuk mengendalikan request
def handleRequest():
    while True:
        print("Ready to serve") #mencetak Ready to serve jika server telah siap
        connectionSocket, addr = serverSocket.accept() 
    
        try:
            message = connectionSocket.recv(1024).decode()
            filename = message.split()[1] #membuat split untuk mempharsing
            f = open(filename[1:]) 
            outputdata = f.read() #untuk membaca file
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode()) #mengembalikan request

            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except IOError:
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
            connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body><html>\r\n\r\n".encode())
            connectionSocket.close()
 
 #membuat function untuk TCP server
def TCPServer():
    #mendengarkan koneksi dari client
    serverSocket.bind((serverHost, serverPort))
    serverSocket.listen()

    while True:
        #menerima koneksi dari client
        print("Server Ready....!")
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

if __name__ == '__main__':
        TCPServer()

sys.exit()

