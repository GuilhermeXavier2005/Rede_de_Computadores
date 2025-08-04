import socket

host = '127.0.0.1'
entrada = 12345

servidor =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((host, entrada))

servidor.listen()

print(f'{servidor} aguardando conexões na porta {entrada}')
conexao, endereco = servidor.accept()

print(f'{servidor} conectado em {endereco}')

while True:
    fluxo_dados = conexao.recv(1024).decode()
    if not fluxo_dados:
        break
    print(f'usuario escreve {fluxo_dados}: ')
    resposta = input("voce responde {servidor}: ")
    conexao.send(resposta.encode())

conexao.close()