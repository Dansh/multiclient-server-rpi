import tkinter as tk

BIG_FONT = ("Verdana", 46)
BIG_MEDIUM_FONT = ("Verdana", 37)
MEDIUM_FONT = ("Verdana", 28)

class ChatUI:
    def __init__(self, master):
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
        self.enter_name_button = tk.Button(self.master, text="CHAT!", font=BIG_FONT, command=self.init_chat_elements)
        self.enter_name_button.pack(side="top", pady=30)
        self.current_items = [self.name_title, self.name_input, self.enter_name_button]

    
          

    def init_chat_elements(self):
        self.user_name = self.name_input.get()
        self.master.geometry("550x850")
        for item in self.current_items:
            item.destroy()
        self.title = tk.Label(self.master, text="Pip Chat", font=BIG_FONT)
        self.title.pack(side="top", pady=20)
        self.msg_text_label = tk.Label(self.master, text="some text", font=MEDIUM_FONT)
        self.msg_text_label.pack(side="top", pady=30)
        self.send_button = tk.Button(self.master, font=MEDIUM_FONT, text="send", command=lambda: self.update_text(writer=self.user_name))
        self.send_button.pack(side="bottom", pady=50)
        self.input_box = tk.Entry(self.master, width=10, font=BIG_FONT)
        self.input_box.pack(side="bottom", pady=0 , padx=40)
        

        
    def update_text(self, writer):
        new_text = self.input_box.get()
        self.input_box.delete(0, 'end')
        if new_text != "":
            if writer == self.user_name:
                self.msg_text += f"\n{new_text}"
            else:
                self.msg_text += f"\n{writer}:{new_text}"
            self.msg_text_label.destroy()
            self.msg_text_label = tk.Label(self.master, text=self.msg_text, font=MEDIUM_FONT)
            self.msg_text_label.pack(side="top", pady=30)

            

