import unittest

from MinimumBoundingBox import MinimumBoundingBox, BoundingBox

from math import pi


class TestMinimumBoundingBox(unittest.TestCase):
  def test_MinimumBoundingBox(self):
    bb = MinimumBoundingBox(((0,0),(3,0),(1,1)))
    self.assertAlmostEqual(bb.area, 3)
    self.assertEqual(bb.length_parallel, 3)
    self.assertEqual(bb.length_orthogonal, 1)
    self.assertEqual(bb.rectangle_center, (1.5,.5))
    self.assertEqual(bb.unit_vector, (1,0))
    self.assertEqual(bb.unit_vector_angle, 0)
    self.assertEqual(bb.corner_points, {(0,-1.1102230246251565e-16),(3,0),(3,1),(0,1)})

    bb = MinimumBoundingBox(((0,0),(0,2),(-1,0),(-.9, 1)))
    self.assertAlmostEqual(bb.area, 2)
    self.assertEqual(bb.length_parallel, 1)
    self.assertEqual(bb.length_orthogonal, 2)
    self.assertEqual(bb.rectangle_center, (-0.49999999999999994, 1))
    self.assertEqual(bb.unit_vector, (1,0))
    self.assertEqual(bb.unit_vector_angle, 0)
    self.assertEqual(bb.corner_points, {(1.6653345369377348e-16,0),(1.6653345369377348e-16,2),(-1,2),(-1,0)})



if __name__ == '__main__': unittest.main()
