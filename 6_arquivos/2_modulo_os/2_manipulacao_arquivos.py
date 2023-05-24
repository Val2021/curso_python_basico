'''
Manipulação de arquivos e diretórios
'''

'''
1 - Criar um diretório
'''
import os

diretorio = "novo_diretorio"
#os.mkdir(diretorio)


'''
2 - Excluir um arquivo
'''
arquivo = "arquivo.txt"
#os.remove(arquivo)

'''
3 - Excluir um diretório vazio:
'''
diretorio = "diretorio_vazio"
#os.rmdir(diretorio)

'''
4 - Listar arquivos e diretórios em um diretório:
'''

diretorio = "diretorio"
conteudo = os.listdir(diretorio)
for item in conteudo:
    print(item)

'''
5 - Verificar se um arquivo ou diretório existe
'''

arquivo = "arquivo.txt"
if os.path.exists(arquivo):
    print("O arquivo existe.")
else:
    print("O arquivo não existe.")