import math

while True:
    choice = input('Выберите опцию:').lower() # lower() преобразует весь input в прописные буквы
    if choice == 'quit':
        print('Выход из цикла')
        break
    else:    
        if choice == 'простые числа':
            print("Введите n")
            n = int(input())

            if n < 2:
                print("Число должно быть больше 1")
                quit()
            elif n == 2:
                print("Это простое число")
                quit()

            i = 2
            limit = int(math.sqrt(n))

            while i <= limit:
                if n % i == 0:
                    print("Это сложное число")
                    quit()
                i += 1
                
            print("Это простое число")
        elif choice == 'общий делитель':
            print("Введите два числа:")
            a = int(input("a = "))
            b = int(input("b = "))

            while a != 0 and b != 0:
                if a > b:
                    a %= b
                else:
                    b %= a

            print("НОД a и b:", a + b)
        elif choice == 'общее кратное':
            print ('НОК a и b')
            print("Введите два числа:")
            a = int(input ("a = "))
            b = int(input ("b = "))

            p = a * b

            while a != 0 and b != 0:
                if a > b:
                    a = a % b
                else:
                    b = b % a

            nod = a + b
            nok = p // nod
            print("НОК a и b:", nok)
        else:
            print('Введите правильный выбор')