''' 7. Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.'''

def count_n(clone_list):
    dikt = {}
    for key in clone_list:
        dikt.update({key: clone_list.count(key)})
    print(dikt)

website_list = ['google.com','includehelp.com', 'linkedin.com', 'pornhub.org',1, 3, 3, 1, 1, 1, 1, (1, "a", 2),1, 3, 3, 1, 1, 1, 1, (1, "a", 2),1, 3, 3, 1, 1, 1, 1, (1, "a", 2),1, 3, 3, 1, 1, 1, 1, (1, "a", 2),1, 3, 3, 1, 1, 1, 1, (1, "a", 2),'google.com','includehelp.com', 'linkedin.com', 'google.com','google.com','includehelp.com', 'linkedin.com', 'google.com','google.com','includehelp.com', 'linkedin.com', 'google.com']
count_n(website_list)
