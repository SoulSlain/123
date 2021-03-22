while True:
    color = input'Выберите свет:'.lower() # SyntaxError - скобки input()
    if color = 'quit':                    # SyntaxError - присваивание вместо сравнения
        print('Выход из цикла')
    break                                 # Не соблюден правильный отступ, дальнейший код Unreachable
    else                                  # SyntaxError - пропущено двоеточие     
        if color == 'красный':
            print('Ждем')
        elif color == 'желтый':
            print('Готовимся')
        elif a == 'желтый':               # Обращение к несуществующей переменной 
            print('Готовимся')
        elif color == 'зеленый':
            print('Двигаемся')
        else:
            print('Странный светофор')