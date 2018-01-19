import random

#MENU DE CÓDIGO DAS CORES:
def cores_disponiveis():
  print("                             CÓDIGOS DAS CORES\n")
  print("1    =  VERMELHO      2    =  AZUL      3    =  AMARELO      4    =  ROXO      ")
  print("5    =  MARROM        6    =  ROSA      7    =  LARANJA      8    =  VINHO      ")

#FUNÇÃO PARA SORTEAR AS CORES DA ESFINGE
def cores_esfinge():
    if mestre_escolha > mestre_escolha[:0]:
        del mestre_escolha[:]
    for i in range(4):
        mestre_escolha.append(random.choice(list(cores.keys())))


#FUNÇÃO DE JOGADA E COMPARAÇÃO COM ESCOLHA DO MESTRE:
def nova_jogada():
    if vetor_jogada > vetor_jogada[:0]:                                            #A CADA RODADA O VETOR É ZERADO, PARA COMPARÁ-LO NA SEGUNDA RODADA E ASSIM POR DIANTE
        del vetor_jogada[:]
    for j in range(0, 4):
        jogada = int(input("Escolha o CÓD da cor na posição Nr {}: ".format(j+1)))
        vetor_jogada.append(jogada)                                                #A JOGADA É ARMAZENADA NO VETOR USADO PARA COMPARAÇÃO Á ESCOLHA DO MESTRE
        escolhas.append(vetor_jogada)
        acerto = 0                                                                 #AQUI SOMA-SE A QUANTIDADE DE ACERTO DE CORES
        acerto_posicao = 0                                                         #AQUI SOMA-SE A QUANTIDADE DE ACERTO DE CORES E POSIÇÕES
    for k in range(4):
          if vetor_jogada[k] != mestre_escolha[k] and vetor_jogada[k] in mestre_escolha:#COMPARA-SE AS ESCOLHAS ARMAZENADAS NO VETOR COM A ESCOLHA DA ESFINGE
                 acerto = acerto + 1
          elif vetor_jogada[k] == mestre_escolha[k]:                               #COMPARA-SE AS POSIÇÕES DO VETOR QUE ARMAZEM AS ESCOLHAS E A ESCOLHA DA ESFINGE
                 acerto_posicao = acerto_posicao + 1
    print(" ")
    print("FEEDBACK: {} Bolas pretas!".format(acerto_posicao))                     #CORES EM POSIÇÕES CORRETAS
    print("FEEDBACK: {} Bolas brancas!\n".format(acerto))                          #CORES CORRESTA EM POSIÇÕES DIVERGENTES
   # if vetor_jogada == mestre_escolha:  # CASO O VIAJANTE CONSIGA ACERTAR AS 4 CORES E POSIÇÕES
   #     print("\nVOCÊ ACERTOU AS CORES CARO VIAJANTE! AUTORIZO SUA PASSAGEM EM SEGURANÇA BOA VIAGEM!\n")
   #     continuar_jogo()


#AO FINAL DAS 10 RODADAS O JOGO PERGUNTA SE QUER REINICIAR OU CONTINUAR
def continuar_jogo():
    while True:
        continuar = int(input("Você deseja jogar novamente? 1 = Sim , 2 = Não: "))
        if continuar == 1:
            print("\nNOVO JOGO INICIANDO...\n")
            cores_esfinge()
            if vetor_jogada > vetor_jogada[:0]:
               del vetor_jogada[:]
            for g in range(1,11):
                  if vetor_jogada > vetor_jogada[:0]:
                    print("AS CORES ESCOLHIDAS NA RODADA PASSADA FORAM: ")
                  for x in vetor_jogada:
                        print(x, " - ", cores[x])
                  cores_disponiveis()
                  print("\n\n>>> Jogada N° {}/10\n".format(g))
                  nova_jogada()
                  print("---------------------------------------------------------------------------------------\n")
        elif continuar == 2:
            print("\n        "
                  "                      >>> VOCÊ SAIU DO JOGO! <<<          ")
            break
        else:
            print("Valor inválido, digite 1 = Sim, 2 = Não: ")

print("-----------------------------------------------------------------------------------------")
print("                       Bem vindo ao jogo Enigma da esfinge!")
print("-----------------------------------------------------------------------------------------\n\n")

print("Você agora é um viajante que está prestes a enfrentar a grande Esfinge! ")
print("Você terá dez tentativas para conseguir acertar 4 cores de 8 disponíveis, que \na grande esfinge irá escolher.")
print("Caso acerte as cores, a esfinge autorizará sua passagem.")
print("Caso contrário...ganhará uma viagem só de ida para o céu!")
print("Ao final de cada rodada você receberá um feedback de quantas cores e posições acertou.")
print("Esse feedback será representado por bolas brancas e pretas.")
print("A cada cor correta em posição diferente da escolhida pela esfinge, você receberá uma bola branca.")
print("A cada cor e posição igual as cores sorteadas pela esfinge, você receberá uma bola preta.\n\n\n")

iniciar_jogo = input("                    --- Aperte enter para iniciar o jogo ---")
print("\n\n\n")



#VETORES QUE ARMAZENAM OS DADOS
vetor_jogada = []                 #ARMAZENA CADA JOGADA SEPARADA POR RODADA
escolhas = []                     #ARMAZENA TODAS AS JOGADAS FEITAS NAS 10 RODADAS
mestre_escolha = []               #ARMAZENA A ESCOLHA DAS 4 CORES DA ESFINGE



#LISTA DE CORES DISPONÍVES PARA O JOGO
cores = {1:"VERMELHO",2:"AZUL",3:"AMARELO",4:"ROXO",5:"MARROM",6:"ROSA",7:"LARANJA",8:"VINHO"}


#CHAMAR A FUNÇÃO QUE SORTEIA AS CORES DA ESFINGE
cores_esfinge()

#MOSTRAR AS CORES DA ESFINGE
#for x in mestre_escolha:
#    print(cores[x])
#print(mestre_escolha)

#10 RODADAS PARA TENTAR DESCOBRIR A COR
for i in range(1,11):
    if vetor_jogada > vetor_jogada[:0]:
        print("AS CORES ESCOLHIDAS NA RODADA PASSADA FORAM: \n")
    for x in vetor_jogada:
        print(x,"-",cores[x])
    cores_disponiveis()
    print("\n\n>>> Jogada N° {}/10\n".format(i))
    nova_jogada()
    if vetor_jogada == mestre_escolha:  # CASO O VIAJANTE CONSIGA ACERTAR AS 4 CORES E POSIÇÕES
        print("\nVOCÊ ACERTOU AS CORES CARO VIAJANTE! AUTORIZO SUA PASSAGEM EM SEGURANÇA BOA VIAGEM!\n")
        break
    print("---------------------------------------------------------------------------------------\n")
    if i == 10 and vetor_jogada != mestre_escolha:
        print("\nVocê não acertou as cores, você perdeu o jogo!\nA esfinge não autoriza sua passagem!")
        print("As cores escolhidas pelo mestre foram: {}, {}, {}, {}".format(cores[mestre_escolha[0]],cores[mestre_escolha[1]],cores[mestre_escolha[2]],cores[mestre_escolha[3]],"\n"))
continuar_jogo()



    
