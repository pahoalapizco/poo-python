import time

def factorial(n):
  respuesta = 1

  while n > 1:
    respuesta *= n
    n -= 1
  return respuesta

def factorial_r(n):
  # Caso base:
  if n == 1: return 1

  return n * factorial_r(n - 1)

if __name__ == "__main__":
  n = 900
  # print(sys.getrecursionlimit(n))
  # Medición por cronometro:
  print('Iterativo')
  comienzo = time.time()
  # print('Iterativo:', factorial(n))
  factorial(n)
  final = time.time()
  fac_time = final - comienzo
  print(f'Tiempo total = {fac_time} \n')

  
  print('Recursivo')
  comienzo = time.time()
  factorial_r(n)
  # print('Recursivo:', factorial_r(n))
  final = time.time()
  fac_r_time = final - comienzo
  print(f'Tiempo total = {fac_r_time} \n')

  if fac_r_time > fac_time:
    print(f'El algoritmo recursivo es más costoso en tiempo por {fac_r_time - fac_time} ms')
  else:
    print(f'El algoritmo iterativo es más costoso en tiempo{fac_time - fac_r_time} ms')
