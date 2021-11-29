''' 6. Вводиться число. Якщо це число додатне, знайти його квадрат, якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.'''

def faNum (num):
    if num > 0 :
        print(num**2)
    elif num < 0:
        print(num + 100)
    else:
        print(num)

faNum(float(input('enter number ')))
