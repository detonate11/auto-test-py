#Импорт класса
from triangle import TriangleCalculator

#Тест на классификацию треугольников

print('Начинаем тестирование типов треугольников')
print('1.Тест на равносторонний треугольник: ')
Test1 = TriangleCalculator(50,50,50)
print('2.Тест на равнобедренный треугольник: ')
Test2 = TriangleCalculator(50,50,60)
print('3.Тест на разносторонний треугольник: ')
Test3 = TriangleCalculator(30,40,50)

# Тест на площадь

print('Начинаем тестирование площади треугольников')
print('1.Тест на площадь - 6: ')
Test4 = TriangleCalculator(3,4,5)

# Тест на периметр
print('Начинаем тестирование периметра треугольников')
print('1.Тест на периметр - 12: ')
Test5 = TriangleCalculator(3,4,5)

# Тест на граничные случаи
print('Начинаем тестирование граничных значений ')
print('1.Тест на минимальные значения: ')
Test6 = TriangleCalculator(1,1,1)
print('2.Тест на максимальные значения: ')
Test7 = TriangleCalculator(100,100,100)

# Тест на негативные случаи
print('Начинаем тестирование негативных кейсов ')
print('1.Тест на несуществование: ')
Test8 = TriangleCalculator(1,2,4)
print('2.Тест на вырожденность: ')
Test9 = TriangleCalculator(1,2,4)
print('3.Тест на нулевые значения: ')
Test10 = TriangleCalculator(0,0,0)
print('4.Тест на отрицательные значения: ')
Test11 = TriangleCalculator(-1,2,3)
print('5.Тест на строчные значения: ')
Test11 = TriangleCalculator('one',2,3)
