
class Automovil:

  def __init__(self, modelo, marca, color):
    self.modelo = modelo
    self.marca = marca
    self.color = color
    self._motor = Motor(4)
    self._estado = 'reposo'

  def agregar_gasolina(self, cantidad):
    self._motor.reabastecer_gasolina(cantidad)

  def acelear(self, tipo='lento'):
    if tipo == 'brusco':
      self._motor.inyectar_gasolina(10)
    else:
      self._motor.inyectar_gasolina(3)


class Motor:
  
  def __init__(self, cilindro, tipo='gasolina', nivel_gasolina = 10):
    self.cilintro = cilindro
    self.tipo = tipo
    self.temperatura = 0
    self._nivel_maximo_gas = 50
    self.nivel_gasolina = nivel_gasolina # Listros

  def inyectar_gasolina(self, cantidad):
    self.nivel_gasolina -= cantidad

  def reabastecer_gasolina(self, cantidad):
    if self.nivel_gasolina == self._nivel_maximo_gas:
      pass
    elif self.nivel_gasolina+cantidad > self._nivel_maximo_gas:
      self.nivel_gasolina = self._nivel_maximo_gas - self.nivel_gasolina
    else:
      self.nivel_gasolina += cantidad 