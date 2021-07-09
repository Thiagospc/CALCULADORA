conta = []
print('''
                                            *********************
                                            <____CALCULADORA____>
                
                                                 Versão 1.0
                                            *********************
''')     # apresentação

# contas iniciais para por na lista
num_inicial = float(input('Número :> '))
op_inicial = (input('Operador [+ - x /]  :> '))
num2_inicial = float(input('Número :> '))

# condições de operadores
if op_inicial == '+':
    conta.append(num_inicial+num2_inicial)
elif op_inicial == '-':
    conta.append(num_inicial-num2_inicial)
elif op_inicial == 'x':
    conta.append(num_inicial*num2_inicial)
elif op_inicial == '/':
    conta.append(num_inicial/num2_inicial)
else:
    print('Operador inválido')
  
while True: # while usando para caso o usuário queira adicionar novas contas na calculadora
    soma = sum(conta)
    
    resposta = str(input('Terminar [S ou N] :>')).strip().upper() # para saber se o user continuará ou não
    if resposta == 'S':
        break
    
    op = (input('Operador [+ - x /]  :> '))
    num = float(input('Número :> '))
    
    # condições de operadores
    if op_inicial == '+':
        conta.append(soma+num)
    elif op_inicial == '-':
        conta.append(soma-num)
    elif op_inicial == 'x':
        conta.append(soma*num)
    elif op_inicial == '/':
        conta.append(soma/num)
    else:
        print('Operador inválido')

# resultado        
print(soma)
    
    
    
    

