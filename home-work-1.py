''' 1 1. Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата, і вертатиме 3 значення (кортеж): периметр квадрата, площа квадрата та його діагональ. '''

def square(edge_rectangle):
    import math
    character_rectangle=(edge_rectangle*4, edge_rectangle*2, math.sqrt(2)*edge_rectangle)
    return character_rectangle

print(square(float(input('enter edge rectangle '))))
