import socket
import tkinter as tk
from threading import Thread
from ui_client import ChatUI

class Client:
    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 65432
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.HOST, self.PORT))
        self.PASSWORD = "Tc6^g*VfWP+D{U4e"
        self.name = ""
        root = tk.Tk()
        self.chat = ChatUI(root)
        root.mainloop()   
        self.run()

    def run(self):
        self.client.send(self.PASSWORD.encode())
        while self.name == "":
            print("here-1")
            self.name = self.chat.user_name
        print("here")
        self.client.send(self.name.encode())     
        isConnected = self.client.recv(1024).decode()
        print(f"Hi {self.name}, you connected successfully!")
        #thread = Thread(target=self.chekc_for_msg)
        #thread.start()
        while isConnected == "CONNECTED":
            msg = input("")
            self.send_msg(msg)

      
            
            
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

        
            


client = Client()

