from ClassificacaodeZonaseProtocolodeTravamento import classificacaoZonas

def leitura():
    quant_leituras=int(input('Digite quantas leituras vai fazer no seu turno: '))
    
    cont=0
    count_vermelho = 0
    
    
    while cont<=(quant_leituras-1):
        leitura=int(input('Leitura da pressão hidrodinâmica do duto: '))
        cont+=1
        if leitura>150:
            leitura=leitura+(leitura*0.08)
        else:
            leitura=leitura-(leitura*0.04)
        leitura,count_vermelho = classificacaoZonas.classificacao(leitura,count_vermelho)

        if count_vermelho == 2:
            break