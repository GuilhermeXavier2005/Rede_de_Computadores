import socket
import tkinter as tinker
import threading
from tkinter import scrolledtext as caixa
from tkinter import *

host = '127.0.0.1'
entrada = 12345

usuario = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
usuario.connect((host, entrada))

def receber_mensagens():
    while True:
        try:
            mensagem_recebida = usuario.recv(1024).decode()
            texto_chat.config(state='normal')
            texto_chat.insert(tinker.END, "outro diz: " + mensagem_recebida + '\n')
            texto_chat.config(state='disabled')
        except: 
            break

def enviar_mensagem():
    captar_mensagem = str(texto.get())
    if captar_mensagem:
        texto_chat.insert(tinker.END, "Você: " + captar_mensagem + '\n')
        usuario.send(captar_mensagem.encode())
        mostrar_mensagens(captar_mensagem)

def mostrar_mensagens(exibir_mensagem):
    texto_chat.config(state='normal')
    texto_chat.insert(tinker.END, "Você: " + exibir_mensagem + '\n')
    texto_chat.config(state='disabled')
    texto.delete(0, tinker.END)

def tecla_enter(event):
    enviar_mensagem()

def iniciar_arraste(event):
    janela.x = event.x
    janela.y = event.y

def arrastar(event):
    x = event.x_root - janela.x
    y = event.y_root - janela.y
    janela.geometry(f"+{x}+{y}")


janela = tinker.Tk()
janela.geometry("400x300")
janela.configure(bg='black')

barra_titulo = tinker.Frame(janela, bg='white', relief='raised', bd=0, height=28)
barra_titulo.pack(fill=tinker.X)
etiqueta_titulo = tinker.Label(barra_titulo, text=" Chat - CMD Style ", bg='white', fg='black', font=('Consolas', 10, 'bold'))
etiqueta_titulo.pack(side=tinker.LEFT, padx=8)
barra_titulo.bind('<Button-1>', iniciar_arraste)
barra_titulo.bind('<B1-Motion>', arrastar)
etiqueta_titulo.bind('<Button-1>', iniciar_arraste)
etiqueta_titulo.bind('<B1-Motion>', arrastar)

frame_corpo = tinker.Frame(janela, bg='black')
frame_corpo.pack(fill=tinker.BOTH, expand=True)
texto_chat = caixa.ScrolledText(frame_corpo, bg='black', fg='white', insertbackground='white', font=('Consolas', 11), state='disabled', wrap=tinker.WORD)
texto_chat.pack(padx=10, pady=10, fill=tinker.NONE, expand=True)
texto_chat.place(x=10, y=10, width=375, height=240)

texto = tinker.Entry(frame_corpo, bg='black', fg='white', insertbackground='white', font=('Consolas', 11))
texto.place(x=10, y=222, width=375, height=28)
texto.focus_set()

botao_enviar = tinker.Button(frame_corpo, text="Enviar", bg='#222', fg='white', font=('Consolas', 10), bd=0, command=enviar_mensagem)
botao_enviar.place(x=175, y=250)


def tecla_enter(event):
    enviar_mensagem()
texto.bind('<Return>', tecla_enter)

nucleo = threading.Thread(target=receber_mensagens)
nucleo.daemon = True
nucleo.start()

janela.mainloop()
