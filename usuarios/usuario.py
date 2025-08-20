# blibliotecas importadas para conexão, janela GUI, códigos simultâneos e criptografia SSL 
import socket
import tkinter as tinker
import threading
from tkinter import scrolledtext as caixa
from tkinter import *
import ssl
from conversas import *

# variaveis de conexão de rede local
host = '127.0.0.1'
entrada = 12345

# cria uma autenticação para o servidor sem requerer um certificado para conexão
SSL_janela = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
SSL_janela.check_hostname = False
SSL_janela.verify_mode = ssl.CERT_NONE

# abre conexão com socket e aplica SSL
usuario = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tls_usuario = SSL_janela.wrap_socket(usuario, server_hostname=host)
# conecta substituindo na variavel
tls_usuario.connect((host, entrada))
 
# funções de mensagem 
def receber_mensagens():
    while True:
        try:
            #descriptografa mensagens recebidas no formato de 1024 de range maximo de dados
            mensagem_recebida = tls_usuario.recv(1024).decode()
            # chama função para gravar mensagem no txt
            escreverDados(str("Outro diz : "+mensagem_recebida + "\n"), 1)
            
            if not mensagem_recebida:
                break
            # insere mensagens na janela GUI
            texto_chat.config(state='normal')
            texto_chat.insert(tinker.END, "outro diz: " + mensagem_recebida)
            texto_chat.config(state='disabled')
        except:
            break

def enviar_mensagem():
    # capta a mensagem digitada pelo usuario na GUI
    captar_mensagem = str(texto.get())
    if captar_mensagem:
        # envia as mensagens usando o envio de dados pela a conexão socket 
        tls_usuario.sendall((captar_mensagem + "\n").encode())
        escreverDados(str("Voce : " +captar_mensagem + "\n"), 1)
        # mostra as mensagens digitadas pelo proprio usuario na GUI
        mostrar_mensagens(captar_mensagem)

def mostrar_mensagens(exibir_mensagem):
    texto_chat.config(state='normal')
    texto_chat.insert(tinker.END, "Voce: " + exibir_mensagem + '\n')
    texto_chat.config(state='disabled')
    texto.delete(0, tinker.END)


def mensagens_anteriores():
    lerDados(1)
    for mensagens in dados_usuario:
        mostrar_mensagens(mensagens)

# abre a configuração da janela e estabelece a geometria dela
janela = tinker.Tk()
janela.geometry("400x300")
janela.configure(bg='black')

# configuração da barra de titulo e estilo
barra_titulo = tinker.Frame(janela, bg='white', relief='raised', bd=0, height=28)
barra_titulo.pack(fill=tinker.X)
etiqueta_titulo = tinker.Label(barra_titulo, text=" Chat - CMD Style ", bg='white', fg='black', font=('Consolas', 10, 'bold'))
etiqueta_titulo.pack(side=tinker.LEFT, padx=8)

# parte do corpo da janela e para entrada de mensagens
frame_corpo = tinker.Frame(janela, bg='black')
frame_corpo.pack(fill=tinker.BOTH, expand=True)
texto_chat = caixa.ScrolledText(frame_corpo, bg='black', fg='white', insertbackground='white', font=('Consolas', 11), state='disabled', wrap=tinker.WORD)
texto_chat.pack(padx=10, pady=10, fill=tinker.NONE, expand=True)
texto_chat.place(x=10, y=10, width=375, height=240)

# area de captacao de mensagens para parametros das funções
texto = tinker.Entry(frame_corpo, bg='black', fg='white', insertbackground='white', font=('Consolas', 11))
texto.place(x=10, y=222, width=375, height=28)
texto.focus_set()

# botao enviar para chamar as funcoes obtendo o texto digitado 'texto.get()'
botao_enviar = tinker.Button(frame_corpo, text="Enviar", bg='#222', fg='white', font=('Consolas', 10), bd=0, command=enviar_mensagem)
botao_enviar.place(x=175, y=250)

# funcao para funcionar a tecla enter alem do botao
def tecla_enter(event):
    enviar_mensagem()
texto.bind('<Return>', tecla_enter)

# threading para multi arquivos rodando ao mesmo tempo
nucleo = threading.Thread(target=receber_mensagens)
nucleo.daemon = True

# exibir as configuracoes de SSL
print(tls_usuario.version())
print(tls_usuario.cipher())
print(tls_usuario.getpeercert())

nucleo.start()
mensagens_anteriores()
janela.mainloop()
