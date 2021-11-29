'''8. Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку. Тобто, функція приймає два аргументи: список і величину зсуву (якщо ця величина додатня - пересуваємо з кінця на початок, якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
   Наприклад:
       fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
       fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]
Свернуть'''
def fnc(list_1, shift = 1):
    if shift > 0:
        for pul in range(abs(shift)):
            temp = list_1[len(list_1)-1::]
            temp_list = list_1[:len(list_1)-1:]
            list_1 = temp + temp_list
        print(list_1)
    else:
        for pul in range(abs(shift)):
            temp_list = list_1[1::]
            temp = list_1[:1:]
            list_1 = temp_list + temp
        print(list_1)
a = int(input('enter pull change '))
fnc([1, 2, 3, 4, 5], shift= a)
