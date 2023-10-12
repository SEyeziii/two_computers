from tkinter import *
import tkinter as tk
import socket
from pathlib import Path

print('Enter your IP-address: ')
ip = input()
print('Enter port: ')
port = int(input())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))

server.listen(2)

user, address = server.accept()


def on_button_click():
    button.config(image=get_next_image())


def get_next_image():
    return next(NEXT_IMAGE)


def next_image_generator():
    photo_list = [
        tk.PhotoImage(file=Path("assets", "cat1.png")),
        tk.PhotoImage(file=Path("assets", "cat2.png")),
        tk.PhotoImage(file=Path("assets", "cat3.png")),
        tk.PhotoImage(file=Path("assets", "cat4.png")),
        tk.PhotoImage(file=Path("assets", "boom.png"))
    ]

    while True:
        yield from photo_list


NEXT_IMAGE = next_image_generator()

root = Tk()
root.geometry('750x750')
root.resizable(False, False)

button = Button(root, image=get_next_image())
button.pack()

while True:
    root.update()
    message = user.recv(1024).decode("utf-8")
    if not message:
        root.update()
    else:
        button.config(image=get_next_image())
















