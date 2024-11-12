def soma(n1, n2):
    return n1+n2

print('''1. SOMA
2. SUBTRAÇÃO
3. MULTIPLICAÇÃO
4. DIVISÃO''')

opcao = int(input('Informe a opção que deseja: '))

if opcao > 0 and opcao < 5:
    n1 = int(input('Informe um número: '))
    n2 = int(input('Informe outro número: '))

match opcao:
    case 1:
        print(f'{n1} + {n2} = {soma(n1, n2)}')