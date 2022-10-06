#  Copyright (c) Vladimir Modenov.
#  Created: 06.10.2022, 21:16
#  Project: StepikPythonProjects
#  File: NumericalGuessingGame.py

# Numerical guessing game

from random import *


def is_bet_good(bet):
    return len(bet) == 3 and 100 <= bet[0] <= balance and bet[0] <= balance_bot and bet[1] in list_coef and bet[
        2] in list_bet


def quantity_trying(bet):
    if bet[2] == 100:
        if bet[1] == 2:
            return 6
        elif bet[1] == 4:
            return 5
        else:
            return 4
    elif bet[2] == 1000:
        if bet[1] == 2:
            return 9
        elif bet[1] == 4:
            return 8
        else:
            return 7
    else:
        if bet[1] == 2:
            return 13
        elif bet[1] == 4:
            return 12
        else:
            return 11


def game():
    global balance
    global balance_bot

    print('Итак, ситуация такова:')
    print('\nТвой баланс:', balance, 'тёмкинсов')
    print('Мой баланс:', balance_bot, 'тёмкинсов')
    print('Доступные коэффициенты:')
    print('коэф. 2, при ставке на: [1-100 - 6 попыток] [1-1000 - 9 попыток] [1-10000 - 13 попыток]')
    print('коэф. 4, при ставке на: [1-100 - 5 попыток] [1-1000 - 8 попыток] [1-10000 - 12 попыток]')
    print(
        'УНИКАЛЬНАЯ ВОЗМОЖНОСТЬ: коэф. 10, при ставке на: [1-100 - 4 попыток] [1-1000 - 7 попыток] [1-10000 - 11 попыток]')

    print(
        'Чтобы сделать ставку, введите через ПРОБЕЛЫ БЕЗ СКОБОК: [Cумма ставки (мин. 100 тёмкинсов)] [выбранный коэф.] [последнее число диапазона чисел] (к примеру: 500 4 10000)')
    bet = [int(i) for i in input().split()]
    while not is_bet_good(bet):
        bet = [int(i) for i in input(
            'Неправильный формат! Формат должен быть: Сумма(не менее 100) Коэффициент(2, 4, 10) Ограничивающее_Число(1000, 10000 или 100000): ').split()]

    number = randint(1, bet[2])
    trying = quantity_trying(bet)
    balance -= bet[0]
    balance_bot += bet[0]
    print('Я загадал число в диапазоне от 1 до', bet[2], '. Попробуй угадай! У тебя', trying, 'попыток.')

    while True:
        num = int(input())
        trying -= 1
        if trying < 1:
            print('Сожалею, но твои попытки закончились. Ты проиграл свою ставку. Кстати, загадал я число', number)
            break
        elif num > number:
            print('Моё число поменьше. Попробуй ещё разок. У тебя осталось', trying, 'попыток')
        elif num < number:
            print('Моё число больше. Попробуй ещё разок. У тебя осталось', trying, 'попыток')
        else:
            print('Везёт тебе,', name.title(), '. Выигрыш в', bet[0] * bet[1], 'твой. Всё по честному.')
            balance += bet[0] * bet[1]
            balance_bot -= bet[0] * bet[1]
            break

    next = input('Чтобы продолжить игру, напиши "далее"\n')
    while next.lower() != 'далее':
        next = input('Чтобы продолжить, введи "Далее"')

    game()


print(
    'Добро пожаловать в игру "Числовая угадайка". Меня зовут бот Тёмка! Я помогу тебе освоиться в игре. Чтобы продолжить, введи "Далее"')
next = input()
while next.lower() != 'далее':
    next = input('Чтобы продолжить, введи "Далее"')

print(
    '\nИтак, правила игры просты. У тебя есть игровой баланс: 1000 тёмкинсов. Чтобы стать тёмкинсонером, тебе надо выиграть у меня мои 9000 тёмкинсов и не потерять свои деньги. Это будет непросто. Ты должен угадывать загаданные мной числа в определенном диапазоне и за определённое количество попыток, которые ты можешь выбрать сам. Чем меньше ты выберешь попыток, тем больше денег можешь выиграть. Но будь осторожен. если проигрываешь - я забираю твою ставку. Ты готов начинать? Напиши "Да" или "Готов"')
next = input()
while next.lower() != 'готов' and next.lower() != 'готова' and next.lower() != 'да':
    next = input('Чтобы продолжить, введи "Да" или "Готов"')

name = input(
    'Сперва, тебе стоит представиться. Всё-таки нам предстоит провести вместе время, мне стоит знать, как тебя зовут :)\n')
print('\n\nРад знакомству', name.title())

balance = 1000
balance_bot = 9000
list_coef, list_bet = [2, 4, 10], [100, 1000, 10000]
list_try2, list_try4, list_try10 = [6, 9, 13], [5, 8, 12], [4, 7, 11]

game()
