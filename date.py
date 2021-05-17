import datetime
import calendar
def getMonthFirstDayAndLastDay(year=None, month=None):
    """
    :param year: 年份，默认是本年，可传int或str类型
    :param month: 月份，默认是本月，可传int或str类型
    :return: firstDay: 当月的第一天，datetime.date类型
              lastDay: 当月的最后一天，datetime.date类型
    """
    if year:
        year = int(year)
    else:
        year = datetime.date.today().year

    if month:
        month = int(month)
    else:
        month = datetime.date.today().month

    # 获取当月第一天的星期和当月的总天数
    firstDayWeekDay, monthRange = calendar.monthrange(year, month)

    # 获取当月的第一天
    firstDay = datetime.date(year=year, month=month, day=1)
    lastDay = datetime.date(year=year, month=month, day=monthRange)

    return firstDay, lastDay

def get_time_sequence(start_year, end_year, s_or_e=1):
    # s_or_e 0输出月初日期，1输出月末日期
    date_list = []
    month = [i for i in range(1,13)]
    year = [i for i in range(start_year,end_year+1)]
    for y in year:
        for m in month:
            a=getMonthFirstDayAndLastDay(y,m)[s_or_e]
            if a != None:
                date_list.append(str(a))
    return date_list

def fix_date(date):
    l = len(date)
    day=int(str(date[l-2:l]))-1
    date = date[:l-2]+str(day)
    return date


fix_date("2015-01-31")
