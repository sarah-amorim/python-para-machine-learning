'''
Por exemplo, você tem o seguinte problema: todo ano acontece a vacinação da gripe H1N1 e, por isso, todas as pessoas deveriam se vacinar. 
Contudo, há uma ordem de prioridade para tomar as vacinas: primeiro, os idosos acima de 75 anos; depois, idosos entre 60 e 74 anos; 
e, por último, as pessoas abaixo de 60 anos. Então, como criar uma função que receba como argumento uma lista de idades e retorne uma lista filtrada 
de acordo com a fase? Bem, já foi definida a função filtrar anteriormente. 

Ao invés de começar a modificar a função filtrar, o primeiro passo é modelar o problema. As fases de vacinação atendem a certos critérios. 
Então, o ideal é criar uma função para cada fase que avalie se uma idade atende ao critério definido anteriormente. 
'''

# Cada função recebe como argumento uma idade e retorna verdadeiro ou falso se aquela idade pertence àquela fase.

def primeira_fase(idade):
    return idade >= 75
def segunda_fase(idade):
    return 60 <= idade <=74
def terceira_fase(idade):
    return idade <= 59

def filtrar(lista, criterio):
    nova_lista = []
    for elemento in lista:
        if criterio(elemento):
            nova_lista.append(elemento)
    return nova_lista

'''
Perceba que o argumento criterio é declarado normalmente como outro parâmetro. 
No entanto, na linha 23 ele é chamado como uma função e se comportará de acordo com a função passada como argumento.
'''

idades = [30, 45, 60, 72, 75, 99]
primeiro_grupo = filtrar(idades, primeira_fase)
segundo_grupo = filtrar(idades, segunda_fase)
terceiro_grupo = filtrar(idades, terceira_fase)

print(primeiro_grupo)
print(segundo_grupo)
print(terceiro_grupo)