import re

palavra = r'otorrinolaringologista 816' # criamos uma variável chamada ‘palavra’ e atribuímos uma string bruta a ela utilizando o prefixo r

# Nas demais linhas, usamos o método search para encontrar uma correspondência do padrão, passada como argumento, na variável ‘palavra’. 
# Ao encontrar a correspondência, o método search retorna um objeto Match, que contém o índice onde o padrão foi encontrado

print(re.search(r'rino', palavra)) # <re.Match object; span=(4, 8), match='rino'>

print(re.search(r'ri', palavra)) # <re.Match object; span=(4, 6), match='ri'>
# utilizamos outra substring como padrão. Neste exemplo, a substring ‘ri’ contém duas vezes na variável 
# ‘palavra’, entretanto, o método search retorna somente o objeto da primeira ocorrência que, nesse caso, estava entre os índices 4 e 6; 

print(re.search(r'rino', palavra)).group(0) # rino
# Ao utilizar o método group(0) do objeto Match retornado é retornada a correspondência encontrada

print(re.search(r'100', palavra)) # None
# o valor retornado é None pois não foi encontrada correspondência na string ‘palavra’. 