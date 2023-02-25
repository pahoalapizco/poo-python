import random

def busqueda_binaria(lista, comienzo, final, objetivo, pasos):
  print(f'Buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
  if comienzo > final:
    print(f'Pasos: {pasos}')
    return False
  
  # Obtenemos el indice de en medio de la lista
  medio = (comienzo + final) // 2
  
  if lista[medio] == objetivo:
    print(f'Pasos: {pasos}')
    return True
  elif lista[medio] > objetivo:
    return busqueda_binaria(lista, comienzo, medio-1, objetivo, pasos+1)
  else:
    return busqueda_binaria(lista, medio+1, final, objetivo, pasos+1)




if __name__ == '__main__':
  tamano = int(input('Tamaño de la lista: '))
  objetivo = int(input('Número a buscar en la lista: '))

  lista = sorted([random.randint(0, 100) for i in range(tamano)])
  encontrado = busqueda_binaria(lista, 0, len(lista), objetivo, 0)
  # print(encontrado)
  print(lista)
  print(f'El número {objetivo} {"esta" if encontrado else "no esta"} en la lista')