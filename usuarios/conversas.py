entrada_dados = 0
dados_usuario = []

def usuario_1_2(parametro):
    if parametro == 1:
        arquivo_dados = 'dados_usuario_1.txt'
    elif parametro == 2: 
        arquivo_dados = 'dados_usuario_2.txt'
    return arquivo_dados

def lerDados(parametro=0):
    if parametro:
        abrir_arquivo = usuario_1_2(parametro)
    with open(abrir_arquivo, 'r') as leitura:
        if not leitura:
            print("falha ao abrir o arquivo...")
            return 0
        for dados in leitura:
            dados_usuario.append(dados)

def escreverDados(gravar_dados, parametro):
    abrir_arquivo = usuario_1_2(parametro)
    with open(abrir_arquivo, 'w+') as escritura:
        if not escritura:
            print("falha em salvar conversa")
            return 0

        lerDados(parametro)
        dados_usuario.append(gravar_dados)
        if gravar_dados:
            for contador in range(len(dados_usuario)): 
                if len(dados_usuario) < 3 and len(dados_usuario) != 0:
                    escritura.write(dados_usuario[contador])
                else:
                    dados_usuario.clear()
                    escritura.write('')
