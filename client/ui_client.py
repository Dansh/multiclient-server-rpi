import tkinter as tk
from threading import Thread
from s_client import Client

BIG_FONT = ("Verdana", 46)
BIG_MEDIUM_FONT = ("Verdana", 37)
MEDIUM_FONT = ("Verdana", 28)

class ChatUI(Client):
    def __init__(self, master):
        Client.__init__(self)
        self.master = master
        master.title("A simple GUI")
        self.master.geometry("550x450")
        self.msg_text = ""
        self.user_name = ""
        self.init_get_name_elements()

    def init_get_name_elements(self):
        self.name_title = tk.Label(self.master, text="Enter Your Name", font=BIG_MEDIUM_FONT)
        self.name_title.pack(side="top", pady=30)
        self.name_input = tk.Entry(self.master, font=BIG_FONT, width=10)
        self.name_input.pack(side="top", pady=20)
        self.enter_name_button = tk.Button(self.master, text="CHAT!", font=BIG_FONT, command=self.change_user_name)
        self.enter_name_button.pack(side="top", pady=30)
        self.current_items = [self.name_title, self.name_input, self.enter_name_button]

    
    def change_user_name(self):
        self.user_name = self.name_input.get()
        self.run(self.user_name)
        self.init_chat_elements()

    
    def init_chat_elements(self):
        self.master.geometry("550x850")
        for item in self.current_items:
            item.destroy()
        self.title = tk.Label(self.master, text="Pip Chat", font=BIG_FONT)
        self.title.pack(side="top", pady=20)
        self.msg_text_label = tk.Label(self.master, text="some text", font=MEDIUM_FONT)
        self.msg_text_label.pack(side="top", pady=30)
        self.send_button = tk.Button(self.master, font=MEDIUM_FONT, text="send", command=lambda: self.send_and_update_text())
        self.send_button.pack(side="bottom", pady=50)
        self.input_box = tk.Entry(self.master, width=10, font=BIG_FONT)
        self.input_box.pack(side="bottom", pady=0 , padx=40)

    def check_for_new_data(self):
        while True:
            data = self.client.recv(1024).decode()
            if not data.startswith(self.trashkey):  
                self.update_text(data)  

    def send_and_update_text(self):
        self.send_msg(self.input_box.get()) 
        self.update_text(self_written = True) 

    def update_text(self, new_text="", self_written=False):
        if self_written:
            new_text = self.input_box.get()
            self.input_box.delete(0, 'end')
        if new_text != "":
            self.msg_text += f"\n{new_text}"
            self.msg_text_label.destroy()
            self.msg_text_label = tk.Label(self.master, text=self.msg_text, font=MEDIUM_FONT)
            self.msg_text_label.pack(side="top", pady=30)

            

root = tk.Tk()       
client = ChatUI(root)
root.mainloop()  
