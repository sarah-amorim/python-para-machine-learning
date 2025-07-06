# O módulo itertools utiliza-se de técnicas de programação funcional, como as funções geradoras, que são funções que retornam um objeto iterável.
import itertools

contador = itertools.count()

print(contador) # count(0)
print(next(contador)) # 0
next(contador) # 1
print(next(contador)) # 2

'''
A função count retorna um iterador. A variável chamada ‘contador’ recebe esse iterador e, à medida que é invocada, por meio da função next, é computado 
um novo valor a essa variável. Com isso, esse valor é computado somando mais 1 ao valor anterior e tendo um mesmo comportamento de um iterador qualquer 
dentro de um ForLoop.
Essa técnica é chamada de avaliação preguiçosa (em inglês, lazy evaluation), que é o processo de adiar a avaliação de uma expressão até que ela seja necessária, 
e muito utilizada para criar sequências grandes ou infinitas sem estourar a memória da máquina. 
'''

