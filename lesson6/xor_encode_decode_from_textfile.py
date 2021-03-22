def str_xor(string,key):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(string,key)])
 
str1 = ""
key = input("Введите начало ключа: ")
arr = ['a','б','в','г','д','a','b','c','d','e']
with open ('text.txt') as f:
    for line in f:
        str1 = str1 + line
    f.close()
 
for i in range(len(str1)):
    if str1[i] == " ":
        continue
    key = key + str(i + 5 * (i%2)) + arr[i%10]
  
print('\n Исходный текст: '+str1+'\n')
print('\n Ключ: '+key)
encoded = str_xor(str1,key)
print('\n Зашифрованный текст: '+encoded+'\n')
decoded = str_xor(encoded,key)
print('\n Дешифрованный текст: '+decoded+'\n')