import socket
import threading
import sys

class ChatClient:
    def __init__(self, host='localhost', port=12345):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port

    def connect(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print("Connected to server.")
            self.listen_thread = threading.Thread(target=self.receive_messages)
            self.listen_thread.start()
        except Exception as e:
            print(f"Failed to connect to server: {e}")
            sys.exit(1)

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    print(f"\r{message}\nYou: ", end='')
                else:
                    # Server has closed the connection
                    break
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    def send_message(self, message):
        try:
            self.client_socket.sendall(message.encode('utf-8'))
        except Exception as e:
            print(f"Failed to send message: {e}")

    def run(self):
        self.connect()
        print("Type 'exit' to leave the chat.")
        while True:
            message = input("You: ")
            if message.lower() == 'exit':
                break
            self.send_message(message)

        self.client_socket.close()
        sys.exit(0)


if __name__ == "__main__":
    client = ChatClient()
    client.run()
