import Adivinhacao
import Forca

print("*********************************")
print("********Escolha seu jogo!********")
print("*********************************")

print("(1) Adivinhacao (2) Forca")

jogo = int(input("Qual jogo?: "))

if(jogo == 1):
    print("Jogando Adivinhacao")
    Adivinhacao.jogar()
elif(jogo == 2):
    print("Jogando Forca")
    Forca.jogar()