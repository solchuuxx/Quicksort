def quick_sort(array):
    def _quick_sort(array, low, high):
        # casos en los que la sublista tiene 0 o 1 elementos.
        if low < high:
            pi = partition(array, low, high)
            # posición del pivote.
            _quick_sort(array, low, pi - 1)
            # ordenar elementos a la izquierda
            _quick_sort(array, pi + 1, high)
            # ordenar elementos a la derecha del pivote
    # función que particiona y coloca al pivote en su posición correcta
    def partition(array, low, high):
        pivot = array[high] # elige el ultimo elemento 
        i = low - 1 # elemento mas pequeño
        #recorre todos los elementos menos el pivote 
        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1 #devuelve la posición del pivote 

    # inicia el proceso de ordenamiento Quick Sort, desde el primer hasta el ultimo momento
    _quick_sort(array, 0, len(array) - 1)

# lista de ejemplo
array = [2, 4, 9, 11, 2, 3, 11, 5, 2, 8, 15, 20, 12, 1]
print("Array original:", array)
quick_sort(array) #llama a la función para ordenar el array
print("Array ordenado:", array)

