import numpy
from random import random
from itertools import tee
from minimum_bounding_box import minimum_bounding_box

from jackedCodeTimerPY import JackedTiming
JTimer = JackedTiming()



for num_pts in range(10, 10000, 100):
  JTimer.start('setup')
  point_cloud = tuple((random(), random()) for pc in range(num_pts))
  unit_vector_p = random(), random()
  JTimer.stop('setup')

  JTimer.start('minimum_bounding_box')
  minimum_bounding_box(point_cloud)
  JTimer.stop('minimum_bounding_box')

  print(num_pts)

print()
print()
print(JTimer.report())
