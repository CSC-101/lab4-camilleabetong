import data
import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

# Write your functions for each part in the space below.

# Part 1
def first_element(nested_list):
    filtered_list = [lst for lst in nested_list if lst]
    first_elements = [lst[0] for lst in filtered_list]
    return first_elements
# Part 2

def x_coordinates(points):
    return [point.x for point in points]

# Part 3
def are_in_positive_quadrant(points):
    return [point for point in points if point.x > 0 and point.y > 0]

# Part 4
def distance(point1, point2):
    return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)

# Part 5
def manhattan_distance(point1, point2):
    return abs(point2.x - point1.x) + abs(point2.y - point1.y)

# Part 6
def distance2(point1, point2):
    return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)

def distance_all(points):
    origin = Point(0, 0)
    return [distance(origin, point) for point in points]

