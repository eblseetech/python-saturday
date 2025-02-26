#Até aqui, exercício

nomeAluno = str(input("Digite o nome do aluno :"))
nota01 = float(input("Qual a nota do primeiro bimestre : "))
nota02 = float(input("Qual a nota do segundo bimestre : "))
nota03 = float(input("Qual a nota do terceiro bimestre : "))
nota04 = float(input("Qual a nota do quarto bimestre : "))
mediaAluno = (nota01 + nota02 + nota03 + nota04) / 4


#Aqui, explicação

freqAluno = int(input("Digite a frequência, em porcentagem, do aluno, de 0 a 100 :"))
tipoEscola = int(input("Tipo do Colegio: \n [1]Publico \n [2]Particular \n"))
print(f"O Aluno {nomeAluno} obteve média {round(mediaAluno,2)}")
if tipoEscola == 1:
    if mediaAluno >=5 or freqAluno >=70:
        print("O aluno está aprovado")
    else:
        print("O aluno está reprovado")
elif tipoEscola == 2:
    if mediaAluno >=6 and freqAluno >=75:
        print("O aluno está aprovado")
    else:
        print("O aluno está reprovado")
else:
    print("Tipo de escola inválido, não é possível atribuir a situação final")

#sites
#colab.research.google.com - python online
#kaggle.com - comunidade online python
#https://egua.dev/ - linguagem de programação em português
#mit app inventor - appinventor.mit.edu


