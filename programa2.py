numero = 42
chute = 0
while(chute != numero):
    chute = input("Digite um número")
    chute = int(chute)
    if chute == numero:
        print("Você Acertou")
    else:
        if(chute > numero):
            print("Você errou! O seu chute foi maior que o número secreto")
        else:
            print("Você errou! O seu chute foi menor que o número secreto")
