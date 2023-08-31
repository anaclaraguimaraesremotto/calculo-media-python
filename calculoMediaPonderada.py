def calcular_media_ponderada(valores, pesos):
    soma_pesos = sum(pesos)
    soma_produtos = sum([valor * peso for valor, peso in zip(valores, pesos)])

    return soma_produtos / soma_pesos

valores = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
pesos = [113, 88, 58, 65, 71, 46, 36, 33, 37, 40, 24, 21, 20, 15, 20]

media_ponderada = calcular_media_ponderada(valores, pesos)

print("Média Ponderada:", media_ponderada)