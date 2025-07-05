print(sorted([20, 1, 5, 19, 6]))  
# [1, 5, 6, 19, 20]
print(sorted(['programacao', 'funcional', 'e', 'legal'])) 
# ['e', 'funcional', 'legal', 'programacao']

'''
Suponha que você queira ordenar a lista de palavras pelo tamanho delas, ao invés de ser pela ordem alfabética. 
Como você faria isso? A função sorted tem um argumento chamado key. O argumento key recebe uma função que indica o critério pelo qual devemos ordenar. 
Se dissermos que o critério é o tamanho da palavra, então ele ordenará do menor tamanho ao maior tamanho. 
'''
print(sorted(['programacao', 'funcional', 'e', 'legal'], key=lambda x: len(x))) 
# ['e', 'legal', 'funcional', 'programacao']