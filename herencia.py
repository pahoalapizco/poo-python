
class Rectangulo():
    
  def __init__(self, base=0, altura=0):
    self.base = base
    self.altura = altura

  def area(self):
    return self.base * self.altura
  

# Cuandrado extiende de Rectanculo
class Cuadrado(Rectangulo):
  def __init__(self, lado):
    super().__init__(lado, lado)


if __name__ == "__main__":
  rectangulo = Rectangulo(3, 4)
  print(rectangulo.area()) # 12

  cuadrado = Cuadrado(5)
  # EL metodo area de la clase Rectangulo se heredó a la clase Cuadrado
  print(cuadrado.area()) # 25