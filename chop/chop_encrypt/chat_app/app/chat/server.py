import socket
import threading

class ChatServer:
    def __init__(self, host='localhost', port=12345):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.clients = []
        self.nicknames = []

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Server listening on {self.host}:{self.port}")

        while True:
            client, address = self.server_socket.accept()
            print(f"Connection established with {address}")

            self.clients.append(client)
            client.send('NICK'.encode('utf-8'))
            nickname = client.recv(1024).decode('utf-8')
            self.nicknames.append(nickname)

            print(f"Nickname of the client is {nickname}")
            broadcast_message = f"{nickname} joined the chat!".encode('utf-8')
            self.broadcast(broadcast_message)

            thread = threading.Thread(target=self.handle_client, args=(client,))
            thread.start()

    def broadcast(self, message):
        for client in self.clients:
            client.send(message)

    def handle_client(self, client):
        while True:
            try:
                message = client.recv(1024)
                self.broadcast(message)
            except:
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                broadcast_message = f'{nickname} left the chat.'.encode('utf-8')
                self.broadcast(broadcast_message)
                self.nicknames.remove(nickname)
                break

if __name__ == "__main__":
    server = ChatServer()
    server.start()
