#import socket module
from socket import *
#import modul sys
import sys

#menentukan nama host dan nomor port
server_name = "localhost"
server_port = 8080

#membuat tcp socket clietnt
client_socket = socket(AF_INET, SOCK_STREAM)
#menghubungi server
client_socket.connect((server_name, server_port)) #menghubungkan client dengan IP dan port
print("Server Terkoneksi") #mencetak server telah terkoneksi

#meminta input dari user
fileName = input("Masukkan nama file : ") #meminta masukan nama file
request = "GET "+str(fileName)+" HTTP/1.1" #filename akan secara otomatis melakukan permintaan HTTP dari client ke server

#mengirim pesan request ke server
client_socket.send(request.encode()) #dan mengencode merubah string menjadi byte

#menerima pesan dari server
returnFromServer = client_socket.recv(4096) #recv 4096 menunjukkan ukuran max darta yang diterima dari server

#mengeluarkan pesan yang didapat dari server
while(len(returnFromServer)>0): #jika panjang returnFromServer lebih dari 0 maka akan dieksekusi
    print(returnFromServer.decode()) #mencetak output dengan mengdecode byte ke string
    returnFromServer = client_socket.recv(4096) #recv 4096 menunjukkan ukuran max darta yang diterima dari server

#menutup koneksi dengan server
client_socket.close()




# from socket import *
# import sys


# servername = "localhost"
# serverport = 8080

# #membuka koneksi TCP dengan server
# sock_client = socket(AF_INET, SOCK_STREAM)
   
# sock_client.connect((servername, serverport))
# print("Server Terkoneksi")


        
# namafile = input("Masukan nama file : ")
# request = "GET"+str(namafile)+"HTTP/1.1"

# #mengirim server ke request
# sock_client.send(request.encode())


# returnFromServer = sock_client.recv(4096)


# while(len(returnFromServer)>0):
#    print(returnFromServer.decode())
#    returnFromServer = sock_client.recv(4096)

# #menutup koneksi
# sock_client.close()


