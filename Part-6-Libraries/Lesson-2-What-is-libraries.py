# Научите Анфису отвечать на вопрос «Анфиса, как дела?» случайным образом.
# Напишите функцию how_are_you(), она должна вернуть случайный элемент из списка answers. Добавьте в список свои варианты ответов: ничего не сломается, а работать станет интереснее.

from random import choice

answers = ['Норм.', 'Лучше всех :)', 'Ну так', 'Отличненько!', 'Ничего, жить буду']


def how_are_you(mood):
    return choice(mood)


print(how_are_you(answers))