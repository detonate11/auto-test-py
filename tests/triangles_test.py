import unittest
from app.triangle import TriangleCalculator


class PositiveTriangleTests(unittest.TestCase):#позитивные проверки

    def test_minimum_triangle(self):
        triangle = TriangleCalculator(1, 1, 1)
        self.assertEqual(triangle.get_area, 0.43)

    def test_triangle_3_4_5(self):
        triangle = TriangleCalculator(3, 4, 5)
        self.assertEqual(triangle.get_area, 6.0)

    def test_isosceles_triangle(self):
        triangle = TriangleCalculator(5, 5, 6)
        self.assertEqual(triangle.get_area, 12.0)


class NegativeTriangleTests(unittest.TestCase):#негативные проверки

    def test_zero_value(self):
        triangle = TriangleCalculator(0, 2, 3)
        self.assertFalse(hasattr(triangle, 'get_area'))

    def test_value_above_maximum(self):
        triangle = TriangleCalculator(101, 50, 50)
        self.assertFalse(hasattr(triangle, 'get_area'))

    def test_string_value(self):
        with self.assertRaises(ValueError):
            TriangleCalculator('one', 2, 3)

    # Некорректное значение стороны B
    def test_invalid_b(self):
        triangle = TriangleCalculator(2, 0, 2)
        self.assertFalse(hasattr(triangle, 'get_area'))

# Некорректное значение стороны C
    def test_invalid_c(self):
        triangle = TriangleCalculator(2, 2, 101)
        self.assertFalse(hasattr(triangle, 'get_area'))

# Треугольник не существует
    def test_triangle_not_exists(self):
        triangle = TriangleCalculator(1, 2, 10)
        self.assertFalse(hasattr(triangle, 'get_area'))

# Вырожденный треугольник
    def test_degenerate_triangle(self):
        triangle = TriangleCalculator(1, 2, 3)
        self.assertFalse(hasattr(triangle, 'get_area'))



if __name__ == '__main__':
    unittest.main()
