# important functions: minimum_bounding_box

from scipy.spatial import ConvexHull
from math import sqrt
import numpy
from math import atan2, cos, sin, pi
from collections import namedtuple


def get_unit_vector(pt0, pt1):
    # returns an unit vector that points in the direction of pt0 to pt1
    dis_0_to_1 = sqrt((pt0[0] - pt1[0])**2 + (pt0[1] - pt1[1])**2)
    # return (pt1[0] - pt0[0]) / dis_0_to_1, \
    #        (pt1[1] - pt0[1]) / dis_0_to_1
    return tuple((pt1[i] - pt0[i]) / dis_0_to_1 for i in range(2))


def orthogonal_vector(vector):
    # from vector returns a orthogonal/perpendicular vector of equal length
    return -1 * vector[1], vector[0]

Rectangle = namedtuple('Rectangle',
    (
        'area',
        'length_parallel',
        'length_orthogonal',
        'rectangle_center',
        'unit_vector',
        'orthogonal_vector',
        'corner_points'
    )
)

def min_length_along_vector(unit_vector, point_cloud):
    '''
    returns the distance between the points along unit_vector
    that have the minimum and maximum displacements along unit_vector
    unit_vector must be of length one like (0, 1)
    '''
    unit_vector = get_unit_vector(*unit_vector)
    displacements = tuple(numpy.dot(unit_vector, pt) for pt in point_cloud)
    return max(displacements) - min(displacements)


def bounding_area(index, hull):
    # unit_vector_p = get_unit_vector(hull[index], hull[index+1])
    # unit_vector_o = orthogonal_vector(unit_vector_p)

    # dis_p = tuple(numpy.dot(unit_vector_p, pt) for pt in hull)
    # dis_o = tuple(numpy.dot(unit_vector_o, pt) for pt in hull)

    # min_p = min(dis_p)
    # min_o = min(dis_o)
    # len_p = max(dis_p) - min_p
    # len_o = max(dis_o) - min_o

    # return {'area': len_p * len_o,
    #         'length_parallel': len_p,
    #         'length_orthogonal': len_o,
    #         'rectangle_center': (min_p + len_p / 2, min_o + len_o / 2),
    #         'unit_vector': unit_vector_p,
    #         }

    # return Rectangle(
    #         area = len_p * len_o,
    #         length_parallel = len_p,
    #         length_orthogonal = len_o,
    #         rectangle_center = (min_p + len_p / 2, min_o + len_o / 2),
    #         unit_vector = unit_vector_p,
    #     )

    # return (max(dis_p) - min_p) * (max(dis_o) - min_o)

    unit_vector = get_unit_vector(hull[index], hull[index+1])
    return min_length_along_vector(unit_vector, hull) * \
           min_length_along_vector(orthogonal_vector(unit_vector), hull)


def to_xy_coordinates(unit_vector_angle, point):
    # returns converted unit vector coordinates in x, y coordinates
    angle_orthogonal = unit_vector_angle + pi / 2
    return point[0] * cos(unit_vector_angle) + point[1] * cos(angle_orthogonal), \
           point[0] * sin(unit_vector_angle) + point[1] * sin(angle_orthogonal)


def rotate_points(center_of_rotation, angle, points):
    # Requires: center_of_rotation to be a 2d vector. ex: (1.56, -23.4)
    #           angle to be in radians
    #           points to be a list or tuple of points. ex: ((1.56, -23.4), (1.56, -23.4))
    # Effects: rotates a point cloud around the center_of_rotation point by angle
    rot_points = []
    ang = []
    for pt in points:
        diff = tuple([pt[d] - center_of_rotation[d] for d in range(2)])
        diff_angle = atan2(diff[1], diff[0]) + angle
        ang.append(diff_angle)
        diff_length = sqrt(sum([d**2 for d in diff]))
        rot_points.append((center_of_rotation[0] + diff_length * cos(diff_angle),
                           center_of_rotation[1] + diff_length * sin(diff_angle)))

    return rot_points


def rectangle_corners(rectangle):
    # Requires: the output of mon_bounding_rectangle
    # Effects: returns the corner locations of the bounding rectangle
    corner_points = []
    for i1 in (.5, -.5):
        for i2 in (i1, -1 * i1):
            corner_points.append((rectangle['rectangle_center'][0] + i1 * rectangle['length_parallel'],
                            rectangle['rectangle_center'][1] + i2 * rectangle['length_orthogonal']))

    return rotate_points(rectangle['rectangle_center'], rectangle['unit_vector_angle'], corner_points)


Rectangle = namedtuple('Rectangle',
    (
        'area',
        'length_parallel',
        'length_orthogonal',
        'rectangle_center',
        'unit_vector',
        'orthogonal_vector',
        'corner_points',
        'unit_vector_angle',
        'rectangle_center'
    )
)



# use this function to find the listed properties of the minimum bounding box of a point cloud
def minimum_bounding_box(points):
    # Requires: points to be a list or tuple of 2D points. ex: ((5, 2), (3, 4), (6, 8))
    #           needs to be more than 2 points
    # Effects:  returns a dictionary that contains:
    #               area: area of the rectangle
    #               length_parallel: length of the side that is parallel to unit_vector
    #               length_orthogonal: length of the side that is orthogonal to unit_vector
    #               rectangle_center: coordinates of the rectangle center
    #                   (use rectangle_corners to get the corner points of the rectangle)
    #               unit_vector: direction of the length_parallel side. RADIANS
    #                   (it's orthogonal vector can be found with the orthogonal_vector function
    #               unit_vector_angle: angle of the unit vector

    assert len(points) > 2
    hull_ordered = [points[index] for index in ConvexHull(points).vertices]
    hull_ordered.append(hull_ordered[0])

    # min_rectangle = bounding_area(0, hull_ordered)
    # for i in range(1, len(hull_ordered)-1):
    #     rectangle = bounding_area(i, hull_ordered)
    #     if rectangle['area'] < min_rectangle['area']:
    #         min_rectangle = rectangle

    # min_rectangle['unit_vector_angle'] = atan2(min_rectangle['unit_vector'][1], min_rectangle['unit_vector'][0])
    # min_rectangle['rectangle_center'] = to_xy_coordinates(min_rectangle['unit_vector_angle'], min_rectangle['rectangle_center'])
    # return min_rectangle

    smallest_side_index = min(range(len(hull_ordered)-1), key=lambda i: bounding_area(i, hull_ordered))

    




