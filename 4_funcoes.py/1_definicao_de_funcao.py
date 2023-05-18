'''
Uma função em Python é um bloco de código que executa uma tarefa específica. 
Uma função é definida usando a  palavra-chave def, seguida pelo nome da função,
parênteses que podem conter parâmetros e um bloco de código indentado.
'''

'''
Estrutura básica de uma função em python

def nome_da_funcao(parametros):
    bloco de código da função
    realiza uma tarefa específica
    pode retornar um valor, se necessário

'''
'''
Elementos de uma função:

def => Palavra chave que especifica uma função
nome_da_funcao => Nomeia a função e deve seguir as convenções de nomenclatura do Python.
bloco de código => É o conjunto de instruções que a função executará quando for chamada.
return => É opcional. Retorna o resultado de uma função

'''

def somar(a, b):
    resultado = a + b
    return resultado


def exibir_mensagem():
    print("Olá! Esta é uma função sem retorno.")