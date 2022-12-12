# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
data = 'AAAAAAAAAAAAbbbbbbbbCCCCCCCCCCdddddddddddddddddddddddd'

def encode(s):
    encoding = ""  # строка для вывода
    i = 0
    while i < len(s):
        # подсчитывает количество вхождений символа в индексе `i`
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
        # добавляет к результату текущий символ и его количество
        encoding += str(count) + s[i]
        i = i + 1
    return encoding

print(encode(data))
z = encode(data)

def decode(s):
    decode = ""
    count = ""
    for char in s:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ""
    return decode

print(decode(z))