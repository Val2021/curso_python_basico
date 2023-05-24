'''
Em Python, o tratamento de exceções é realizado utilizando blocos try-except. 
O código que pode gerar uma exceção é colocado dentro do bloco try, e caso uma 
exceção ocorra, o fluxo de execução é desviado para o bloco except correspondente, 
onde é possível tratar a exceção ou tomar alguma ação apropriada. O tratamento de
exceções permite lidar com erros de forma controlada, executando um código alternativo
ou exibindo uma mensagem personalizada, por exemplo.
'''

def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")


resultado = dividir(10, 2)
print("Resultado:", resultado)

resultado = dividir(10, 0)



def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


resultado = dividir(10, 2)
print("Resultado:", resultado)

resultado = dividir(10, 0)




