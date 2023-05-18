
def contar_vogais(palavra):
    vogais = 0

    for letra in palavra:
        if letra.lower() in 'aeiou':
            vogais += 1

    if vogais == 0:
        print("A palavra não contém vogais.")
    elif vogais == 1:
        print("A palavra contém 1 vogal.")
    else:
        print(f"A palavra contém {vogais} vogais.")

# Chamada da função
contar_vogais("Python")


def calcular_media(notas):
    soma = sum(notas)
    quantidade = len(notas)
    media = soma / quantidade
    return media