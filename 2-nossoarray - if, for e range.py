numeros = []
numero = int(input("Digite, de 1 a 3, quantos números seu array terá : "))
if numero >= 1 and numero < 4:
    for i in range(numero):
        componente = int(input(f"Digite o numero {i+1} : "))
        numeros.append(componente)
    print("Os numeros do seu array são :", numeros)
else:
    print("Erro na operação")

    '''sites para estatística
    https://www.brasil.io
    https://servicodados.ibge.gov.br/api/docs/
    sites para programas
    https://www.kaggle.com - ótima comunidade python
    color.adobe.com - paleta de cores RGB
    https://ollama.com - sistemas para carregar modelos de dados em C
    
    '''

