class Bullet:
  def __init__(self, x, y, img_file):
      self.score = 0
      self.sqr.x = x
      self.sqr.y = y


  def move_right(self):
     self.sqr.x += 1

  def move_left(self):
      self.sqr.x -=1