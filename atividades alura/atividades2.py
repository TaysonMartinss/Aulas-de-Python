import os
numero = int(input('Digite um numero: '))

if numero %2 == 0:
    print('Este numero é par! ')
else:
    print('Este numero é impar! ')


idade = int(input('Digite sua idade: '))

if 0 <= idade <= 12:
    print('Voce é criança! ')
elif 13 <= idade <= 18:
    print('Voce é adolescente! ')
else:
    print('Voce é adulto!')


ipt_user = input('digite seu nome de usuario: ')
ipt_pass = input('digite sua senha: ')

senha = 'ben10'
usuario = 'vinicius jr'



if ipt_user != usuario and ipt_pass != senha:
    os.system('cls')
    print('usuario negado, deletando terminal....')
else:
    os.system('cls')
    print("""
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝
""")
    

    coordenadas_x = float(input('digite as coordenadas x: '))
    coordenadas_y = float(input('\ndigite as coordenadas y: '))

    if coordenadas_x >= 0 and coordenadas_y >=0:
        print('Voce esta no PRIMEIRO QUADRANTE!')
    elif coordenadas_x <0 and coordenadas_y >0:
        print('Voce esta no PRIMEIRO QUADRANTE!')
    elif coordenadas_x < 0 and coordenadas_y <0:
        print('Voce esta no TERCEIRO QUADRANTE')
    elif coordenadas_x >0 and coordenadas_y <0:
        print('Voce esta no QUARTO QUADRANTE: ')
    else:
        print('VOCE ESTA LOCALIZADO NO EIXO OU NA ORIGEM')