# В теории этого урока приведён код, который находит количество вхождений определённого значения в списке — подсчитывает количество комнат заданной площади; выражение «количество вхождений» означает «сколько раз определённое значение встречается в списке или в любом другом наборе данных».
# Недостаток этого кода в том, что он размещён в теле программы, а не в функции.
# Ваша задача — исправить эту ситуацию: оберните код в функцию.
# Объявите функцию, назовите её rooms_equal()
# Функция rooms_equal() должна принимать на вход два параметра:
# room_size — значение, которое функция будет искать в списке;
# room_list — имя списка, в котором будет проводиться поиск;
# Перенесите в функцию код, который подсчитывает количество помещений заданной площади.
# В коде уже подготовлен вызов функции rooms_equal(), она должна подсчитать, сколько в списке flat помещений площадью 5.55 кв.м.
#  Добавьте ещё один вызов функции: пусть она сосчитает, сколько комнат площадью 9.2 кв.м в списке hut (англ. hut — «хижина»).


def rooms_equal(room_size,room_list):
    count = 0
    for room in room_list:
        if room == room_size:
            count = count + 1
    print('Комнат площадью', room_size, 'кв.м:', count)


flat = [
    5.55, 22.19, 7.78, 26.86, 5.55,
    29.84, 22.19, 5.55, 16.85, 4.52
]
hut = [9.2, 3.5, 8.1, 2.3, 9.2, 4.2, 6.9]
rooms_equal(5.55, flat)
rooms_equal(9.2,hut)

# Допишите функцию number_of_occurrences() так, чтобы она сосчитала, сколько раз в строке string встречается буква, переданная в параметр char.
# Строка — это последовательность, как и список; строку можно точно так же перебрать в цикле по элементам (буквам), найти и пересчитать нужные элементы.
# Предыдущая задача вам поможет: она очень похожа на эту.


def number_of_occurrences(char, string):
    count = 0
    for letter in string:
        if letter == char:
            count += 1

    print('Исходная строка:', string)
    print('Количество вхождений символа', char, 'составляет:', count)


phrase = 'Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили.'

number_of_occurrences('е', phrase)

# Гидрометцентр опубликовал списки средних дневных температур в Москве за май 2017 и 2018 годов.
# Допишите функцию comfort_count(temperatures), она должна подсчитывать дни, когда температура воздуха была от 22 до 26 градусов включительно.
# Функция принимает параметр temperatures: это список, в котором нужно искать тёплые дни.
# В теле функции объявите переменную-счётчик.
# Переберите в цикле for temp in temperatures: элементы списка и найдите значения в диапазоне от 22 до 26.
# В поиске таких значений вам поможет двойное неравенство: «температура больше или равна 22 и, одновременно, меньше или равна 26», то есть между 22 и 26, включительно.
# if temp >= 22 and temp <= 26:
# Это неравенство можно записать покороче:
# if 22 <= temp <= 26:
# Если условие выполняется — увеличивайте значение счётчика на 1.
# В результате работы функция должна вывести на экран строку 'Количество тёплых дней в этом месяце: N', где N — полученное количество дней.


may_2017 = [24, 26, 15, 10, 15, 19, 10, 1, 4, 7, 7, 7, 12, 14, 17, 8, 9, 19, 21, 22, 11, 15, 19, 23, 15, 21, 16, 13, 25,
            17, 19]
may_2018 = [20, 27, 23, 18, 24, 16, 20, 24, 18, 15, 19, 25, 24, 26, 19, 24, 25, 21, 17, 11, 20, 21, 22, 23, 18, 20, 23,
            18, 22, 23, 11]


def comfort_count(temperatures):
    count = 0
    for temp in temperatures:
        if temp >= 22 and temp <= 26:
            count += 1
    print('Количество тёплых дней в этом месяце:', count)


comfort_count(may_2017)
comfort_count(may_2018)