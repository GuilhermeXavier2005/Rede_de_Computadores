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

def minimizar():
    janela.iconify()

def fechar():
    try:
        usuario.close()
    except:
        pass
    janela.destroy()

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

title_bar = tinker.Frame(janela, bg='white', relief='raised', bd=0, height=28)
title_bar.pack(fill=tinker.X)
title_label = tinker.Label(title_bar, text=" Chat - CMD Style ", bg='white', fg='black', font=('Consolas', 10, 'bold'))
title_label.pack(side=tinker.LEFT, padx=8)
title_bar.bind('<Button-1>', iniciar_arraste)
title_bar.bind('<B1-Motion>', arrastar)
title_label.bind('<Button-1>', iniciar_arraste)
title_label.bind('<B1-Motion>', arrastar)

btn_min = tinker.Button(title_bar, text='—', bg='white', fg='black', bd=0, padx=6, pady=0, command=minimizar, font=('Consolas', 10))
btn_min.pack(side=tinker.RIGHT, padx=(0,4))
btn_close = tinker.Button(title_bar, text='✕', bg='white', fg='black', bd=0, padx=6, pady=0, command=fechar, font=('Consolas', 10))
btn_close.pack(side=tinker.RIGHT)

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
