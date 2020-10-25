eng_rus = {
    'red': 'красный',
    'apple': 'яблоко',
    'car': 'автомобиль',
    'game': 'игра',
    'cat': 'кошка',
    'dog': 'собака'
}

word = input('Введите слово на английском: ')

if word in eng_rus:
    print(eng_rus[word])
else:
    print('Такого слова нет в словаре')
