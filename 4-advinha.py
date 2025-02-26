from random import randint

print("####---------- VAMOS JOGAR ? ----------####")
min = 0
max = 100

gameOver = False

while gameOver != True:
    chute = 0
    chances = 0
    dificuldade = 0
    while dificuldade < 1 or dificuldade > 3:
        dificuldade = int(input("Selecione:\n [1] - Fácil \n [2] - Normal \n [3] - Dificil \n AGORA : "))
        if dificuldade == 1:
            chances = 15
        elif dificuldade == 2:
            chances = 10
        elif dificuldade == 3:
            chances = 5
        random = randint(min, max)
        while chute != random:
            chute = input(f'chute um número entre {min} e {max} : ')
            
            if chute.isnumeric():
                chute = int(chute)
                chances = chances - 1
                if chances == 0:
                    print("SUAS CHANCES ACABARAM E VOCÊ PERDEU ! HAHAHAHAHAHAHAHAHAHAH !")
                    break
                else:
                    if chute == random:
                        print('WE ARE THE CHAMPIONS !')
                        print('Você venceu, parabéns !')
                        print(f'O numero era {random} e você ainda tinha {chances} chance(s)')
                        print('CLAP, CLAP, CLAP, CLAP, CLAP !')
                        break
                    else:
                        print(f'Errado ! Você só tem mais {chances} chances!')
                        if chute > random:
                            print('Uma dica, meu número é menor')
                        else:
                            print('Uma dica, meu número é maior')                            
    print("####---------- VAMOS JOGAR DE NOVO ? ----------####")
    replay = 0
    while replay < 1 or replay > 2:
        replay = int(input("Digite 1 para continuar, 2 para sair: "))
        if replay == 2:
            print('Nos vemos em breve !')
            gameOver = True



