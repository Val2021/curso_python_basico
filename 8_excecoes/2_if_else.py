'''
Também é possivel utilizar  blocos try-except combinados com if-else
'''

def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    else:
        print("A divisão foi realizada com sucesso.")
        return resultado


resultado = dividir(10, 2)
print("Resultado:", resultado)

resultado = dividir(10, 0)


def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    else:
        if resultado > 10:
            print("O resultado é maior que 10.")
        else:
            print("O resultado é menor ou igual a 10.")
        return resultado

resultado = dividir(20, 2)
print("Resultado:", resultado)

resultado = dividir(5, 2)