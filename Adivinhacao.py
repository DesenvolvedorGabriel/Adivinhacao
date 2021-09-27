import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000


    print("Qual o nivel de dificuldade?")
    print("(1) Facil (2) Medio (3) Dificil ")

    nivel = int(input("Defina o nivel: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    print(numero_secreto) #Tirar isto depois

    #  variável/em/série/n°inicial, /n°Final, /step, => intervalo entre os elementos
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}" .format(rodada, total_de_tentativas))
        # print(f"Tentativa {rodada} de {total_de_tentativas}") # f-strings ou formatted string literals => novo recurso a partir do python 3.6
        chute_str = input("Digite um valor entre 1 e 100: ")
        print("Voce digitou", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Voce deve digitar um valor entre 1 e 100")
            continue

        acertou = numero_secreto == chute
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

        if (acertou):
            print("Parabens! Voce acertou e fez {} pontos!" .format(pontos))
            break
        else:
            if(maior):
                print("Voce errou! O seu chute foi maior que o numero secreto!")
            if(rodada == total_de_tentativas):
                    print("O numero secreto era {}. Voce fez {} pontos" .format(numero_secreto, pontos))

            elif(menor):
                print("Voce errou! O seu chute foi menor que o numero secreto!")



    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()

# Abaixo:

# random() => função que gera números aleatórios (precisa ser importado --> import random) Obs: random é uma função que está em um módulo separado, por importar
# round() => função que arredonda o número. Exemplo: 18.895629671768187 para 19 (arredonda pelo mais aproximado)
# random.random() => gera números aleatórios de 0.0 a 1.0
# random.randrange(10) => de 0 a 10
# random.randrange(0, 101) => 0 a 100 inclusivo
# seed => é as entradas dadas a cada chamada da função random e cada seed é utilizado como entrada por padrão os milisegundos(hora). Ou seja, cada milisegundos representa uma entrada e por isso acaba gerando números aleatórios. Lembrando que se repetir a entrada, repete o mesmo número a cada chamada da função random ou a cada sorteio
# pseudo-random => o python recebe esse nome pelo motivo de saber gerar número aleatórios de verdade
# Importante! "funções built-in" => As funções built-in podem ser chamadas a qualquer momento, em todos os lugares. Exemplo de funções são type(..), abs(), input(..) ou int.

##############################################

# Abaixo: funções random e round para fins didáticos

#import random

#numero_random = random.random() * 100
#print(numero_random)

#numero_round = round(numero_random)
#print(numero_round)

##############################################