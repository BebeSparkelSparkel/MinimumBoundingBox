import numpy
from random import random
from itertools import tee

from jackedCodeTimerPY import JackedTiming
JTimer = JackedTiming()

for num_pts in range(10, 10000, 100):
  JTimer.start('setup')
  hull = tuple((random(), random()) for pc in range(num_pts))
  unit_vector_p = random(), random()
  JTimer.stop('setup')

  JTimer.start('tuple')
  dis_p = tuple(numpy.dot(unit_vector_p, pt) for pt in hull)
  min_p = min(dis_p)
  len_p_tuple = max(dis_p) - min_p
  JTimer.stop('tuple')

  JTimer.start('list')
  dis_p = list(numpy.dot(unit_vector_p, pt) for pt in hull)
  min_p = min(dis_p)
  len_p_list = max(dis_p) - min_p
  JTimer.stop('list')

  JTimer.start('iterator')
  len_p_iterator = max(numpy.dot(unit_vector_p, pt) for pt in hull) - min(numpy.dot(unit_vector_p, pt) for pt in hull)
  JTimer.stop('iterator')

  JTimer.start('tee')
  min_itr, max_iter = tee(numpy.dot(unit_vector_p, pt) for pt in hull)
  len_p_tee = max(max_iter) - min(min_itr)
  JTimer.stop('tee')

  print(num_pts)

print()
print()
print(JTimer.report())
