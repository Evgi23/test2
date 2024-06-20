import numpy as np
number = np.random.randint(1,1091)

count = 0
while True:
    count +=1
    predict_number = int(input("Уагадай число"))
    
    if predict_number > number:
        print("Число должно быть меньше")
    
    elif predict_number < number:
        print("Число должно быть больше")
    
    else:
        print(f"Вы угадали число! Это число = {number} за {count} попыток")
        break