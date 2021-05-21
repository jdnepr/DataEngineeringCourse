sentence = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
# used while loop, cause otherwise I cannot alter iterator variable - i
while i < len(sentence):
    numeric_part = ""
    not_numeric_part = ""
    for j in sentence[i]: # save numeric and non-numeric parts of an element in separate variables
        if j.isnumeric():
            numeric_part += j
        else:
            not_numeric_part += j
    if numeric_part and (not int(numeric_part)//10): #
        sentence[i] = not_numeric_part + "0" + numeric_part

    if numeric_part:
        sentence.insert(i, '\"')
        sentence.insert(i + 2, '\"')
        i = i + 2

    i = i + 1 # while loop increment
print(sentence)

message = ''
i = 0
while i < len(sentence):
    if sentence[i] == '\"':
        message += f'{sentence[i]}{sentence[i + 1]}{sentence[i + 2]} '
        i += 2
    else:
        message += sentence[i] + ' '
    i += 1

print(message)
