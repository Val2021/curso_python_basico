def contar_ate(numero):
    contador = 1
    while contador <= numero:
        print(contador)
        contador += 1


def imprimir_repetido(caractere, quantidade):
    contador = 0
    while contador < quantidade:
        print(caractere, end=",")
        contador += 1
  


def imprimir_repetido(caractere, quantidade):
    contador = 0
    resultado = ""
    while contador < quantidade:
        resultado += caractere
        contador += 1
    return resultado

