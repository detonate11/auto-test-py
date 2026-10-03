
class TriangleCalculator:
    def __init__(self,a,b,c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
#проверка на длину
        if self.a < 1 or self.a > 100:
            print('Длина A выходит за диапазоны 1..100')
            return
        else:
            print('Длина - ОК')

        if self.b < 1 or self.b > 100:
            print('Длина B выходит за диапазоны 1..100')
            return
        else:
            print('Длина - ОК')

        if self.c < 1 or self.c > 100:
            print('Длина C выходит за диапазоны 1..100')
            return
        else:
            print('Длина - ОК')

        #проверка  треугольника на существование
        if (self.a + self.b)< self.c or (self.a + self.c)<self.b or (self.b + self.c)<self.a :
            print('Треугольника не существует')
            return
        elif (self.a + self.b)== self.c or (self.a + self.c)==self.c or (self.b + self.c)==self.a :
            print('Треугольник вырожденный')
            return
        else:
            print('Треугольник существует! Ура!')

        #проверка типа треугольника
        if self.a == self.b == self.c:
            self.get_type = 'равносторонний'
            print('Треугольник равносторонний')
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            self.get_type = 'равнобедренный'
            print('Треугольник равнобедренный')
        else:
            self.get_type = 'разносторонний'
            print('Треугольник разносторонний') 

        #Проверяем площадь
        s=(self.a + self.b + self.c)/2
        S=(s*(s-self.a)*(s-self.b)*(s - self.c))**0.5
        self.get_area = round(S, 2)
        print('Площадь треугольника:', self.get_area)
        S1 = f"{S:.2f}"


        print('Площадь треугольника:')
        print(S1)

        #Проверяем длину
        self.get_perimeter = self.a + self.b + self.c
        print('Длина треугольника: ')
        print(self.get_perimeter)