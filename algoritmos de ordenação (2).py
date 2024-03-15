import random
import time
import math
from statistics import median, mean, mode, variance

# variavel inicio
inicio = time.time()
# gerar numeros
n = random.sample(range(0,30000), 20000)
print(f'Sequência de números desorganizada:')
print(n)

#byblet sort
def bubble_sort(lista):
    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                ordenado = False        
        
    return lista
print("\n Ordenado por bubble sort:")
print(bubble_sort(n))
fim = time.time()
delta = fim - inicio


# insertion sort
inicio2 = time.time()
def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        key = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > key:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = key
lista = n
insertion_sort(lista)
print("\n Ordenado por insertion sort:")  
print(lista)  
fim2 = time.time()
delta2 = inicio2 - fim2


# mergesort
inicio3 = time.time()
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
fim3 = time.time()
delta3 = fim3 - inicio3

lista = n
merge_sort(lista)

# prints
print("\n Ordenado por mergesort")
print(lista)


list_mean = mean(lista)
list_median = median(lista)
list_mode = mode(lista)
variancia = sum((x - list_mean) ** 2 for x in lista) / len(lista) - 1 
print("\no tempo de execução do bubblesort foi:", delta)
print('o tempo de execução do insertsort foi:', delta2)
print('o tempo de execução do mergesort foi:', delta3)
print("\na média da lista é:", list_mean)
print('a moda da lista é:', list_mode)
print('a mediana da lista é:', list_median)
print('a variancia da lista é', variancia)
desvio_padrao = math.sqrt(variancia)
print('o desvio padrao é é', desvio_padrao)