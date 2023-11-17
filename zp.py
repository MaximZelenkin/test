from datetime import date
import calendar
import datetime


YEAR = 2023
MONTH = 11
SALARY = 60000


def quantity_work_day(year=YEAR, month=MONTH):
    last_day = (calendar.monthrange(year, month)[1])
    list_work_day = []

    for i in range(1, last_day + 1):
        name_day = date.ctime(datetime.date(year,month,i))[:3]
        if name_day != 'Sun' and name_day != 'Sat':
            list_work_day.append(name_day)
        else:
            pass

    return len(list_work_day)


def quantity_work_day_before_10(year=YEAR, month=MONTH):
    last_day = (calendar.monthrange(year, month)[1])
    list_work_day_before_10 = []

    for i in range(1, 10):
        name_day = date.ctime(datetime.date(year,month,i))[:3]
        if name_day != 'Sun' and name_day != 'Sat':
            list_work_day_before_10.append(name_day)
        else:
            pass

    return len(list_work_day_before_10)


def quantity_work_day_after_10(year=YEAR, month=MONTH):
    last_day = (calendar.monthrange(year, month)[1])
    list_work_day_after_10 = []

    for i in range(10, last_day + 1):
        name_day = date.ctime(datetime.date(year,month,i))[:3]
        if name_day != 'Sun' and name_day != 'Sat':
            list_work_day_after_10.append(name_day)
        else:
            pass

    return len(list_work_day_after_10)


tax = 13/100*SALARY
net_profit = SALARY - tax

salary_for_day_last_month = net_profit / quantity_work_day(YEAR, MONTH - 1)
salary_for_day_currant_month = net_profit / quantity_work_day(YEAR, MONTH)

salary_10 = salary_for_day_last_month * quantity_work_day_after_10(YEAR, MONTH - 1)
salary_25 = salary_for_day_currant_month * quantity_work_day_before_10(YEAR, MONTH)

print('Получка 10 числа: ', salary_10.__round__(2), ' руб.')
print('Получка 25 числа: ', salary_25.__round__(2), ' руб.')
print('Сумма за декабрь: ', sum([salary_10, salary_25]).__round__(2), ' руб.')







