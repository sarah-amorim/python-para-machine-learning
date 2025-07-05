'''
Analise as aplicações de map com um seguinte exemplo. Você trabalha para a Netflix e quer analisar quantos filmes ruins, médios e bons há no catálogo. 
Porém, o seu chefe te deu somente uma média da avaliação dos usuários. Você pode começar a modelar o seu problema. 
Para isso, é importante definir a função que classifica um filme.
'''

def categoria(nota):
    if nota < 5.0:
        return 'ruim'
    elif 5.0 <= nota <= 7.0:
        return 'médio'
    else:
        return 'bom'

'''
Bom, agora é necessário aplicar a função que foi criada à lista de dados chamada notas que o seu chefe lhe deu. 
Lembre-se de que, para aplicar a função categoria, definida anteriormente, a toda lista de uma vez, é preciso usar a função map. 
Além disso, para ter o resultado como lista, deve ser chamado o método list.
'''

notas = [9.87, 3.15, 7.53, 6.17, 0.53, 9.55, 7.7, 1.88, 7.9, 6.01]
classificacao = list(map(categoria, notas))
print(classificacao)
# ['bom', 'ruim', 'bom', 'médio', 'ruim', 'bom', 'bom', 'ruim', 'bom', 'médio']

'''
Muito bem! Você já tem a classificação dos filmes de acordo com as notas. Agora, que tal dividir esse resultado em grupos? Nesse caso, 
é necessário criar três grupos. Desse modo, você conseguirá contar o tamanho de cada grupo.
Para isso, você poderia utilizar a função filtrar. Só que já existe uma função para isso no Python: função filter.
Ela se comporta exatamente como essa função apresentada anteriormente.
'''

# A função filter recebe dois argumentos, o primeiro é a função que você quer utilizar como critério de filtragem e a segunda é o conjunto de dados. 
# Ela também retorna um iterador, portanto precisamos utilizar o método list para obter uma lista como retorno.

filmes_ruins = list(filter(lambda x: x == 'ruim', classificacao))
filmes_medios = list(filter(lambda x: x == 'médio', classificacao))
filmes_bons = list(filter(lambda x: x == 'bom', classificacao))

# Agora, para saber o tamanho de cada grupo, é só chamar a função len

print(len(filmes_ruins), len(filmes_medios), len(filmes_bons))  
# 3 2 5

'''
A lista de filmes passadas pelo seu chefe tem 3 filmes ruins, 2 filmes médios e 5 filmes bons! 
Você pode dar a boa notícia de que há mais filmes bons no seu catálogo do que ruins! Agora, e se ele lhe passar uma nova lista de filmes e 
perguntar a você: “existe algum filme ruim no meio? Todas as notas são boas?”
'''
#  Primeiro, utilize-a para comparar a nota de cada filme com a avaliação ‘ruim’. Para fazer essa comparação, basta usar uma expressão lambda. 
novas_categorias = ['bom', 'bom', 'bom', 'ruim', 'bom']
filmes_ruins_booleano = list(map(lambda x: x == 'ruim', novas_categorias))
print(filmes_ruins_booleano)  # [False, False, False, True, False]

print(any(filmes_ruins_booleano))  # True

# De maneira parecida, você deve utilizar a função map para comparar se as classificações são iguais a ‘bom’.
filmes_bons_booleano = list(map(lambda x: x == 'bom', novas_categorias))
print(filmes_bons_booleano)  # [True, True, True, False, True]

print(all(filmes_bons_booleano))  # False