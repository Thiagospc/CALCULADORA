from banner import ban
from banner import menu
from time import sleep
print(ban)
print(menu)


sleep(1)

while True:
    
    r = int(input('Opção :> '))
    if r == 0:
        break
    
    n1 = float(input('Primeiro valor :> '))
    n2 = float(input('Segundo valor :> '))
    
    def soma():
        print('='*20)
        print(f'Resultado: {n1 + n2}')
    def sub():
        print(f'Resultado: {n1 - n2}')
    def multi():
        print(f'Resultado: {n1 * n2}')
    def div():
        print(f'Resultado: {n1 / n2}')
    def exp():
        print(f'Resultado: {n1 ** n2}')
        
    def escolha():
        if r == 1:
            soma()
        elif r == 2:
            sub()
        elif r == 3:
            multi()
        elif r == 4:
            div()
        elif r == 5:
            exp()
        else:
            print('Opção inválida!')
            
        
    escolha()

print()
print('***********************')
input('Digite ENTER para sair.')

