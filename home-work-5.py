'''5. Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.'''

def fibonacci(num_lim):
    list_fi = [0,1,0]
    print (list_fi[0])
    print (list_fi[1])
    while True:
        list_fi[2] = list_fi[0]+list_fi[1]
        list_fi[0] = list_fi[1]
        list_fi[1] = list_fi[2]
        if list_fi[1] >= num_lim:
            break
        print(list_fi[1])
fibonacci(int(input()))'''

''' 6. Вводиться число. Якщо це число додатне, знайти його квадрат, якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.

def faNum (num):
    if num > 0 :
        print(num**2)
    elif num < 0:
        print(num + 100)
    else:
        print(num)

faNum(float(input('enter number ')))
