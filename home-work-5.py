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
fibonacci(int(input()))


