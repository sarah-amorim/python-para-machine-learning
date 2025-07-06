import itertools

print(list(itertools.product([1,2], repeat=2))) # [(1, 1), (1, 2), (2, 1), (2, 2)]

print(list(itertools.product([1,2], [1,2]))) # [(1, 1), (1, 2), (2, 1), (2, 2)]

print(list(itertools.product(['Python'], ['Academy', 'Rocks']))) # [('Python', 'Academy'), ('Python', 'Rocks')]

print(list(itertools.product([1, 2], [3, 4], [5, 6]))) # [(1, 3, 5), (1, 3, 6), (1, 4, 5), (1, 4, 6), (2, 3, 5), (2, 3, 6), (2, 4, 5), (2, 4, 6)]

'''
Na linha 3, utilizamos o argumento opcional repeat para especificar quantas vezes vamos repetir a lista de entrada, 
como utilizamos repeat = 2, a chamada desse método ficou equivalente à chamada do método na linha 5. 

Na linha 7, é possível observar o produto cartesiano de duas listas de tamanhos diferentes.

Na linha 9, fizemos o produto cartesiano a partir de 3 listas, perceba que o tamanho do iterável final é igual ao 
produto do tamanho de cada elemento: 2 x 2 x 2 = 8.


Criar um algoritmo para saber qual é a combinação mais bonita é um problema bem difícil para a máquina entender, pois beleza é um conceito subjetivo. 
Contudo, a máquina pode lhe auxiliar a criar todos os pares possíveis de blusa e calça diferentes, onde, a partir disso, será possível você testar todos 
os pares de roupas imagináveis e informar de qual gostou mais. Como exemplo, considere a situação em que você tem várias blusas e calças de cores diferentes 
e precisa decidir qual a melhor combinação.

Você tem duas listas, uma só com os possíveis primeiros nomes e outra só com os possíveis sobrenomes (sem deixar o sobrenome vir antes do nome). 
Qual seria o melhor método a se utilizar para criar todos os pares de nomes?
R: Product
'''

