# figure: Ventana donde vamos a graficar (seria como el canva??)
# output_file: nombre del archivo donde se va a generar el putput de la grafica. (html)
# show: Crear un servidor para mostrar le archivo generado con en el output_file
from bokeh.plotting import figure, output_file, show

def run():
  output_file('graficado.jpg')
  fig = figure()
  print(type(fig))

  total_values = int(input('Cauntos valores quieres graficar? '))
  x_values = list(range(total_values))
  y_values = []

  for x in x_values:
    value = int(input(f'Valor de y en {x} => '))
    y_values.append(value)

  fig.line(x_values, y_values, line_width=2)
  show(fig)

if __name__ == "__main__":
  run()