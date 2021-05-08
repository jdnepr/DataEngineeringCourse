list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# add '0' to all number less than 10, without +
#for i in range(len(list)):
#    if list[i].isnumeric():
#        if not int(list[i])//10:
#            list[i] = "0" + list[i]

print(list)

i = 0
while i < len(list):
    numeric_part = ""
    not_numeric_part = ""
    for j in list[i]:
        if j.isnumeric():
            numeric_part += j
        else:
            not_numeric_part += j
    if numeric_part and (not int(numeric_part)//10):
        list[i] = not_numeric_part + "0" + numeric_part

    if numeric_part:
        list.insert(i, '\"')
        list.insert(i + 2, '\"')
        i = i + 2

    i = i + 1 # while loop increment

print(list)
message = ' '.join(list)
print(message)