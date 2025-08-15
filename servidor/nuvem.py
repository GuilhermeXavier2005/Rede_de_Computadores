import socket
import threading
import ssl

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
            usu.close()
            break


host = '127.0.0.1'
entrada = 12345

usuarios_conectado = []

SSL = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
SSL.load_cert_chain(certfile="../TLS/nuvem.crt", keyfile="../TLS/nuvem.key")

servidor =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((host, entrada))

servidor.listen()

print(f'{servidor} aguardando conexões na porta {entrada}')

while True:
    usuario, conexao = servidor.accept()
    TLS_usuario = SSL.wrap_socket(usuario, server_side=True)

    dados = TLS_usuario.recv(1024)
    usuarios_conectado.append(TLS_usuario)
    nucleo = threading.Thread(target=tratamento_cliente, args=(TLS_usuario,))
    nucleo.start()