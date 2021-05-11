def num_translate(number):
    dict_en_rus = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }

    return dict_en_rus.get(number, None)

my_number = input('Enter english number: ')
print(my_number, ':', num_translate(my_number))

