def limparTela():
    import os
    os.system('cls')

def criaBanco():
    try:
        leBanco()
    except:
        arquivo = open('banco.txt', 'w')
        arquivo.close()
    
def leBanco():
    arquivo = open('banco.txt', 'r')
    dados = arquivo.read()
    arquivo.close()
    return dados

def escreveBanco(dados):
    arquivo = open('banco.txt', 'w')
    arquivo.write(dados)
    arquivo.close()

def adicionaBanco(dados):
    arquivo = open('banco.txt', 'a')
    arquivo.write(dados)
    arquivo.close
    

def insereDados(dados,desafiante,competidor, palavra,partida):
    partida = str(partida)
    dados = dados + partida + "\n" + "Desafiante: " + desafiante + "\n" + "Competidor: " + competidor + "\n" + "Palavra:" + palavra + "\n"
    return dados

def imprimirOculta(palavra):
    for i in range(len(palavra)):
        i = (i + 1) * '_'  
    return i

def venceu( palavra,listacertas):
    venceu= True
    for letra in palavra: 
        if letra not in listacertas: 
            venceu = False 
            break 
    return venceu 

def palpite(listacertas,listaerradas):
    while True:

        palpite = input('Dê seu palpite: ').upper() 
        
        if len(palpite) != 1: 
            print('Só é válido uma letra por vez')
        elif palpite in listacertas or palpite in listaerradas: 
            print('Essa letra já foi digitada. Tente novamente')
        elif not 'A' <= palpite <= 'Z': 
            print('Apenas uma letra é aceita.')

        else:
            return palpite  

def delay(tempo):
    import time
    time.sleep(tempo)





    
                
    
           

      
