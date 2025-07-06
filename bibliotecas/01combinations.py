import itertools

# Tentamos imprimir as combinações com as letras da palavra “ABC”. Entretanto, o método combinations retorna um objeto iterável, e não uma lista; 
print(itertools.combinations("ABC", 2)) # <itertools.combinations at 0x1916522f130>

print(list(itertools.combinations("ABC",2)))
# Convertemos o objeto retornado em uma lista. Foi impresso como resultado uma lista com combinações 2 a 2 a partir da palavra ‘ABC’, onde não há repetições de combinações e a ordem não importa ('A', 'B') = ('B','A’);

print(list(itertools.combinations("AABC",2)))
# A lista impressa contém uma combinação que aparece duas vezes ('A', 'B'), isso acontece porque a palavra contém dois caracteres ‘A’ e a função considera que esses dois caracteres ‘A’ são diferentes;

print(list(itertools.combinations("ABCD",3)))
# A lista impressa contém combinações 3 a 3 com as letras da palavra ‘ABCD’, onde não há repetições e a ordem não importa. 
# Perceba que esse método é utilizado quando queremos criar combinações onde a ordem não importa.

'''
 imagine que você foi a uma padaria, e que os lanches estavam em promoção pelo preço de R$ 1. Como você só tinha R$ 2, precisou escolher qual deles iria comprar.
 As combinações de itens que podem ser comprados com R$ 2 são, por exemplo, coxinha e pão de queijo, coxinha e folheado, coxinha e pastel, empada e pastel, empada e esfiha etc. 
 Como você pode perceber, a ordem que você vai comprar os itens não importa e por isso esse é um problema que pode ser resolvido com combinações.
'''