def thesaurus(*args):

    dictionary = {}
    for name in args:
        name_surname = name.split()
        my_key = name_surname[1][0]
        if my_key in dictionary:
            dictionary[my_key].append(name)
        else:
            dictionary[my_key] = [name]

    for value in dictionary.values():
        print(value)

    return dictionary


my_dict = thesaurus("Мария Шимановская", "Иван Соколов", "Игорь Сеченов", "Петр Чайковский", "Илья Бешевли")
print(my_dict)

for key in sorted(my_dict.keys()):
    print(f'{key} : {my_dict[key]}')
