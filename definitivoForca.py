from funcoes import limparTela,escreveBanco,leBanco,insereDados,imprimirOculta,palpite,venceu,delay,adicionaBanco,criaBanco

inicio = True
partida = '----- Partida(s) Anterior(es) -----'

while inicio:

    imgForca = ['''
    
    +---+
    |   |
        |
        |
        |
        |
    =========''','''
    
    +---+
    |   |
    O   |
        |
        |
        |
    =========''','''
    
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''','''
    
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''','''
    
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''','''
    
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========''','''
    
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========''']

    criaBanco()
    leBanco()

    nomeDesafiante = input("Digite o nome para o desafiante: ").upper()
    nomeCompetidor = input("Digite o nome para o competidor: ").upper()

    limparTela()


    while True:

        palavra = str(input('Digite a palavra a ser descoberta: ')).upper()

        if len(palavra) != 1 and 'A' <= palavra <= 'Z':
            break
        else:
            print('Palavra inválida')

    leBanco()
    dados = insereDados(leBanco(),nomeDesafiante,nomeCompetidor,palavra,partida)
    escreveBanco(dados)

    while True:
        dicaUm = input("Dica n° 1: ")
        if dicaUm != int and len(dicaUm) > 1:
            break
        else:
            print('Forma inválida')
    while True: 
        dicaDois = input("Dica n° 2: ")
        if dicaDois != int and len(dicaDois) > 1:
            break
        else:
            print('Forma inválida')
    while True:
        dicaTres = input("Dica n° 3: ")
        if dicaTres != int and len(dicaTres) > 1:
            break
        else:
            print('Forma inválida')




    letrasErradas = []
    letrasAcertadas = []
    tentativas = len(letrasAcertadas)+ len(letrasErradas)

    dicas = 0
    erros = 0

    jogando = True

    limparTela()

    print(f'A palavra possuí: {len(palavra)} letras\nA palavra é: {imprimirOculta(palavra)}\n')

    while jogando and erros < 6:
        
        #limparTela()

        print(imgForca[(len(letrasErradas))] + '\n')
    
        print('Escolha entre:')
        print('(1) Jogar')
        print('(2) Solicitar Dica')
        
        while True:
            try:
                escolhaCompetidor = int(input("Qual a sua escolha? "))
                if escolhaCompetidor == 1 or escolhaCompetidor == 2:
                    while True :
                        if escolhaCompetidor == 1:
                            break

                        elif escolhaCompetidor == 2 and dicas == 0:  
                            print(f'A dica é: {dicaUm}')
                            dicas += 1
                            break
                                    
                        elif escolhaCompetidor == 2 and dicas == 1:
                            print(f'A dica é: {dicaDois}')
                            dicas += 1
                            break     
                                        
                        elif escolhaCompetidor == 2 and dicas == 2:   
                            print(f'A dica é: {dicaTres}')
                            dicas += 1
                            break     
                                        
                        else:
                            print('Você não possuí mais dicas!')
                            break
                    break
                else:
                    print('Digite 1 - Para jogar e 2 - Para Dica')
            except:
                print('Opção inválida')
                

        palpiteCompetidor = palpite(letrasAcertadas,letrasErradas)
        limparTela()
        delay(2)
                
        tamanhoPalavra = "_" * len(palavra)
        delay(2)
                
        if palpiteCompetidor in palavra:
            letrasAcertadas += palpiteCompetidor
                        
            for i in range(len(palavra)):
                if palavra[i] in letrasAcertadas:
                    tamanhoPalavra = tamanhoPalavra[:i] + palavra[i] + tamanhoPalavra[i+1:]
                    tentativas += 1
            print(f'A palavra possuí a letra: {palpiteCompetidor}')
            print(f'A palavra é {tamanhoPalavra}\nLetras corretas = {letrasAcertadas}. Letras erradas = {letrasErradas}\n') 
            delay(2)
        else:
            print(f'A palavra não possuí a letra {palpiteCompetidor}')
            letrasErradas+= palpiteCompetidor
            erros += 1
            delay(2)


        if venceu(palavra,letrasAcertadas):
            print('Você acertou a palavra, PARABÉNS!')
            jogando = False
            delay(2)

    while True:
        if erros > 5:
            leBanco()
            desafianteGanha = 'Vencedor: ' + nomeDesafiante + '\n' + 'Perdedor: ' + nomeCompetidor + '\n'
            adicionaBanco(desafianteGanha)
            break
        else:
            leBanco()
            competidorGanha = 'Vencedor: '+ nomeCompetidor + '\n' + 'Perdedor: ' + nomeDesafiante + '\n'
            adicionaBanco(competidorGanha)
            break 

    print(leBanco())
    delay(2)
    limparTela()

    print(leBanco())

    while True:
        jogarNovamente = input('Você deseja jogar novamente? (S/n) \n').upper()
        if jogarNovamente == 'S' or jogarNovamente == 'SIM':
            letrasAcertadas = ''
            letrasErradas = ''
            erros = 0
            inicio = True
            break

        elif jogarNovamente == 'N' or jogarNovamente == 'NAO' or jogarNovamente == 'NÃO':
            print('Você optou por não continuar. Até a próxima !')
            inicio  = False  
            break



   
    




                    


        
            
