import itertools

print(list(itertools.permutations([1,1])))
print(list(itertools.permutations([1,2])))
# criamos uma permutação com dois elementos, como o valor de r não foi passado explicitamente, então, por padrão, o método considera o tamanho da lista, ou seja, r = 2. 

print(list(itertools.permutations([1,2,3])))
# Na linha 7, ele considera o r = 3, devido à lista possuir 3 elementos. 

print(list(itertools.permutations([1,2,3], r=2)))
# o valor de r foi como passado por parâmetro, criando permutações com dois elementos. Isso prova que esse método é bastante flexível podendo ser usado em diversos problemas que envolvem combinações ordenadas. 

'''
Uma situação bem comum que vale ser citada aqui é a organização de uma casa. Por exemplo, lavar louças, limpar o quarto, limpar o banheiro, lavar e estender roupas, dentre muitas outras atividades. 
Então, para otimizar seu tempo, você pode determinar a melhor ordem de fazer essas atividades.
Sabendo disso, você precisa testar as possíveis combinações de atividades para saber qual a ordem que você consegue fazer no menor tempo, certo?
'''