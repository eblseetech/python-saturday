ativa = True
while ativa:
    escolhas = '''
    Operações de cálculo permitidas
    [1] - Soma
    [2] - Subtração
    [3] - Multiplicação
    [4] - Divisão
    [5] - Potência
    [0] ou [Sair] - Sair
    '''
    print(escolhas)
    operador = input("Selecione sua opção: ")
    if operador == "0" or operador == "Sair":
        print("Obrigado por usar nossa Calculadora !")
        ativa = False
    elif operador >= "1" and operador < "6":
        n1 = int(input('Entre com o primeiro número: '))
        n2 = int(input('Entre com o segundo número: '))

        match operador:
            case "1":
                print(f'\nSomando os valores, temos: {n1+n2}')
            case "2":
                if n1 >= n2:
                    print(f'\nSubtraindo os valores, temos: {n1-n2}')
                else:
                    print(f'\nSubtraindo os valores, temos: {n2-n1}')
            case "3":
                print(f'\nMultiplicando os valores, temos: {n1*n2}')
            case "4":
                if n2 == 0:
                    print(f'\nNão é possível dividir por zero')
                else:
                    if n1 >= n2:
                        print(f'\nDividindo os valores, temos: {n1/n2}')
                    else:
                        print(f'\nDividindo os valores, temos: {n2/n1}')
            case "5":
                print(f'\nEfetuando a exponenciação entre os valores, temos: {n1**n2}')
            case _:
                print('Erro na operação')
    else:
        print('Erro na Operação')
