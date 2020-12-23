import random

if __name__ == '__main__':
    """
    Спросить у пользователя сколько попыток и до скольки максимум пробовать. 
    Сделать генерацию рендомного значения столько то раз. 
    Каждое значение вывести и потом вывести итоговое максимально выпавшее число.
    
    """
    attempts = input("Сколько раз сгенерировать?:")
    max = input("Какое максимальное число?:")

    i = 0
    was_numb = 0

    while i < int(attempts):


        numb = random.randrange(0, int(max))
        print(numb)

        if was_numb < numb:
            was_numb = numb


        i += 1
    else:
        print(was_numb)
