#import socket module
import socket

def TCPserver():
    #mengaitkan ke alamat dan port tertentu
    SERVER_HOST = "localhost"
    SERVER_PORT = 8080

    #membuat TCP socket
    sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    #mendengarkan koneksi dari client
    sock_server.bind((SERVER_HOST, SERVER_PORT))
    sock_server.listen()

    print("Server Ready....")

    while True:
        #menerima koneksi dari client
        sock_client, client_address = sock_server.accept()
  
        #meminta 
        request = sock_client.recv(1024).decode()
        print("Dari client: "+request)

        #memberi respon 
        response = handle_request()
        sock_client.send(response.encode())

        #menutup koneksi client
        sock_client.close()

    #menutup server
    sock_server.close()
    
def handle_request():
     try:
        response_line = "HTTP/1.1 200 OK\r\n"
        content_type = "Content-type: text/HTML\r\n\r\n"
        
        file = open("docs_HTML/idx.html",'r')
        message_body = file.read()
        file.close()
        
        response = response_line+content_type+message_body
        return response
     
     except:
        response_line = "HTTP/1.1 404 Not Found\r\n"
        content_type = "Content-type: text/HTML\r\n\r\n"
        
        file = open("docs_HTML/idx1.html",'r')
        message_body = file.read()
        file.close()
        
        response = response_line+content_type+message_body
        return response

if __name__ == "__main__":
    TCPserver()