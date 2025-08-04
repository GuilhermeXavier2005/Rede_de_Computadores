import socket
import tkinter as tinker
from tkinter import scrolledtext as caixa
from tkinter import *
import threading

host = '127.0.0.1'
entrada = 12345

usuario = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
usuario.connect((host, entrada))

def enviar_mensagem():
    captar_mensagem = texto.get()
    if captar_mensagem:
        texto_chat.config(state='normal')
        texto_chat.insert(tinker.END, "Você: " + captar_mensagem + '\n')
        texto_chat.config(state='disabled')
        texto.delete(0, tinker.END)

janela = tinker.Tk()
janela.title("Chat com computador")
janela.geometry("400x300")

texto_chat = caixa.ScrolledText(janela, state='disable', wrap = tinker.WORD)
texto_chat.pack(padx=10, pady=10, fill=tinker.NONE, expand=True)
texto_chat.place(x=0, y=100)

texto = tinker.Entry(janela, background='grey', width=10, font='Arial 11')
texto.pack(padx=10, pady=(0,5), fill=tinker.X)

botao_enviar = tinker.Button(janela, text="Enviar", command=enviar_mensagem())
botao_enviar.pack(pady=(0,10))
botao_enviar.place(x=175, y=250)

texto_inicial = Label(janela, text="voce usuario diz :", font="Arial 11")
texto_inicial.place(x=100,y=1)
janela.mainloop()

print(f"usuario: {usuario} conectado..")

while True:
    mensagem_usuario = input(f"Voce usuario diz: ")
    usuario.send(mensagem_usuario.encode())
    resposta_servidor = usuario.recv(1024).decode()
    print(f"servidor responde {resposta_servidor}")