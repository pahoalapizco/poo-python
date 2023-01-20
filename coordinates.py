
class Coordinates:
    
    def __init__(self, x, y):
      self.x = x
      self.y = y
    
    def distance(self, other_coord):
      x_diff = (self.x - other_coord.x)**2
      y_diff = (self.y - other_coord.y)**2
      dist = (x_diff + y_diff)**0.5

      return dist
    
if __name__ == "__main__":
   coord_p = Coordinates(8, 20)
   coord_q = Coordinates(15, 36)
   distance = coord_p.distance(coord_q)

   print(distance)