# О проекте в целом
В этом проекте на языке **python** реализованы функции для вычисления периметра и площади разных фигур, а именно: окружности, прямоугольника, квадрата и треугольника.

# Описание работы функций
## 1. Окружность (circle.py)
### Площадь
#### Аргументы
```
r (int) - радиус окружности
```
#### Реализация
```python
def area(r):
    return math.pi * r * r # здесь math - это стандартная библиотека python
```
### Периметр
#### Аргументы
```
r (int) - радиус окружности
```
#### Реализация
```python
def perimeter(r):
    return 2 * math.pi * r # здесь math - это стандартная библиотека python
```

## 2. Прямоугольник (rectangle.py)
### Площадь
#### Аргументы
```
a (int): длина первой стороны
b (int): длина второй стороны
```
#### Реализация
```python
def area(a, b): 
    return a * b 
```
### Периметр
#### Аргументы
```
a (int): длина первой стороны
b (int): длина второй стороны
```
#### Реализация
```python
def perimeter(a, b): 
    return (a + b) * 2
```

## 3. Квадрат (square.py)
### Площадь
#### Аргументы
```
a (int): длина стороны квадрата
```
#### Реализация
```python
def area(a): 
    return a * a
```
### Периметр
#### Аргументы
```
a (int): длина стороны квадрата
```
#### Реализация
```python
def perimeter(a): 
    return a * 4
```

## 4. Треугольник (triangle.py)
### Площадь
#### Аргументы
```
a (int): длина основания
h (int): высота, проведённая к основанию
```
#### Реализация
```python
def area(a, h): 
    return a * h / 2 
```
### Периметр
#### Аргументы
```
a (int): длина первой стороны
b (int): длина второй стороны
c (int): длина третьей стороны
```
#### Реализация
```python
def perimeter(a, b, c): 
	return a + b + c
```

# История коммитов
+ **[8ba9aeb](https://github.com/Robshak/ITMO_programming_tools_lab2/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460)**  - L-03: Circle and square added (2021-01-04)
+ **[d078c8d](https://github.com/Robshak/ITMO_programming_tools_lab2/commit/d078c8d9ee6155f3cb0e577d28d337b791de28e2)**  - L-03: Docs added (2021-01-04)
+ **[8bb897a](https://github.com/Robshak/ITMO_programming_tools_lab2/commit/8bb897a7a0db15f88cbaa0774cd588170493ea15)**  - add rectangle file (2024-09-21)
+ **[37671b9](https://github.com/Robshak/ITMO_programming_tools_lab2/commit/37671b9466d7f6a1d989ef25ee25fe76974fae93)**  - add triangle file and fix perimeter function into rectangle file (2024-09-21)
+ **[3fbf03e](https://github.com/Robshak/ITMO_programming_tools_lab2/commit/3fbf03eb9276c14b0228bda99e858bdb04011d35)**  - add comments to all functions (2024-09-21)
+ **[3e6b0fe](https://github.com/Robshak/ITMO_programming_tools_lab2/commit/3e6b0febb7cfb395261a5913fb6d0d749f07e9dc)**  - add documentation in README (2024-09-22)
+ **[e03a586](https://github.com/Robshak/ITMO_programming_tools_lab2/commit/e03a5865f99dd57257186cb4214e807790c1ac66)**  - delete dividers in README (2024-09-22)
+ **[e25f6f5](https://github.com/Robshak/ITMO_programming_tools_lab2/commit/e25f6f576186b53a550db56355b61d8bcd5489b9)**  - complete documentation (2024-09-22)
