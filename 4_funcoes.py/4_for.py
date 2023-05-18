def contar_vogais(texto):
    vogais = 'aeiouAEIOU'
    contador = 0
    for caractere in texto:
        if caractere in vogais:
            contador += 1
    return contador

### fazer uma função aqui de contar pares