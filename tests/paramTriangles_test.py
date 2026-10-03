import unittest
from parameterized import parameterized
from app.triangle import TriangleCalculator


class ParamTriangleTests(unittest.TestCase):
#площадь
    @parameterized.expand([
        ("equilateral", 1, 1, 1, 0.43),
        ("right", 3, 4, 5, 6.0),
        ("isosceles", 5, 5, 6, 12.0),
    ])
    def test_area(self, name, a, b, c, expected_area):
        triangle = TriangleCalculator(a, b, c)
        self.assertEqual(triangle.get_area, expected_area)
#периметр
    perimeter_data = [
        ("equilateral", 1, 1, 1, 3.0),
        ("right", 3, 4, 5, 12.0),
        ("isosceles", 5, 5, 6, 16.0),
    ]

    @parameterized.expand(perimeter_data)
    def test_perimeter(self, name, a, b, c, expected_perimeter):
        triangle = TriangleCalculator(a, b, c)
        self.assertEqual(triangle.get_perimeter, expected_perimeter)
#тип
    @staticmethod
    def triangle_type_data():
        return [
            ("equilateral", 1, 1, 1, "равносторонний"),
            ("isosceles", 5, 5, 6, "равнобедренный"),
            ("scalene", 3, 4, 5, "разносторонний"),
        ]

    @parameterized.expand(triangle_type_data())
    def test_triangle_type(self, name, a, b, c, expected_type):
        triangle = TriangleCalculator(a, b, c)
        self.assertEqual(triangle.get_type, expected_type)


if __name__ == "__main__":
    unittest.main()
