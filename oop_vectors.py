from math import sqrt

class Vector:
  @staticmethod
  def validate(arg):
    return isinstance(arg, str)

  def init(self, x, y):
    self.x = 0
    self.y = 0
    if self.validate(x) == False and self.validate(y) == False:
      self.x = x
      self.y = y


  def add(self, other):
    return (self.x + other.x, self.y + other.y)

  @staticmethod
  def len(x, y):
    return sqrt(x**2 + y**2)
  

v1 = Vector(1, 2)
v2 = Vector(2, 2)
cord = v1 + v2

print("координаты: ", cord)
print("длина вектора: ", Vector.len(cord[0], cord[1]) )