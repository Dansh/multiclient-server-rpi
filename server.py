
import socket
from threading import Thread
import threading
import time



class Server:
    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 65432
        self.PASSWORD = "Tc6^g*VfWP+D{U4e"
        self.trashkey = "sH46HJ*/-"
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.HOST, self.PORT))
        self.active_connections = {}
        self.run()
        
    def run(self):      
        print("[STARTING] server is starting...") 
        self.server.listen()
        print(f"[LISTENING] Server is listening on\nip - {self.HOST}\nPORT - {self.PORT}")
        while True:
            conn, addr = self.server.accept()
            thread = Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            

    def handle_client(self, conn, addr):  
        password = conn.recv(1024).decode()
        conn.send("PASSWORD ARRIVED".encode())
        if password == self.PASSWORD:
            conn_name = conn.recv(1024).decode()
            connected = True
            conn.send("CONNECTED".encode())
            print("[NEW CONNECTION] new connection from " + str(addr))
            time.sleep(1)
            if conn_name == "Yarin":
                conn_name = "Son of a bitch"
            print(f"{conn_name} is connected :)")
            time.sleep(1) 
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
            self.active_connections[conn] = conn_name
        else:
            print("[ACCESS_DENIED] incorrect password from " + str(addr))
            conn.send("INCORRECT PASSWORD, please don't hack.".encode())
            connected = False        
        while connected:           
            msg_length = conn.recv(64).decode()
            conn.send((self.trashkey + "trash").encode())
            conn.send("LEN_RECV".encode())
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode()                                   
                if msg == "!DISCONNECT":
                    connected = False 
                    print(f"{addr} - DISCONNECTED FROM THE SERVER")
                    time.sleep(1)
                    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 2}")
                else:
                    print(f"[{addr}] - ({conn_name}): {msg}")
                    self.broadcast(msg, sender=conn)

        conn.close()

    def broadcast(self, msg, sender=None):
        if sender is not None:
            for client in self.active_connections.keys():
                if sender != client:
                    print(self.active_connections[sender])  
                    client.send((f"{self.active_connections[sender]}:  {msg}").encode())



server = Server()

