import random

"""
Task 1

The Guessing Game.
Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. 
The result should be sent back to the user via a print statement.

"""

if __name__ == '__main__':

    min = 1
    max = 10
    number_attempts = 4
    i_number_attempts = number_attempts
    i = 0

    def ending(n):
        if n in range(5, 20) or n % 10 in range(5, 10) or n == 0:
            return(" попыток ")
        elif n % 10 == 1:
            return(" попытка ")
        elif n % 10 in range(2, 5):
            return(" попытки ")


    computer_numb = random.randrange(min, max)


    humen_numb = input("Какое число от " + str(min) + " до " + str(max) + " я загадаал?"  "\nУ тебя "
                       + str(number_attempts) + str(ending(number_attempts)) + "\nПоехали:")


    while i < number_attempts:

        if humen_numb.isalpha():
            humen_numb=input("Попробуй написать числом:")



        elif int(humen_numb) == computer_numb:
            print("Ты угадал, это " + str(computer_numb))
            break

        elif i == (number_attempts-1):
            print("Ты не смог угадать, это было число " + str(computer_numb))
            break

        elif int(humen_numb) > computer_numb:

            i_number_attempts -= 1
            print("Неверно, у тебя осталось " + str(i_number_attempts) + str(ending(number_attempts)))
            humen_numb = input("Попробуй число поменльше:")
            i += 1

        elif int(humen_numb) < computer_numb:

            i_number_attempts -= 1
            print("Неверно, у тебя осталось " + str(i_number_attempts) + str(ending(number_attempts)))
            humen_numb = input("Попробуй число побольше:")
            i += 1





