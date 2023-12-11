import copy
import random
# Consider using the modules imported above.


class Hat:

  #Init
  def __init__(self, **kwargs):
    self.colors = kwargs
    self.contents = []

    #Loop to make contents list
    for color in self.colors:
      i = 0
      while self.colors[color] > i:
        self.contents.append(color)
        i = i + 1

  #Draw method
  def draw(self, times):
    draw_list = []
    i = 0

    if times > len(self.contents):
      draw_list = self.contents
      return draw_list

    while times > i:
      random_choice = random.choice(self.contents)
      self.contents.remove(random_choice)
      draw_list.append(random_choice)
      i = i + 1
    return draw_list


#Function to make the experiments
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  M = 0  #times the experiment was correct
  
  #Loop to make expected list
  expected = []
  for ball in expected_balls:
    x = 0
    while expected_balls[ball] > x:
      expected.append(ball)
      x += 1
  #Loop to make the experiments
  i = 0
  while num_experiments > i:
    original_hat = copy.deepcopy(hat)  #Restablish hat
    draw = original_hat.draw(num_balls_drawn) 
    present = all(draw.count(ball) >= expected.count(ball) for ball in set(expected))
    if present:
      M += 1
    i += 1
  return M / num_experiments
