words = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for w in words:
    last_word = len(w.split(' ')) - 1
    name = w.split(' ')[last_word]
    print(f"Привет, {name[0].upper() + name[1:].lower()}!")

# Вопрос:
# почему, если я напишу через .join(), а не через "+":
# print(f"Привет, {name[0].upper().join(name[1:].lower())}!")
# результат будет, например: "Привет, эАлАиАтАа!" ?
#


