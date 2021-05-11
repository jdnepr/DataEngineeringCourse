def thesaurus(*args):
    print(f'args:{args}')
    dictionary = {}
    for name in args:
        my_key = name[0]
        if my_key in dictionary:
            dictionary[my_key].append(name)
        else:
            dictionary[my_key] = [name]

    return dictionary


my_dict = thesaurus("Мария", "Иван", "Петр", "Илья")
print(my_dict)

for key in sorted(my_dict.keys()):
    print(f'{key} : {my_dict[key]}')

