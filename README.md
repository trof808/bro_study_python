# Обучение языку python
## Команды

```bash
    # Запуск программы
    python имя_файла.py
```

## Что изучили

### Переменные
Переменные - это ячейки, которые хранят значения в программе, которые можно использовать в любом месте
Когда мы создаем переменную, она записывается в память компьютера

Имя переменной придумывает программист самостоятельно.
Значения мы сохраняем в переменную с помощью знака =

Пример создания переменной и запись в нее значения:
```python
    name = 'Ivan'
    age = 9
    best_game = 'brawl stars'
```
### Команды ввода - input() и вывода - print() 
Команда, которая выводит сообщение в консоль
```python
    print('Я люблю питон')
```

Команда, которая задает вопрос и ждет ответ от пользователя
```python
    input('Как тебя зовут?')
```

### Условия
Условия. Делают проверку условий, и могут выполнять код если условие правда или ложь
Также можно делать вложенные условия
```python
    age = 9
    if (age > 18):
        print('Вы взрослый')
    else:
        print('Вы еще школьник')
```

### Использование библиотек
Библиотеки помогают использовать код, который написали другие программисты

Например, в этой программе мы используем библиотеку turtle, которая умеет рисовать в окне

```python
    import turtle

    t = turtle.Pen()

    for x in range(100):
        t.forward(x)
        t.left(90)
```

### Несколько команд библиотеки turtle
```python
    t = turtle.Pen()

    #Рисует красным
    t.pencolor("red")
    #Вперед на 1 пиксель
    t.forward(1)
    #Влево на 90 градусов
    t.left(90)
    #Рисует круг с радиусом 5 или шириной 10
    t.circle(5)
    #Цвет фона
    t.bgcolor("black")
    #Меняет толщину ручки
    t.width(2)
```

### Типы данных
Типы данных
```python
    #Строки
    name = 'Ivan'

    #Числа
    age = 9

    #Логические True - Правда или False - Ложь
    have_car = False
    have_computer = True

    #Списки
    best_games = ['csgo', 'brawl stars', 'minecraft']
    best_games[0] # выведет csgo

    #Кортежи
    family = ('brother', 'mother', 'father')
    family[1] # выведет mother

    #Словари
    english_russian = {
        'apple': 'Яблоко',
        'car': 'Машина'
    }
    english_russian['apple'] # выведет Яблоко
```

### Операторы
Операторы в математике помогают нам делать операции с числами
Вот некоторые из них

```python
a = 2
b = 1

# сложение выведет 3
print(a + b)

# вычетание выведет 1
print(a + b)

# умнодение выведет 2
print(a * b)

# деление выведет 1
print(a / b)

# возведение в степень выведет 4
print(a ** 2)

# сложные выражения выведет 6
print( (a + b) * 2 )
```