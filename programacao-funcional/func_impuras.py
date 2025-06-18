# Exemplos de funções impuras 

a = 2
def soma(b): # b = 1
    b = b + a # b = 3
    return b
print(soma(1))

'''
Essa função:
- Não depende somente dos valores de entrada
- A variável a, na primeira linha de código, está fora do escopo da função
- O valor de a pode mudar durante a execução do programa
'''

# Transformando a função soma em uma função pura

def soma_pura(c, b):
    b = b + c
    return b
print(soma_pura(2, 1))

# Método impuro

class A:
    atributo = 0

    def mudar_valor(self, x):
        self.atributo = x

objeto = A()
objeto.mudar_valor(5)
print(objeto.atributo)

'''
Esse método é impuro porque modifica uma variável que não pertence ao escopo da função (atributo)
A execução dessa função com o mesmo parâmetro irá sempre repetir o mesmo comportamento, 
mas ainda assim não é uma função pura.
'''