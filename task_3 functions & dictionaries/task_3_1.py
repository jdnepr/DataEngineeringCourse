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
    if number[0].isupper():
        number = number.lower()
        flag = 1

    result = dict_en_rus.get(number, None)

    if result is not None and flag:
        return result.capitalize()

    return result


my_number = input('Enter english number: ')
num_translate(my_number)
print(my_number, ':', num_translate(my_number))

