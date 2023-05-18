'''
O laço de repetição "while" em Python é para repetir um bloco de 
código enquanto uma condição específica for verdadeira.
O laço, executa o conjunto de instruções até que a condição for falsa
'''

'''
A estrutura básica do "while" é a seguinte:

while condição:
    # bloco de código a ser repetido enquanto a condição for verdadeira
'''

contador = 1

while contador <= 5:
    print(contador)
    contador += 1

'''
O laço while precisa de um critério de parada, 
senão torna-se um loop infinito que consome recursos do computador
'''
