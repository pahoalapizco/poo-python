
def insertion_sort(lista):
  n = len(lista)  
  # El rango empieza en 1 porque esa es la posición desde la que 
  # de donde vamos a tomar el primer valor para compararlo con el valor 
  # anterior de la lista (posición 0).
  # >>>> No tomamos de incio la posición en 0 porque no habia con que comparar dicho valor   con uno previo 
  for idx in range(1, n):
    valor_actual = lista[idx]
    posicion_actual = idx
    print(f'lista[{posicion_actual}] = {valor_actual}')

    # posicion_actual > 0: valida que no salgamos de la posición 1 
    # lista[posicion_actual] > lista[posicion_actual - 1]: Valor actual > Valor anterior
    while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
      # Si el elemento de la posición actual es mayor al anterior, al actual se le asigna el antrior.
      lista[posicion_actual] = lista[posicion_actual - 1]
      # Se disminiye hasta llegar a 0 (donde el valor actual es el mas pequeñ)
      # O hasta la posicion donde el valor predecesor es menor al que contiene la posición en el numero que quedó.
      posicion_actual -= 1 
      print(f'posicion_actual = {posicion_actual}, lista = {lista}')

    # El valor obtenido al inicio en el for, se asigna en la posición donde 
    # es mas alto que la posicion anterior pero mas chico que la posición siguiente.
    lista[posicion_actual] = valor_actual
    print(lista)
  return lista

if __name__ == '__main__':
  lista = [7, 3, 1, 2, 4, 6]
  print('Unsorted: ', lista)
  
  new_list = insertion_sort(lista)
  print('Sorted: ', new_list)
