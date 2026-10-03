import sys
sys.path.append('C:\перенос\21092020\обучение\ТУСУР\Автоматизированное тестирование\testPython')
from app.triangle import TriangleCalculator

def test_triangle1():
    calculator = TriangleCalculator(1,1,1)
    expected = calculator.get_area()
    assert expected == 0.43