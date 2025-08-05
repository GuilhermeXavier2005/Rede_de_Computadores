import socket
import threading

def verificar_usuarios(mensagem, receptor):
    for usu in usuarios_conectado:
        if usu != receptor:
            try:
                usu.send(mensagem)
            except:
                usuarios_conectado.remove(usu)

def tratamento_cliente(usu):
    while True:
        try:
            mensagem_usuario = usu.recv(1024)
            verificar_usuarios(mensagem_usuario, usu)
        except:
            usuarios_conectado.remove(usu)
            usuario.close()
            break


host = '127.0.0.1'
entrada = 12345

usuarios_conectado = []

servidor =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((host, entrada))

servidor.listen()

print(f'{servidor} aguardando conexões na porta {entrada}')

while True:
    usuario, conexao = servidor.accept()
    usuarios_conectado.append(usuario)
    nucleo = threading.Thread(target=tratamento_cliente, args=(usuario,))
    nucleo.start()