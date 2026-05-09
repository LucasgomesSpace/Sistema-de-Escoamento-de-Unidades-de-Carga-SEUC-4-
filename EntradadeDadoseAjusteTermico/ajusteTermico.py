import os
from ClassificacaodeZonaseProtocolodeTravamento import classificacaoZonas
from MetricasFinais import metricas

def leitura():
    os.system("cls")
    print("Seja Bem vindo, ao Sistema de Escoamento de Unidades de Carga (SEUC-4)\n ")
    quant_leituras=int(input('Digite quantas leituras serão feitas no seu turno: '))
    print("\n============= LEITURAS ============")
    
    cont=0
    count_vermelho = 0
    soma = 0
    menor_pressao = 9999
    contagem_verde = 0
    
    while cont<=(quant_leituras-1):
        if cont!=0 and cont%5 == 0 :
            os.system("cls")
            print("\n============= LEITURAS ============")
        leitura=int(input(f'{cont+1}° Leitura da pressão hidrodinâmica do duto: '))
        cont+=1
        if leitura>150:
            leitura=leitura+(leitura*0.08)
        else:
            leitura=leitura-(leitura*0.04)
        zona,count_vermelho = classificacaoZonas.classificacao(leitura,count_vermelho)
        if zona == "VERDE":
            contagem_verde += 1
        soma += leitura
        if menor_pressao > leitura:
            menor_pressao = leitura
        if count_vermelho == 2:
            break
    metricas.media_pressao(soma, cont)
    metricas.menor_pressao(menor_pressao)
    metricas.porcentagem_zonaverde(cont, contagem_verde)
    if count_vermelho == 2:
        metricas.porcentagem_travamento(quant_leituras, cont)