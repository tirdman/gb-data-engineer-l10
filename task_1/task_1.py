def salary_calc(hours, rate, bonus):
    """
    Функция расчета заработанной платы
    :param hours: отработанные часы
    :param rate: ставка
    :param bonus: премия
    :return: возвращает расчитанную заработанную плату
    """
    if float(hours) < 0 or float(rate) < 0 or float(bonus) < 0:
        print('Все введенные значения не должны быть отрицательными')
        return

    return (float(hours) * float(rate)) + float(bonus)


if __name__ == '__main__':
    print(salary_calc(48, 2000, 'ee'))
