1. Выяснить тип результата выражений:

    15 * 3  
    15 / 3  
    15 // 2  
    15 ** 2  
    <br> 
2. Дан список:  
    ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
Новый список не создавать! Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
3. \* (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place). Эта задача намного серьёзнее, чем может сначала показаться.
4. Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?

    Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду. Можно ли при этом не создавать новый список?
5. Создать список, содержащий цены на товары (10–20 товаров), например:

    [57.8, 46.51, 97, ...]  

Задачи со звёздочкой: 
* Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
* Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
* Создать новый список, содержащий те же цены, но отсортированные по убыванию.
* Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.
