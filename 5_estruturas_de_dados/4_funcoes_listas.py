'''
Exemplos de funções com listas
'''

'''
Função que retorna o maior valor em uma lista:
'''
def encontrar_maior(lista):
    maior = lista[0] 
    for num in lista:
        if num > maior:
            maior = num
    return maior

print(encontrar_maior([1,4,5,6,3]))


'''
1 - Função que retorna a soma de todos os elementos de uma lista:
'''

'''
2 - Função que retorna uma nova lista contendo apenas os números pares da lista original:
'''

