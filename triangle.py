def area(a, h):
    '''
    Возвращает площадь треугольника с основанием a и высоторой, проведённой к основанию h

        Принимает:
            a (int): длина основания
            h (int): высота, проведённая к основанию

        Возвращаемое значение:
            area (int): площадь треугольника
    '''
    return a * h / 2 

def perimeter(a, b, c): 
    '''
    Возвращает периметр треугольника со сторонами a, b, c

        Принимает:
            a (int): длина первой стороны
            b (int): длина второй стороны
            c (int): длина третьей стороны

        Возвращаемое значение:
            perimeter (int): периметр треугольника
    '''
    return a + b + c
