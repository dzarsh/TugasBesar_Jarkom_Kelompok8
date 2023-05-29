#import modul socket untuk membuat koneksi antara client dengan server
import socket
#import modul os untuk dapat mengakses direktori, mengelola file dll
import os

#mengikat socket ke alamat dan port tertentu
serverHost = '' #dapat diisi dengan IP laptop anda
serverPort = 8080 #menghubungkan koneksi dengan port 8080

#membuat socket TCP 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #untuk menampung socket baru yang digunakan sebagai socket server

#fungsi untuk mengambil konten file yang diminta oleh klien
def get_file(filename): #fungsi get_file dengan parameter filename
    with open(filename, 'rb') as file: #membuka file dengan fungsi open dan 'rb' untuk membaca file dalam biner
        return file.read() #mengembalikan isi dari suatu file/objek

#fungsi untuk membuat HTTP response message
def create_response(filename, content): #fungsi create_response
    response_header = "HTTP/1.1 200 OK\r\n" #menampung string dari fungsi response menggunakan protokol HTTP, 200 kode telah berhasil. OK menunjukkan pesan tidak memiliki kesalahan
    if filename.endswith(".html"): #file yang dapat dibaca adalah dalam bentuk html
        response_header += "Content-Type: text/html\r\n\r\n".format(len(content)) #konten tipe ditetapkan dalam bentuk html dengan melakukan format

    return response_header.encode() + content #mengembalikan gabungan byte string dari header response dan konten yang dikirimkan untuk response HTTP

#fungsi untuk menangani koneksi dari klien
def handle_connection(client_socket): #fungsi handle_connection
    #menerima data dari client
    message = client_socket.recv(1024).decode() #menerima pesan dari klien melalui socket dan mendekodekannya dari byte ke string
    request_line = message.split("\r\n") #memisahkan pesan menjadi baris" terpisah yang berisi informasi tentang request

    #mendapatkan path file yang diminta oleh klien 
    filename = request_line[0].split()[1][1:] #membagi baris berdasarkan spasi dan mengambil elemen kedua/index 1 dan menghilangkan / pada awan nama file

    #mengambil konten file
    if os.path.exists(filename): #Mengembalikan True jika path ada, dan False jika tidak.
        content = get_file(filename) #memanggil fungsi get_file untuk membaca file
        response = create_response(filename, content) #memanggil fungsi create_response untuk membuat response
    else:
        response = "HTTP/1.1 404 Not Found\r\n\r\n".encode() #jika file tidak sesuai makana kan muncul pesan error
        response += "<html><head></head><body><h1>404 Not Found</h1></body><html>\r\n\r\n".encode()

    #mengirim respon ke klien
    client_socket.sendall(response) #mengirim response dari server ke klien
    #dengan fungsi sendall digunakan untuk memastikan data yang dikirim lengkap
    print("Dari client: " +response.decode() +message) #mencetak response dan message yang akan ditampilkan diserver
    #menutup koneksisocket dengan klien
    client_socket.close() 

#fungsi utama
def main():
   #mengikat socket ke alamat dan port tertentu
    server_address = (serverHost, serverPort) #server_address berisi host dan port yang telah ditentukan
    server_socket.bind(server_address) #menghubungkan socket_server dengan server_address menggunakan fungsi bin

    #mendengarkan koneksi masuk
    server_socket.listen(1)
    print("Server Ready!!!") #menvetak server ready

    while True:
        #menerima koneksi dari klien
        client_socket, client_address = server_socket.accept()
        print("Menerima koneksi dari: ", client_address) #mencetak client_address

        #menangani koneksi dari klient secara terpisah (thread terpisah)
        handle_connection(client_socket)

        #menutup server socket
    server_socket.close()

if __name__ == '__main__': #memastikan bahwa code di bawahnya hanya dijalankan jika file dieksekusi
    main() #memanggil fungsi main
