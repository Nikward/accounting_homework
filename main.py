from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
if __name__ == '__main__':
    date1 = datetime.now()
    date2 = datetime(day=31, month=12, year=2022)
    print(f' Сегодня: {date1}  \n До нового года осталось: {(date2 - date1)}')

    get_employees()
    calculate_salary()
