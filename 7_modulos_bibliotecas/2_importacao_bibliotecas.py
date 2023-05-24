'''
Em Python, uma biblioteca é um conjunto de módulos e pacotes contendo
funcionalidades pré-escritas que podem ser reutilizadas em projetos de software. 
Uma biblioteca fornece um conjunto de ferramentas, funções, classes e recursos 
que facilitam o desenvolvimento de aplicativos, poupando tempo e esforço ao fornecer
implementações prontas para tarefas comuns.
'''

'''
1 - Bibliotecas padrão (built-in libraries)
2 - Bibliotecas de terceiros
'''


'''
As bibliotecas de terceiros em Python podem ser encontradas no Python Package Index (PyPI),
que é o principal repositório para pacotes.
Para acessar o PyPI, você pode visitar o site oficial em https://pypi.org/.
Para instalar, atualizar e desinstalar bibliotecas em python, usa-se o comando pip
'''

'''
A importação de bibliotecas em Python é feita usando a palavra-chave import
Exemplos de importação de bibliotecas:
'''

'''
1 - Importação básica:
'''

import nome_da_biblioteca


'''
2 - import nome_da_biblioteca as alias
'''
import nome_da_biblioteca as alias


'''
3 - Importação de módulos específicos:
'''
from nome_da_biblioteca import nome_do_módulo


'''
4 - Importação de todos os módulos:
'''
from nome_da_biblioteca import *

'''
5 - Possibilidade de conflito quando se importa todos os modulos de uma bilioteca
Exemplo:
'''

from math import *
from numpy import *

print(sqrt(9))  #???????

'''
6 - Para evitar esse conflito:
'''
import math
import numpy

print(math.sqrt(9)) 


