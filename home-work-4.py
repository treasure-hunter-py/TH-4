'''4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона, і вертатиме список простих чисел всередині цього діапазона.'''

def prime_list(start_pul, finish_pul):

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
    myListEyeNum = []
    for i in range (start_pul,finish_pul+1):
        if is_prime(i) == True:
            myListEyeNum.append(i)
    print(myListEyeNum)


start = int(input('enter start position '))
finish = int(input('enter start position '))
prime_list(start, finish)
