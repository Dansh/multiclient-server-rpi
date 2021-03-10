import socket
import tkinter as tk
from threading import Thread

class Client:
    def __init__(self):
        self.HOST = '84.94.170.57'
        self.PORT = 65432
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.HOST, self.PORT))
        self.PASSWORD = "Tc6^g*VfWP+D{U4e"
        self.trashkey = "sH46HJ*/-"
        self.user_name = ""


    def run(self, name):
        self.client.send(self.PASSWORD.encode())
        self.client.recv(1024).decode()
        self.client.send(self.user_name.encode())     
        isConnected = self.client.recv(1024).decode()
        print(f"Hi {self.user_name}, you connected successfully!")
        self.check_for_data_thread = Thread(target=self.check_for_new_data)
        self.check_for_data_thread.start()


            
    def chekc_for_msg(self):
        name = self.client.recv(1024).decode()
        msg = self.client.recv(1024).decode()
        print(f"{name}: {msg}")


    def send_msg(self ,msg):
        def check_msg_size(self, msg):
            if len(msg) > 1024:
                return False
            return True
        valid_size = check_msg_size(self, msg)
        if valid_size:
            self.client.send(str(len(msg)).encode())
            self.client.recv(1024).decode() # recv an approved
            self.client.send(msg.encode())
        else:
            print("message too big, send another message")



        
