'''
As funções anônimas são aquelas que podem ser definidas em Python sem a necessidade de um nome. 
Isso mesmo, ao invés de você declarar def funcao(x), você pode utilizar a palavra-chave lambda.
A maior versatilidade das funções lambda é poder passá-las como argumentos para outras funções
'''

# Função 
def quadratica(x):
    return x*x

# Função lambda
quadrado = lambda x: x*x
quadrado(7)

'''
- A palavra "lambda” é a palavra chave que indica a criação de uma função de uma linha só;
- Já o “x” é o argumento da função lambda;
- O ":” indica o início do cálculo da função; e
- Por fim, "x*x” é o cálculo da função lambda.
'''

# Você pode passar argumentos de outros tipos para a função. 
# Por exemplo, criar uma função que transforma somente o primeiro caractere de uma palavra em maiúsculo. Conforme o trecho abaixo:
f1 = lambda x: x[0].upper() + x[1:]
print(f1('olá mundo'))

# Relembre, agora, a solução que foi dada ao problema de separar uma lista de idades em diferentes grupos para vacinação. 
# Podemos adaptar o código final para ter menos funções, utilizando a expressão lambda.
idades = [30, 45, 60, 72, 75, 99]
primeiro_grupo = filtrar(idades, lambda x: x >= 75)
segundo_grupo = filtrar(idades, lambda x: 60 <= x <= 74)
terceiro_grupo = filtrar(idades, lambda x: x <= 59)
print(primeiro_grupo)  # [75, 99]
print(segundo_grupo)   # [60, 72]
print(terceiro_grupo)  # [30, 45]
                                        