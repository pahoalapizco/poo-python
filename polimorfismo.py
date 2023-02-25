
class Persona():
  
  def __init__(self, nombre):
    self.nombre = nombre

  def avanza(self):
    print('Ando caminando')


class Ciclista(Persona):

  def __init__(self, nombre):
    super().__init__(nombre)

  # Se aplica el polimorfisco, Avanza se hereda de Persona
  # pero en Ciclisca se le cambia el funcionamiento, (cambia de forma = Polimorfismo)
  def avanza(self):
    print('Ando en mi bicicleta')

if __name__ == "__main__":
  persona = Persona('Emelyn')
  persona.avanza() # Ando caminando

  ciclista = Ciclista('Paola')
  ciclista.avanza() # Ando en mi bicicleta