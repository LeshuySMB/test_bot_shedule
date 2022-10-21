from email import message
from traceback import print_tb
from turtle import st
import requests
from bs4 import BeautifulSoup as BS

days_in_week=["Понедельник","Вторник","Среда",
              "Четверг","Пятница","Суббота","Воскресенье"]

def parse_shedule(lk):
    r = requests.get(lk)
    html = BS(r.content, 'html.parser')

    week={}

    day=""

    for el in html.select(".text-center, .adopt_area_scrollable >table > tbody > tr"):
        day_of_week = el.text.split() 
        
        words = ""


        if (((day_of_week[0] == "Скачать") or (day_of_week[0] == "Группа") or (day_of_week[0] == "8-я,"))):
            continue
        
        if (day == "" and day_of_week[0] in days_in_week):
            day = day_of_week[0]
            shedule = []
            continue
        
        if (day == "Воскресенье"):
            week[day] = shedule
            continue
        
        if (day_of_week[0] in days_in_week) and (day_of_week != day):
            week[day] = shedule
            shedule = []
            
            day = day_of_week[0]
            continue
        


        for word in day_of_week:
            words+=word + " "
        
        if (len(words) <= 16):
            continue
        

        shedule.append(words)

    return(week)

def find_group(k, group_name):
    r = requests.get(f"https://ies.unitech-mo.ru/schedule_list_groups?i=0&f=0&k={k}")
    html = BS(r.content, 'html.parser')

    for el in html.select("tr"):
        blok= el.text.split()
        if (blok[0] == group_name):
            lk = el.a['href']
            break
    
    return(f'https://ies.unitech-mo.ru{lk}')

def print_shedule(k, group_name, fragment="неделя"):
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
