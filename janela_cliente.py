import tkinter as tinker
from tkinter import scrolledtext as caixa
from tkinter import *
import threading

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
texto_chat.place(x=0, y=0)

texto = tinker.Entry(janela, background='grey', width=10, font='Arial 11')
texto.pack(padx=10, pady=(0,5), fill=tinker.X)

botao_enviar = tinker.Button(janela, text="Enviar", command=enviar_mensagem())
botao_enviar.pack(pady=(0,10))
botao_enviar.place(x=175, y=250)

texto_inicial = Label(janela, text="primeiros testes com janela", font="Arial 11")
texto_inicial.place(x=100,y=35)
janela.mainloop()