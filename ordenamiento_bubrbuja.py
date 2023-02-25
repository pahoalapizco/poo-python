from random import randint

def bubble_sort(lista):
  n = len(lista)
  
  # O(n) * O(n - i - 1) = O(n**2 - in - n)
  # Nos quedamos con el peor de los casos.
  # Complejidad = O(n**2)
  for i in range(n): # O(n)
    for j in range((n-i) - 1): # O(n - i - 1)
      print(f'j= {lista[j]}, j+1= {lista[j+1]}')
      if lista[j] > lista[j+1]:
        # aplicando swapping
        lista[j], lista[j+1] = lista[j+1], lista[j]
  
  return lista


if __name__ == '__main__':
  tamano = int(input('Tamaño de la lista: '))
  lista = [randint(0, 100) for i in range(tamano)]
  print('Random \n',lista)

  lista_ordenada = bubble_sort(lista)
  print('Ordenada \n', lista_ordenada)
