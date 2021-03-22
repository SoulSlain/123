while True:
    color = input('Dыберите свет').lower() # lower() преобразует весь input в прописные буквы
    if color == 'quit':
        print('Выход из цикла')
        break
    else:    
        if color == 'красный':
            print('Ждем')
        elif color == 'желтый':
            print('Готовимся')
        elif color == 'зеленый':
            print('Двигаемся')
        else:
            print('Странный светофор')