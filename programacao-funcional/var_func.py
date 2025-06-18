'''
Você sabia que uma variável também pode receber uma função? Uma função em Python pode ser tratada como qualquer outro objeto. 
Portanto, dizemos que ela é um objeto de primeira classe.
'''

def soma(a, b):
    return a + b
f = soma 
print(f(1, 2))
print(type(f)) # <class 'function'>
