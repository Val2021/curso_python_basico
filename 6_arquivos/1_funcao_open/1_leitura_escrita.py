'''
A função open() em Python é uma função embutida que permite abrir um arquivo e retornar um objeto do tipo arquivo. 
Esse objeto arquivo é usado para realizar operações de leitura, escrita e manipulação nos dados armazenados no arquivo.
'''


'''
A sintaxe básica da função open():

open(nome_arquivo, modo, encoding)

nome_arquivo => é uma string que representa o caminho ou o nome do arquivo que você deseja abrir.
modo => é uma string que especifica o modo de abertura do arquivo:
"r" para leitura
"w" para escrita
"a" para anexar conteúdo ao final do arquivo
entre outros
'''


'''
Escrevendo um arquivo em modo de escrita ('w')
'''

arquivo = open("6_arquivos/arquivo.txt", "w")
arquivo.write("Olá, mundo!\n")  
arquivo.close()

'''
Adicionar conteúdo a um arquivo existente sem sobrescrevê-lo
'''
arquivo = open("6_arquivos/arquivo.txt", "a")
arquivo.write("Olá, Rio!") 
arquivo.close()


'''
Abrir um arquivo em modo de leitura usando o modo "r"
Para ler o conteudo dos arquivos pode-se usar os seguintes métodos:
read(), readline() ou readlines()
'''
arquivo = open("6_arquivos/arquivo.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

'''
É Recomendado o uso do bloco with 
'''

nome_arquivo = "6_arquivos/arquivo.txt"

with open(nome_arquivo, "w") as arquivo:
    arquivo.write("Exemplo de conteúdo.\n")
    arquivo.write("Outra linha de texto.\n")
    arquivo.write("Mais uma linha.\n")

print("Arquivo criado com sucesso!")



'''
Outros modos:
Modo "b" (binário) => É usado para abrir um arquivo em modo binário e é adequado para leitura ou escrita de arquivos binários
Modo "r+" (leitura e escrita)
'''

with open("6_arquivos/imagem.png", "rb") as arquivo:
    dados = arquivo.read()
   


with open("6_arquivos/arquivo.txt", "r+") as arquivo:
    conteudo = arquivo.read()
    arquivo.write("Texto adicionado")