import requests
from bs4 import BeautifulSoup as BS

#Массив дней недели
days_in_week=["Понедельник","Вторник","Среда",
              "Четверг","Пятница","Суббота","Воскресенье"]

#Массив номеров пар
number = ['1','2','3','4',
          '5','6','7','8']

#Функия парсинга расписания
def parse_shedule(lk):
    r = requests.get(lk)
    html = BS(r.content, 'html.parser')

    week={}

    day=""

    for el in html.select(".text-center, .adopt_area_scrollable >table > tbody > tr"):
        day_of_week = el.text.split() 
        
        words = ""

        
        if (not (day_of_week[0] in days_in_week ) and not (day_of_week[0] in number)):
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


#Функция поиска сайта расписания группы
def find_group(k, group_name):
    r = requests.get(f"https://ies.unitech-mo.ru/schedule_list_groups?i=0&f=0&k={k}")
    html = BS(r.content, 'html.parser')

    for el in html.select("tr"):
        blok= el.text.split()
        if (blok[0] == group_name):
            lk = el.a['href']
            break
    
    return(f'https://ies.unitech-mo.ru{lk}')    