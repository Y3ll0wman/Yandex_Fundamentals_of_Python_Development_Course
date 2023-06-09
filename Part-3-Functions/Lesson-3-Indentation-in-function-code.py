# Программистка Маша написала функцию, которая печатает имена всех её коллег. Но Маша мучается с расстановкой отступов.
# Помогите ей и поправьте код так, чтобы программа заработала как надо, то есть вывела список всех коллег.

users = ['Степан', 'Анатолий', 'Антон', 'Андрей']


def print_users(users):
    for user in users:
        print(user)


print_users(users)

# Тоня и Стёпа хотят поехать на отдых, но не могут определиться, куда именно: Стёпа настаивает на Карелии, а Тоня — на Сочи. Тоня решила схитрить и написала функцию, которая из всех предложенных вариантов всегда возвращает Сочи. Но форматирование программы сломалось и нужно всё починить.
# Помогите поправить эту функцию, чтобы Тоня и Стёпа смогли поскорее отправиться на заслуженный отдых.

resorts = ['Сочи', 'курорты Краснодарского Края', 'Санкт-Петербург', 'Карелию']


def choose_vacation_place(resorts):
    for resort in resorts:
        if resort == 'Сочи':
            return resort


resort = choose_vacation_place(resorts)
print('Поехали в ' + resort)