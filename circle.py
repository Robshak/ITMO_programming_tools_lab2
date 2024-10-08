import math


def area(r):
    '''
    Возвращает площадь окружности радиуса r

        Принимает:
            r (int): радиус вашей окружности

        Возвращаемое значение:
            area (int): площадь окружности
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр окружности радиуса r

        Принимает:
            r (int): радиус вашей окружности

        Возвращаемое значение:
            perimeter (int): периметр окружности
    '''
    return 2 * math.pi * r
