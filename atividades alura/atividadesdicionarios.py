lista_pessoas = {'Nome':'Neymar da Silva Santos Jr' , 'Idade':19 , 'Cidade':'São Paulo',
'Nome':'Vinicius jr' , 'Idade':19 , 'Cidade':'Rio de janeiro' }


# Atualização de Idade
lista_pessoas['idade'] = 31

# Adicionando Profissão
lista_pessoas['profissao'] = 'Engenheiro'

# Remoção de Elemento
del lista_pessoas['cidade']


# 3 - Uma possível abordagem para criar um dicionário que apresente os números de 1 a 5 e seus respectivos quadrados é a seguinte:
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)


# 4 - Para verificar a existência de uma chave no dicionário, você pode utilizar a seguinte estrutura:
pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")



# 5 - Para contar a frequência de cada palavra em uma frase, você pode utilizar o seguinte código:
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)