"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число

# количество попыток
count = 0
min = 1
max = 100

while True:
    count+=1
    predict_number = int(input("Угадай число от 1 до 100: "))
    
    if predict_number > number:
        max = predict_number - 1
        predict_number = (max + min) // 2
        print("Число должно быть меньше!")

    elif predict_number < number:
        min = predict_number + 1
        predict_number = (max + min) // 2
        print("Число должно быть больше!")
    
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break #конец игры выход из цикла
