def calcular_moda(lista):
    lista.sort()
    contagem_elementos = [(elemento, lista.count(elemento)) for elemento in set(lista)]
    moda = max(contagem_elementos, key=lambda x: x[1])[0]
    return moda

def calcular_mediana(lista):
    lista.sort()
    tamanho = len(lista)

    if tamanho % 2 == 1:
        mediana = lista[tamanho // 2]
    else: 
        meio_superior = tamanho // 2
        meio_inferior = meio_superior - 1
        mediana = (lista[meio_inferior] + lista[meio_superior]) / 2
    
    return mediana

numeros = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]

moda = calcular_moda(numeros)
mediana = calcular_mediana(numeros)

print("Moda:", moda)
print("Mediana:", mediana)