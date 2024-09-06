
lista_numeros = [1,2,3,4,5,'string',6,7,8,9,10] #ou
list_numeros_com_range = list(range(11))
###########################################

lista_nomes = ['Neymar jr','Saint-Maximin','Rafael leão']
lista_anos = [2002,2024]


def listar_numeros_lista():
    for lista_numero in lista_numeros:
        print(lista_numero)



def loop_listar_numero_impares():
    impar_auxiliar = 0
    for i in lista_numeros:
        if i %2 !=0:
            impar_auxiliar += i


    print(impar_auxiliar)
        
def loop_listar_numeros_decrescente():
    for lista_numero in lista_numeros[::-1]:
        print(lista_numero)

def loop_lista_numeros_com_calculo():
    numero_usuario = int(input('digite um numero: \n'))

    for lista_numero in lista_numeros:
        calculo = numero_usuario*lista_numero
        print(f'{numero_usuario}*{lista_numero} = {calculo} ')

def loop_lista_numeros_com_validacao_try_except():
    soma = 0
    for lista_numero in lista_numeros:
        try:
            soma+= lista_numero
            print(soma)
        except:
            print('caracter invalido!')

def loop_lista_numeros_calculo_total_validacao_try_except():
    acumulador = 0        
    for lista_numero in lista_numeros:
        try:
            acumulador += lista_numero
            print(f'{acumulador}')
        except:
            print('erro!')


    print(acumulador)