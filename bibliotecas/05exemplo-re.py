'''
considere a lista de dados pessoais a seguir:

    Laura Maria da Silva
    (46) 93201-6392
    (89) 42010-7411
    (61) 47405-4895
    Rua José Geraldo
    lauramaria@hotmail.com
    Le@d Dell Technologies
  
Como você faria para extrair os números de telefone com os seus respectivos DDDs, 
a partir da string apresentada? Bom, primeiro você deve tentar buscar somente o DDD de cada número. 
'''
import re 

palavra = r"Laura Maria da Silva\n(46) 93201-6392\n(89) 42010-7411\n(61) 47405-4895\nRua José Geraldo\nlauramaria@hotmail.com\nLe@d Dell Technologies"

print(re.search(r'[0-9][0-9]', palavra)) # Primeira correspondência  

print(re.findall(r'[0-9][0-9]', palavra)) # Lista de todas as correspondências

print(re.findall(r'\W[0-9][0-9]\W', palavra))
# utilizamos o ‘\W’, que é um símbolo que significa um caractere não verbal, que corresponderá aos parênteses que ficam em volta do DDD. 
# Dessa forma, conseguimos buscar todos os DDDs da personagem do exemplo.

# Resolvendo com quantificadores
print(re.findall(r'\W[0-9]{2}\W', palavra)) # utilizamos o quantificador {2} para explicitar que queremos somente duas correspondências dessa expressão, ou seja, dois dígitos. Não havendo a necessidade de repetir símbolos

print(re.findall(r'\W\d{2}\W', palavra)) # O caractere especial \d é equivalente ao caractere especial [0-9], como o quantificador {2}.

# Buscando números telefônicos
print(re.findall(r'\d{5}\W\d{4}', palavra))
# A expressão ‘\d{5}’ significa que queremos um número qualquer de 5 dígitos
# Para corresponder ao traço ‘-’, utilizamos o símbolo ‘\W’

print(re.findall(r'\W\d{2}\W\s\d{5}\W\d{4}', palavra))
# Após definidas as duas expressões, basta uni-las em uma só. Para isso, utilizamos o símbolo ‘\s’, que representa um espaço.

# No axemplo abaixo, um dos números não tem DDD
palavra = r"Laura Maria da Silva\n(46) 93201-6392\n42010-7411\n(61) 47405-4895\nRua José Geraldo\nlauramaria@hotmail.com\nLe@d Dell Technologies"

print(re.findall(r'\W\d{2}\W\s\d{5}\W\d{4}|\d{5}\W\d{4}', dados)) 
# Para isso, é necessário combinar as duas expressões para buscar os dois formatos de números telefônicos. Assim, basta unir as duas expressões utilizando o operador ou ‘|’