from datetime import datetime
from server import parse_shedule
from server import find_group
from server import days_in_week
import datetime


#функция возвращающая название текущего дня недели
def in_day():
    return(days_in_week[datetime.datetime.today().weekday()])

#Фунция вывода рассписания
def print_shedule(k, group_name, fragment=in_day()):

    week = parse_shedule((find_group(k, group_name)))
    message = ""


    if (fragment in days_in_week):
        day = f"{fragment}\n ------------\n"
        for string in week[fragment]:
            day+=string + "\n"
        message+=day
    else:
        for days in week:
            day = f"{days}\n ------------\n"
            for string in week[days]:
                day+=string + "\n"
            day+="\n"
            message+=day
    return(message)

#Функция сравнения расписаний двух групп
def comparision(k1, group1, k2, group2, day='Вторник'):

    week1 = parse_shedule((find_group(k1, group1)))
    week2 = parse_shedule((find_group(k2, group2)))
    
    sum1 = 0
    
    for string in week1[day]:
        sum1 += 1

    sum2 = 0
    for string in week2[day]:
        sum2 += 1

    print(f"Пар у {group1}: {sum1}, а у {group2}: {sum2}")
    if(sum1 != 0):
        print(week1[day][-1])
    if(sum2 != 0):
        print(week2[day][-1])