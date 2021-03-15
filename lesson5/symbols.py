from collections import Counter

message = input("Введите текст:")
 
res = {i : message.count(i) for i in set(message)}  
print ("Частота использования символов такова:\n "
        +  str(res))