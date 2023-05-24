'''
O módulo os.path em Python fornece várias funções úteis para manipulação 
de caminhos e nomes de arquivos. Essas funções ajudam a lidar com caminhos 
de forma portátil, independentemente do sistema operacional.
'''

'''
1 - Juntar partes de um caminho
'''
import os

diretorio = "/caminho/para/o/diretorio"
nome_arquivo = "arquivo.txt"
caminho_completo = os.path.join(diretorio, nome_arquivo)
print(caminho_completo)


'''
2 - Obter o nome do diretório de um caminho
'''

caminho = "6_arquivos/2_modulo_os/3_manipulacao_caminhos.py"
nome_diretorio = os.path.dirname(caminho)
print(nome_diretorio)

'''
2 - Obter o nome do arquivo de um caminho:
'''

caminho = "6_arquivos/2_modulo_os/3_manipulacao_caminhos.py"
nome_arquivo = os.path.basename(caminho)
print(nome_arquivo)


'''
3 - Verificar se um caminho é absoluto
'''
caminho = ""
if os.path.isabs(caminho):
    print("O caminho é absoluto.")
else:
    print("O caminho não é absoluto.")