import random

def busqueda_lineal(lista, objetivo):
  match = False
  counter = 0
  for elemento in lista: # O(n)
    counter += 1
    if elemento == objetivo:
      match = True
      break
  
  print(f'Pasos: {counter}')
  return match

if __name__ == '__main__':
  tamano = int(input('Tamaño de la lista: '))
  objetivo = int(input('Número a buscar en la lista: '))

  lista = [random.randint(0, 100) for i in range(tamano)]
  encontrado = busqueda_lineal(lista, objetivo)

  print(lista)
  print(f'El número {objetivo} {"esta" if encontrado else "no esta"} en la lista')