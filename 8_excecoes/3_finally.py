'''
O uso do bloco finally é útil para realizar ações de limpeza ou liberação de recursos,
como fechar arquivos, conexões de banco de dados ou desalocar memória. Isso garante que
essas ações sejam realizadas, independentemente de ocorrerem exceções ou não durante a
execução do bloco try.
'''

def ler_arquivo():
    arquivo = None
    try:
        arquivo = open("dados.txt", "r")
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:", conteudo)
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    finally:
        if arquivo:
            arquivo.close()
            print("Arquivo fechado.")

ler_arquivo()
