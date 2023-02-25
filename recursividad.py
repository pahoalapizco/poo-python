# Entendiendo la recursividad

# Factorial
def factorial(n):
  if n == 1:
    return 1
  
  return n * factorial(n-1)

# potencia
def potencia(a, n):
  if n == 0: return 1

  return a * potencia(a, n - 1)



# Morral
def morral(tamano_morral, pesos, valores, n):

  # Caso base:
  if n == 0 or tamano_morral == 0:
    return 0

  if pesos[n - 1] > tamano_morral:
    return morral(tamano_morral, pesos, valores, n - 1)

  return max(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1),
            morral(tamano_morral, pesos, valores, n - 1))
  

if __name__ == '__main__':
  """ valores = [60, 100, 120]
  pesos = [10, 20, 30]
  tamano_morral = 50
  n = len(valores)

  resultado = morral(tamano_morral, pesos, valores, n)
  print(resultado)
  """
  # print(factorial(64))
  print(potencia(2, 2))