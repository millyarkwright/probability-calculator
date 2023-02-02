import copy
import random

class Hat:
  def __init__(self, **kwargs):

    self.contents = []

    # Add kwarg values (ie ball colours) to contents list
    for key, value in kwargs.items():
      self.contents.extend([key] * value)

  # Draw: Remove balls at random from contents and return those balls as list of strings
  def draw(self, number):
    
    draws = []

    if number > len(self.contents): 
      return self.contents
    else:
      for n in range(number):
        ball = random.choice(self.contents)
        draws.append(ball)
        self.contents.remove(ball)
        
    return draws    
  
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  count_successes = 0 
  expected = []

  # Add expected ball values to expected list
  for key, value in expected_balls.items():
    expected.extend([key] * value)

  # Matches: If the ball in the draw list is also in the exp_ball list, return the ball to the matches list.
  # Check: check if there are enough of each expected ball colour in the matches list. 
  for n in range(num_experiments):
    new_hat = copy.deepcopy(hat)
    draw = new_hat.draw(num_balls_drawn)
    matches = [ball for ball in draw if ball in expected]
    check = all([matches.count(item) >= expected.count(item) for item in expected])
        
    if check:
      count_successes += 1

  
  return count_successes/num_experiments
  
  
  
