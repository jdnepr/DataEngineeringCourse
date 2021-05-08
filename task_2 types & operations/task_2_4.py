words = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for w in words:
    last_word = len(w.split(' ')) - 1
    name = w.split(' ')[last_word]
    print("Привет, %s%s" % (name[0].upper(), name[1:].lower()))

# print(f"Привет, {name[0].upper(), name[1:].lower()}!")
# returns: Привет, ('И', 'горь')!