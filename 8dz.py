import requests
def val():
    valuta = []
    nameval = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    val = nameval ['Valute']
    for k,v in val.items():
        valuta.append([k,round(float(v.get('Value'))/float(v.get('Nominal')),2)])
    return max(valuta, key=lambda x: x[1])
    
val() 

Напишите класс Designer, который учитывает количество международных премий. 
Подсказки в коде занятия в разделе “Домашнее задание задача 3”.
Вопрос: Где этот самый "код занятия"? Если речь про ноутбук к лекциям, то там нет такого "раздела"

class Employee:
    def __init__(self, name, seniority):
        self.name = name
        self.seniority = seniority
        
        self.grade = 1
        
    def grade_up(self):
        self.grade +=1
        
    def publish_grade(self):
        print(self.name,self.grade)
        
    def check_if_it_is_time_for_upgrade(self):
        pass


 class Designer(Employee):
    def __init__(self, name, seniority, awards):
        super().__init__(name, seniority)
        self.awards= awards; 
    
    def check_if_it_is_time_for_upgrade(self): 
        self.seniority +=1
        
        if self.awards  == 2:
            self.seniority +=2
            
        if self.seniority % 7 == 0:
            self.grade_up()
            
            
        return self.publish_grade()

elena = Designer('Елена', seniority=0, awards=2)
for i in range(20):
    elena.check_if_it_is_time_for_upgrade()


Задание 2
Добавьте в класс Rate параметр diff (со значениями True или False), который в случае значения True в методах курсов валют (eur, usd итд) будет возвращать не курс валюты, а изменение по сравнению в прошлым значением. Считайте, self.diff будет принимать значение True только при возврате значения курса. При отображении всей информации о валюте он не используется.

import requests

class Rate:
    def __init__(self,  diff, format_='value'): 
        self.format = format_
        self.diff = diff;
         
    def exchange_rates(self):
        self.r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return self.r.json()['Valute']
        
    def make_format(self, currency):
        response = self.exchange_rates()
        
        if currency in response:     
            if self.format == 'full' or  self.diff == 'False':
                return response[currency]
            
            if self.format == 'value':
                return response[currency]['Value']
            
            if  self.diff == 'True':
                return response[currency]['Value'] - response[currency]['Previous']
            
        return 'Erroy'
  
       
    def eur(self):
        return self.make_format('EUR')
    
    def usd(self):
        return self.make_format('USD')
      
