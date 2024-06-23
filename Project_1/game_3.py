def game_core_v3(number: int = 1) -> int:
    """Guess the number less then 20 attempts

    Args:
        number (int, optional): Random number. Defaults to 1.

    Returns:
        int: Number of attempts
    """
   
    
    count = 0 # создаем счетчик количества попыток
    number = np.random.randint(1, 101)
    
    min = 0  # задаем минимум"
    max = 101 # задаем максимум"
    while True:
        predict = round((min+max)/2)  # применяем бинарный поиск"
        
        count += 1 # увеличиваем счетчик
        if number == predict: # если угадал число
            break   # останавливаем цикл
        elif number > predict: # если число больше загадываемого
            min = predict
            print(f"Загаданное число больше {predict}") # печатаем, что число больше
        elif number < predict: # если меньше
            max = predict
            print(f"Загаданное число меньше {predict}") # печатам, что меньше
    return count # возвращаем количество попыток