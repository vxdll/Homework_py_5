# Игра против бота с возможностью выигрыша

import random

print("*"*5,"ИГРА В КОНФЕТЫ 2022","*"*5)

# вводим функции на ввод конфет и вывод промежуточного значения
def input_sw(name):
    x = int(input(f"{name} введите количество конфет которое вы возьмете: "))
    while x < 1 or x > 28:
        x = int(input(f"{name} введите количество конфет от 1 до 28: "))
    return x

# Функция на выбор бота
def input_sw_bot():
    x = random.randint(1,28)
    return x

def concl(name, amount, count, value):
    print(f"{name} взял(-а) {amount} конфет, в итоге у него(-неё) {count} конфет. На столе ещё {value} конфет!")

# Исходные значения
f_name = input("Введите имя игрока: ")
count_f = 0
s_name = "Bot"
count_s = 0
val_sw = int(input("Введите количество конфет: "))

# Объявляем флаг на ход
flag = random.randint(0,1)
if flag:
    print(f"Первым ходит {f_name}")
else:
    print(f"Первым ходит {s_name}")

while val_sw > 28:
    if flag:
        amout = input_sw(f_name)
        count_f = count_f + amout
        val_sw = val_sw - amout
        flag = False
        concl(f_name, amout, count_f, val_sw)
    else:
        amout = input_sw_bot()
        count_s = count_s + amout
        val_sw = val_sw - amout
        flag = True
        concl(s_name, amout, count_s, val_sw)

if flag:
    print(f"Выиграл {f_name}")
else:
    print(f"Выиграл {s_name}")