import math

def calcular_media_aritimetica(lista):
    return sum(lista) / len(lista)

def calcular_media_geometrica(lista):
    produto = 1
    for num in lista:
        produto *= num
    return math.pow(produto, 1/len(lista))

def calcular_media_harmonica(lista):
    inversos = [1/num for num in lista]
    return len(lista) / sum(inversos)

numeros = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]

media_aritimetica = calcular_media_aritimetica(numeros)
media_geometrica = calcular_media_geometrica(numeros)
media_harmonica = calcular_media_harmonica(numeros)

print("Média Aritimética:", media_aritimetica)
print("Média Geométrica:", media_geometrica)
print("Média Harmônica:", media_harmonica)