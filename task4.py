
from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Mary Woker", "birthday": "1981.03.21"},
    {"name": "Olga Masnyk", "birthday": "1981.03.17"}
]

def get_upcoming_birthdays(users):
    upcoming_birthday = []
    now = datetime.today().date()
    one_day = timedelta(days=1)
    two_days = timedelta(days=2)
    for user in users:
        try:
            user["birthday"] = datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=now.year)
            if user["birthday"]  < now:
                user["birthday"] = user["birthday"].replace(year=now.year +1)
            if 0 <= (user["birthday"]- now).days <=7:
                if user["birthday"].weekday() == 5:
                    user["birthday"] = user["birsday"] + two_days
                if user["birthday"].weekday() == 6:
                    user["birthday"] = user["birthday"] + one_day
                upcoming_birthday = [{"name": user["name"], "congratulation_date": user["birthday"]}]

        except ValueError:
            print(f'Некоректна дата народження користувача {user["name"]}')    
    return upcoming_birthday    
        

    

