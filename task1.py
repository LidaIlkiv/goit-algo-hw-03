##Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

from datetime import datetime
def get_days_from_today(date:str ):
    try:
        now = datetime.today().date()    
        datetime_date = datetime.strptime(date, "%Y-%m-%d").date()       
        delta = (datetime_date - now).days
        return delta
    except ValueError:
        print('Invalid date format!!!  Valid date format - РРРР-ММ-ДД')
        






