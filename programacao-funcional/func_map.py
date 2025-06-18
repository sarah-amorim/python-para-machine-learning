'''
Uma tarefa clássica na área de Machine Learning é o tratamento de dados. Isso significa limpar dados inválidos, 
arredondar valores numéricos ou aplicar alguma função matemática aos valores iniciais. 

Vamos supor que você tem uma lista de números de ponto flutuante que representam anos. O número de anos deveria ser um número inteiro, 
então não faz sentido trabalhar com um número como 2.5 anos. 

Para converter um número x de ponto flutuante em inteiro, é só utilizar a função int(x). E para aplicar essa função em toda uma lista de uma vez, 
basta utilizar a função map. A função map recebe dois argumentos: uma função e um conjunto de dados. 
Em seguida, ela aplica a função a cada elemento do conjunto de dados individualmente.
'''

anos = [1.5, 2.3, 5.0, 19.4]
anos_inteiros = map(int, anos)
for ano in anos_inteiros:
    print(ano)

'''
A função map retorna um iterador, ou seja, um elemento que representa uma sequência de elementos. 
Para converter o resultado automaticamente para uma lista, podemos usar o método list() no retorno da função. 
'''