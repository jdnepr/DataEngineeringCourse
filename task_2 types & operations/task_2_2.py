list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# add '0' to all number less than 10, without +
for i in range(len(list)):
    if list[i].isnumeric():
        if not int(list[i])//10:
            list[i] = "0" + list[i]

print(list)

for i in range(len(list)):
    for j in list[i]:
        numeric_part = ''
        not_numeric_part = ''
        if j.isnumeric():
            numeric_part += j
        else:
            not_numeric_part += j

    list[i] = not_numeric_part + "0" + numeric_part

print(list)