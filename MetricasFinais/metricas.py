from ClassificacaodeZonaseProtocolodeTravamento import classificacaoZonas
from EntradadeDadoseAjusteTermico import ajusteTermico

def media_pressao(soma, cont):
    print("=============Metricas finais============")
    if cont == 0:
        print("Nenhuma leitura registrada")
    else:
        resultado = soma / cont
        print("Media de pressao: ", resultado) 
    
def menor_pressao(valor):
    print("Menor pressao registrada: ", valor)

def porcentagem_zonaverde(cont, quantidade_verde):
    if cont == 0:
        print("Nenhuma leitura registrada")
    else:
        resultado = (quantidade_verde / cont)*100
        print("A porcetagem de Zona Verde: ", resultado)
    print("========================================")

def porcentagem_travamento(quant_leituras, cont):
    print("===============Travamento===============")
    if cont == 0:
        print("Nehuma leitura registrada")
    else:
        resultado = (cont / quant_leituras)*100
        print("Porcentagem de leituras realizadas: ", resultado)
    print("========================================")
