'''
O laço "for" em Python é usado para iterar sobre uma sequência (como uma lista, uma string, um dicionário etc.) 
ou para repetir um bloco de código um número específico de vezes. É uma estrutura muito útil para percorrer
elementos em uma coleção de dados.
'''

'''
for i in sequência:
    # bloco de código a ser executado para cada (i)
'''
'''
Estrutura básica:
"for" => Indica o início do laço
"i" => Variável temporária que vai receber os elementos de cada interação do laço
"in" => Separa a variável (i) da sequencia a ser percorrida
"sequencia" =>  É a coleção de elementos sobre a qual o laço "for" irá iterar/percorrer
Identação

'''

a = "Hello, world!"

for i in a:
    print(i)


'''
Usando "for" com "if/else"
'''

frase = "Python é uma linguagem poderosa"

for letra in frase:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        print(letra, "é uma vogal")
    else:
        print(letra, "é uma consoante")



