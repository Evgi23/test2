import numpy as np




def random_predict(number:int=1) -> int:
    """_summary_

    Args:
        number (int, optional): _description_. Defaults to 1.

    Returns:
        int: _description_
    """
    
    count = 0 # количество попыток
    while True:
        count +=1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return(count)
def score_game(random_predict) ->int:
    """_summary_

    Args:
        random_predict (_type_): _description_

    Returns:
        : _description_
    """
    count_lst = []
    np.random_seed(1)
    random_array = np.random.randit(1, 101, size=(1000))
    for number in random_array:
        count_lst.append(random_predict(number))
    score = int(np.mean(count_lst))
    print(f'Выш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


score_game(random_predict)
#print(f'Количество попыток: {random_predict(10)}')


