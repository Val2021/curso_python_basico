'''
Operador "and":
O operador "and" retorna True se ambas as expressões forem verdadeiras, caso contrário, retorna False.
'''
a = True
b = False
print(a and b)  # Saída: False

'''
Operador "or":
O operador "or" retorna True se pelo menos uma das expressões for verdadeira, caso contrário, retorna False.
'''
a = True
b = False
print(a or b)  # Saída: True

'''
Operador "not":
O operador "not" inverte o valor de uma expressão booleana. Se a expressão for True, o operador "not" retorna False e vice-versa.
'''
a = True
print(not a)  # Saída: False

'''
Combinação de operadores booleanos:
É possível combinar os operadores booleanos para criar expressões mais complexas.
'''
a = True
b = False
c = True
print((a and b) or (not c))  # Saída: False

'''
Além desses operadores básicos, Python também possui outros operadores relacionais, como igualdade (==),
desigualdade (!=), maior que (>), menor que (<), maior ou igual a (>=), e menor ou igual a (<=).
Esses operadores retornam valores booleanos com base na comparação entre os operandos.
'''
