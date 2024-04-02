import requests
from bs4 import BeautifulSoup
link = 'https://knastu.ru/students/schedule/ca5ea85f-3881-47c8-9cdc-fda4e4dd44ff'

def sheduleParse(link):
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    block_date = soup.find('div', id = 'div_visualdate')
    check_date = block_date.find('input', id = 'visual_date')
    check_date = str(check_date)[-13:-3]


    block_shedule = soup.find_all('td', title = 'Выбранная дата')
    chek_shedule = [block_shedule[i].text for i in range(0, len(block_shedule) - 1)]
    result_shedule = f'{check_date}\n'
    for i in range(0, len(chek_shedule) - 1):
        if 'Лекции' in chek_shedule[i]:
            chek_shedule[i] = str(chek_shedule[i]).replace('Лекции', ' Лекции ')
        if 'Практические занятия (УГ-1_ПР)' in chek_shedule[i]:
            chek_shedule[i] = str(chek_shedule[i]).replace('Практические занятия (УГ-1_ПР)', ' Практические занятия (УГ-1_ПР) ')
        if 'Практические занятия (УГ-3_ПР)' in chek_shedule[i]:
            chek_shedule[i] = str(chek_shedule[i]).replace('Практические занятия (УГ-3_ПР)', ' Практические занятия (УГ-3_ПР) ')
        if 'Лабораторные работы (УГ-3_ЛР)' in chek_shedule[i]:
            chek_shedule[i] = str(chek_shedule[i]).replace('Лабораторные работы (УГ-3_ЛР)', ' Лабораторные работы (УГ-3_ЛР) ')
        if 'Лабораторные работы (УГ-5_ЛР)' in chek_shedule[i]:
            chek_shedule[i] = str(chek_shedule[i]).replace('Лабораторные работы (УГ-5_ЛР)', ' Лабораторные работы (УГ-5_ЛР) ')
        if 'Лабораторные работы (УГ-6_ЛР)' in chek_shedule[i]:
            chek_shedule[i] = str(chek_shedule[i]).replace('Лабораторные работы (УГ-6_ЛР)', ' Лабораторные работы (УГ-6_ЛР) ')
        chek_shedule[i] = str(chek_shedule[i]).replace('?', '')
        result_shedule += chek_shedule[i] + '\n'


    return  result_shedule
result_shedule = sheduleParse(link)
