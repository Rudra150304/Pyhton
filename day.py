import calendar

def days(date, month, year):
    day_index = calendar.weekday(year, month, date)
    day = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    return day[day_index]

def main():
    date = int(input("Enter date: "))
    month = int(input("Enter month: "))
    year = int(input("Enter year: "))
    print(f"The day on {date}/{month}/{year} is {days(date, month, year)}")

if __name__ == '__main__':
    main()