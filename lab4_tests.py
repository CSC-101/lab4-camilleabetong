import data
import lab4
import unittest
import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input1 = [[1,2], [3,4]]
        result = lab4.first_element(input1)
        expected = [1, 3]
        self.assertEqual(expected, result)


    def test_first_element_2(self):
        input1 = [[5, 7], [9, 17]]
        result = lab4.first_element(input1)
        expected = [5, 9]
        self.assertEqual(expected, result)


    # Part 2
    def test_coordinates1(self):
        point = [Point(1, 2),Point(3, 4),Point(5, 6)]
        result = lab4.x_coordinates(point)
        expected = [1,3,5]
        self.assertEqual(expected, result)

    def test_coordinates2(self):
        point = [Point(5, 2),Point(6, 4),Point(7, 6)]
        result = lab4.x_coordinates(point)
        expected = [5,6,7]
        self.assertEqual(expected, result)


    # Part 3
    def test_positive_quadrant1(self):
        points = [Point(1, -2),Point(3, 4),Point(5, 6)]
        result = lab4.are_in_positive_quadrant(points)
        expected = [Point(3,4),Point(5,6)]
        for e, r in zip(expected, result):
            self.assertEqual(e.x, r.x)
            self.assertEqual(e.y, r.y)

    def test_positive_quadrant2(self):
        points = [Point(1, 2),Point(-3, 4),Point(-5, 6)]
        result = lab4.are_in_positive_quadrant(points)
        expected = [Point(1,2)]
        for e, r in zip(expected, result):
            self.assertEqual(e.x, r.x)
            self.assertEqual(e.y, r.y)


    # Part 4
    def test_distance_between_points(self):
        p1 = Point(1, 2)
        p2 = Point(4, 6)
        result = lab4.distance(p1,p2)
        expected = 5.0
        self.assertAlmostEqual(expected,result)

    def test_distance_between_points2(self):
        p1 = Point(3, 3)
        p2 = Point(3, 3)
        result = lab4.distance(p1, p2)
        expected = 0.0
        self.assertAlmostEqual(expected, result)

    # Part 5
    def test_manhattan_distance_between_points(self):
        p1 = Point(1, 2)
        p2 = Point(4, 6)
        result = lab4.manhattan_distance(p1, p2)
        expected = 7
        self.assertAlmostEqual(expected, result)

    def test_manhattan_distance_between_points2(self):
        p1 = Point(4, 4)
        p2 = Point(4, 4)
        result = lab4.manhattan_distance(p1, p2)
        expected = 0
        self.assertAlmostEqual(expected, result)

    # Part 6
    def test_distance_all(self):
        points = [Point(1, 1), Point(3, 4), Point(-2, -2)]
        expected = [math.sqrt(2), 5.0, 2.8284271247461903]
        actual = lab4.distance_all(points)
        self.assertAlmostEqual(actual, expected)

    def test_distance_all2(self):
        points = [Point(0, 0), Point(1, -1), Point(-1, 1), Point(-3, -4)]
        expected = [0.0, math.sqrt(2), math.sqrt(2), 5.0]
        actual = lab4.distance_all(points)
        self.assertAlmostEqual(actual, expected)



if __name__ == '__main__':
    unittest.main()
