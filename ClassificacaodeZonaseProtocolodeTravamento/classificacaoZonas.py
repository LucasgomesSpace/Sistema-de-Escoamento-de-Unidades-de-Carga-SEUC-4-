
#Classificação de Estabilidade:
# Zona Verde (Estável): Entre 120 UPCs e 180 UPCs (após o ajuste).
# Zona Amarela (Oscilação): Fora da Zona Verde, mas abaixo de 250 UPCs (após o ajuste).
# Zona Vermelha (Crítica): Qualquer valor acima de 250 UPCs (após o ajuste).

def classificacao(leitura,count_vermelho):
    if leitura >= 120 and leitura <= 180:
        print('Zona Verde')
        zona = 'VERDE'
    elif leitura < 250:
        print('Zona Amarela')
        zona = 'AMARELA'
    else:
        print('Zona Vermelha')
        zona = 'VERMELHA'

    if zona == 'VERMELHA':
        count_vermelho += 1
    else:
        count_vermelho = 0

    if count_vermelho >= 2:
        print('========================================\nALERTA CRÍTICO: Duas leituras consecutivas na Zona Vermelha! ESCOAMENTO INTERROMPIDO POR SEGURANÇA\n========================================')
        
    return zona, count_vermelho

 


