from datetime import datetime

def main():
    """
    计算输入的日期是一年的第几天
    :return:
    """
    days_of_month = [31,28,31,30,31,30,31,31,30,31,30,31]

    input_date_str = input('Please input a date(yyyy/mm/dd):')
    print(input_date_str)

    day_of_year = 0
    flag = False


    input_day = datetime.strptime(input_date_str,'%Y/%m/%d')
    year = input_day.year
    month = input_day.month
    day = input_day.day

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        flag = True


    for days in days_of_month[:month-1]:
        day_of_year += days

    if flag == True and month >= 3:
        day_of_year += 1

    day_of_year += day

    print("{} is the {} day of the year".format(input_day,day_of_year))


if __name__ == '__main__':
    main()
