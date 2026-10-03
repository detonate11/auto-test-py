import unittest
import sys

# Добавляем букву 'r' перед строкой, чтобы слэши в путях Windows читались корректно
sys.path.append(r'C:\перенос\21092020\обучение\ТУСУР\Автоматизированное тестирование\testPython')

from app.triangle import TriangleCalculator

class MyCalculator_test(unittest.TestCase):

    def test_triangle1(self):
        self.calculator = TriangleCalculator(1, 1, 1)
        # Округляем до 2 знаков, так как площадь правильного треугольника 0.43301...
        self.expected = self.calculator.get_area
        self.assertEqual(self.expected, 0.43)

    def test_triangle2(self):
        self.calculator = TriangleCalculator(3, 4, 5)
        self.expected = self.calculator.get_area
        self.assertEqual(self.expected, 6.0)

# Этот блок ОБЯЗАТЕЛЬНО должен быть без отступов на самом левом краю
if __name__ == '__main__':
    unittest.main()
