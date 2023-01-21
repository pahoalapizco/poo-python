
class Lavadora:
    
    def __init__(self):
      pass
    
    # la función lavar() abstrae el proceso de lavado, mandando llamar
    # a aquellas funciones que realizadn dicho proceso.
    def lavar(self, temperatura='caliente'):
      self._llenar_tanque(temperatura)
      self._agregar_jabon()
      self._lavar()
      self._centrifugar()

    def _llenar_tanque(self, temperatura):
       print(f'Llenando el tanque con agua {temperatura}')
    
    def _agregar_jabon(self):
      print('Agergando jabon...')
    
    def _lavar(self):
      print('Lavando la ropa...')

    def _centrifugar(self):
      print('Centrifugando...')


if __name__ == "__main__":
  lavadora = Lavadora()
  lavadora.lavar('fria')