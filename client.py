import socket
from tkinter import *
import random

print('Enter your IP-address: ')
ip = input()
print('Enter port: ')
port = int(input())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))


def click():
    phrases = [
        "Даааааа",
        "МолодЕец!",
        "УффФфффФфФ",
        "Ещё!!",
        "ТыКТыК",
        "Сюда!1!!!",
        "Даааваааай!",
        "Ееееееее"
    ]
    rand_num = random.randint(0, 7)
    while button["text"] == phrases[rand_num]:
        rand_num = random.randint(0, 7)

    button["text"] = phrases[rand_num]
    client.send("1".encode("utf-8"))


root = Tk()
root.title("БАТОН")
root.geometry("500x250")
root.resizable(False, False)

button = Button(text="НУ ТЫКНИ", height=20, width=100, font='Courier 50', command=click)
button.pack()

root.mainloop()


