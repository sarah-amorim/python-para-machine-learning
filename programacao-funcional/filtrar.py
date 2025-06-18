# Exemplo de função pura

def filtrar(lista, limiar):
    nova_lista = []
    for elemento in lista: 
        if elemento > limiar:
            nova_lista.append(elemento)
    return nova_lista

numeros = [20, 25, 30, 35, 150, 200, 1024]

filtrar(numeros, 40)

'''
Essa função:
- Produz um valor de saída
- Não gera nenhum efeito colateral
- Nenhuma variável externa é modificada ou acessada
- Todo o escopo da função envolve ler parâmetros e retornar um valor
'''

'''
A Programação Funcional é muito útil para trabalhar com grandes conjuntos de dados, pois faz um gerenciamento de memória inteligente. 
Essa é uma tarefa rotineira no contexto de Machine Learning. Logo, é comum usar técnicas da Programação Funcional.
A pureza de uma função garante que o sistema irá ter um comportamento consistente ao longo da aplicação. 
Isto é especialmente importante na Programação Funcional, pois nesse paradigma você deve modelar um problema através do uso de funções.
'''