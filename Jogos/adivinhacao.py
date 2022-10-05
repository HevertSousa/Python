print("*************************************************************************")
print("*********************     JOGO DA ADIVINHAÇÃO     ***********************")
print("*************************************************************************")

numero_secreto = 42
rodada = 1

nivel = int(input("Escolha a dificuldade do jogo \n NÍVEL FÁCIL 1 \n NÍVEL MÉDIO 2 \n NÍVEL DIFÍCIL 3 \n"))

if(nivel == 1):
        tentativas = 20
elif(nivel == 2):
        tentativas = 10
elif(nivel == 3):
        tentativas = 5
        
chances = tentativas

while(tentativas > 0):
    print("Rodada {} Tentativa {} de {}".format(rodada,tentativas,chances))
    chute = int(input("Digite seu número: "))
    print('Você digitou: ', chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou")
        break
    elif(maior):
        print("Você errou! O seu chute foi maior que o número secreto")
    elif(menor):
        print("Você errou! O seu chute foi menor que o número secreto")
    tentativas = tentativas-1
    rodada = rodada+1
    if(tentativas == 0):
        print("\n PERDEU TODAS AS CHANCES")
