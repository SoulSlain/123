while True:
    N = input("Введите факториал, который нужно посчитать: ")
    try:
        N = int(N)                                                        # конвертируем строку в integer
    except ValueError:                                                    # и если это не получилось
        print("Неправильный ввод: невозможно конвертировать в число")                           
        continue                                                          # пытаемся ввести снова рестартом петли
    if N > 0:                                                             # при правильном вводе
        break                                                             # выходим из петли
    else:                                                            
        print("Неправильный ввод: отрицательное число")                   # входим в петлю из-за отрицательного значения
    
#ans = 1
#for i in range(1,N+1,1):
#    ans = ans*i
#print(ans)

def factorial(N):
    res = 1
    for i in range(1, N + 1):
        res *= i
    return res

print(factorial(N))
