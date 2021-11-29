'''3. Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000, и яка вертатиме True, якщо це число просте, и False - якщо ні.'''


def is_prime(number):
    temp = True
    for num_checked in range(1, number):
        if num_checked in [1, number]:
            continue
        if number % num_checked == 0:
            temp = False
            break
        else:
            temp = True
    return temp

a = is_prime(int(input('enter n = ')))
print(a)

#auto_test    
#for i in range (1000+1):
#    print(f'{i} = {is_prime(i)}')

