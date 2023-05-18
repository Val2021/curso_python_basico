'''
A estrutura de controle if/else é uma das mais importantes em Python (e em muitas outras linguagens de programação).
Ela permite que você tome decisões com base em condições específicas e execute diferentes blocos de código com base
nesses resultados.
'''


'''
A estrutura básica da declaração if/else em Python é a seguinte:

if condição:
    # bloco de código a ser executado se a condição for verdadeira
else:
    # bloco de código a ser executado se a condição for falsa

'''

'''
O "elif" é uma palavra-chave em Python que permite adicionar condições adicionais à estrutura if/else. 
'''
pontuacao = 80

if pontuacao >= 90:
    nota = "A"
elif pontuacao >= 80:
    nota = "B"
elif pontuacao >= 70:
    nota = "C"
elif pontuacao >= 60:
    nota = "D"
else:
    nota = "F"

print("Nota:", nota)

a = "Hello, World"

if 'e' in a:
    print("Yes, we have e!")
else:
    print("Sorry, we dont have it")



