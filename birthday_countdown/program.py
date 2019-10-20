import datetime

def print_header():
    print('-------------------------------------')
    print('           Birthday App')
    print('-------------------------------------')
    print()


def get_birthday_from_user():
    print("When were you born? ")
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))

    birthday = datetime.date(year, month, day)
    return birthday


def compute_days_between_dates(date1, date2):
    dt = date1 - date2
    return dt.days


def print_birthday_information():
    pass


def main():
    print_header()
    bday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print(number_of_days)
    # print_birthday_information()


main()