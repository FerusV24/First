from random import randint

n = randint(1, 20)
g = 0
a = 0
r = None
l = ["нет", "Нет", "не", "Не"]
print("Угадай число от 1 до 20.\nУ тебя 5 попыток.")
while True:
    a += 1
    try:
        g = int(input("Ответ: "))
    except ValueError:
        print("Вводи числа.")
        a -= 1
        continue
    if g == n:
        print("Верно!\nПопыток потрачено: " + str(a))
        print("Спасибо за игру!")
        break
    elif g > n:
        print("Нет, число меньше.\nПопыток: " + str(5 - a))
    elif g < n:
        print("Нет, число больше.\nПопыток: " + str(5 - a))
    if a == 5 and g != n:
        if g > n:
            print("Нет, число меньше.\nПопытки закончились.\nИгра окончена.")
            r = str(input("Ещё раз? "))
        elif g < n:
            print("Нет, число больше.\nПопытки закончились.\nИгра окончена.")
            r = str(input("Ещё раз? "))
    if r == l:
        print("Ладно.")
        break