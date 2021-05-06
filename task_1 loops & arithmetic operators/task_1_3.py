def switch_numbers(last_digit):
    last_digit = int(last_digit)
    switcher = {
        0: 'процентов',
        1: 'процент',
        2: 'процента',
        3: 'процента',
        4: 'процента',
    }
    return(switcher.get(last_digit, "процентов"))

user_number = input('Enter your number ')

for i in range(int(user_number) + 1):
    word = switch_numbers(i)
    print(i, word)