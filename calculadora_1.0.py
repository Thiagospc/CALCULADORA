#!/usr/bin/env python3
print('==========================================================')
print('***********************CALCULADORA************************')
print('==========================================================')

# painel de apresentação
while True:
    print('''
        1- SOMA
        2- SUBTRAÇÃO
        3- MULTIPLICAÇÃO
        4- DIVISÃO
        5- EXPONENCIAL
        0- SAIR
        ''')
    resposta = int(input(':>  '))
    # CONDIÇÕES
    if resposta == 1:
        num1 = float(input('N1 :>'))
        num2 = float(input('N2 :>'))
        soma = num1 + num2
        print('*************')
        print(f'Soma: {soma}')
        print('*************')

    elif resposta == 2:
        num3 = float(input('N1 :>'))
        num4 = float(input('N2 :>'))
        sub = num3 - num4
        print('*****************')
        print(f'Subtração: {sub}')
        print('*****************')

    elif resposta == 3:
        num5 = float(input('N1 :>'))
        num6 = float(input('N2 :>'))
        mult = num5 * num6
        print('**********************')
        print(f'Multiplicação: {mult}')
        print('**********************')

    elif resposta == 4:
        num7 = float(input('N1 :>'))
        num8 = float(input('N2 :>'))
        div = num7 / num8
        print('***************')
        print(f'Divisão: {div}')
        print('***************')

    elif resposta == 5:
        num = float(input('N1 :>'))
        num_2 = float(input('Expoente :>'))
        exp = num ** num_2
        print('*******************')
        print(f'Exponencial: {exp}')
        print('*******************')

    elif resposta == 0:
        break
    else:
        print('**********************')
        print('Digite um valor válido')
        print('**********************')

