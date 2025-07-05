"""
Você foi chamado para trabalhar como novo programador Python para o aplicativo Spotify, analisando as avaliações de músicas pelos usuários. 
O seu chefe está muito entusiasmado com a sua chegada e já pensou em várias perguntas para você responder. Ele coletou diversas avaliações dos gêneros 
musicais Rock e Pop.

Em cada avaliação o usuário pode dar uma nota em quantidade de estrelas para uma música, de 1 a 5. 
Ele quer que você mapeie as avaliações numéricas em categorias: entre 0 e 1 estrelas é uma música ruim, entre 2 e 3 é uma música mediana e entre 
4 e 5 são para as músicas boas. 
O seu papel é dizer para o seu chefe quantas músicas ruins, medianas e boas existem para cada gênero: Rock e Pop.

Além disso, ele quer saber se existe alguma música mediana de Rock e se todas as músicas de Pop são boas. Por fim, quer saber qual gênero musical 
teve uma maior quantidade de músicas boas. Abaixo seguem as notas de cada gênero.

notas_rock = [5, 1, 4, 0, 2, 5, 2, 1, 0, 5, 5, 3, 5, 2, 5, 5, 3, 5, 4, 4]
notas_pop = [3, 2, 5, 1, 2, 1, 4, 1, 5, 0, 4, 2, 1, 2, 5, 2, 4, 4, 0, 1]

Pronto, com essas informações você pode começar a desenvolver um programa em Python capaz de responder as perguntas do seu chefe.
"""

"""
eu tenho uma lista, cada valor dela vai ser atribuido um a uma categoria (ruim, mediana, boa), depois eu tenho que saber a quantidade de notas de cada 
categoria. Existe alguma música de rock com nota mediana? Todas as músicas de Pop são boas? Qual gênero musical tem a maior quantidade de músicas boas?
"""

# Função para mapear as avaliações numéricas em categorias:
def atribui_categorias(notas):
    if (0 <= notas <= 1):
        return 'ruim'
    elif (2 <= notas <= 3):
        return 'mediana'
    elif (4 <= notas <= 5):
        return 'boa'

notas_rock = [5, 1, 4, 0, 2, 5, 2, 1, 0, 5, 5, 3, 5, 2, 5, 5, 3, 5, 4, 4]
notas_pop = [3, 2, 5, 1, 2, 1, 4, 1, 5, 0, 4, 2, 1, 2, 5, 2, 4, 4, 0, 1]

# Variável que armazena uma lista com as categorias atribuídas as suas respectivas notas:
classificacao_rock = list(map(categorias, notas_rock))
classificacao_pop = list(map(categorias, notas_pop))

print(f"Rock:{classificacao_rock}")
print(f"Pop:{classificacao_pop}")

# Quantidade de notas em cada categoria
rock_ruins = list(filter(lambda x: x == 'ruim', classificacao_rock))
rock_medianas = list(filter(lambda x: x == 'mediana', classificacao_rock))
rock_boas = list(filter(lambda x: x == 'boa', classificacao_rock))

print(f"Rock\nRuins: {len(rock_ruins)}\nMedianas: {len(rock_medianas)}\nBoas: {len(rock_boas)}")

pop_ruins = list(filter(lambda x: x == 'ruim', classificacao_pop))
pop_medianas = list(filter(lambda x: x == 'mediana', classificacao_pop))
pop_boas = list(filter(lambda x: x == 'boa', classificacao_pop))

print(f"Pop\nRuins: {len(pop_ruins)}\nMedianas: {len(pop_medianas)}\nBoas: {len(pop_boas)}")

# Existe alguma música mediana de Rock?
