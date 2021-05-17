import pandas as pd
import numpy as np
import date
from matplotlib import pyplot as plt
def judge_func(file, date):
    # 检查当日是否休市
    try:
        file.loc[date]
        return False
    except:
        return True

def get_lograte(file):
    # 获取时间序列
    date_list = date.get_time_sequence(2015, 2020)
    print(date_list)

    # 每个月的收盘价
    close_list = []
    for i in date_list:
        day = i
        while(judge_func(file, day)):# 如果当天休市
            day = date.fix_date(day)# 往后挪一天继续检测
        close_list.append(file.loc[day]["Close"])# 返回当天收盘价

# 计算对数收益率
    close_list = pd.Series(close_list)
    log_rate = np.log(close_list/close_list.shift(1))
    return log_rate


# 读入股票数据
file1 = pd.read_csv("./babe/babe/贵州茅台600519.SS.csv",index_col=["Date"])
lograte_1 = get_lograte(file1)
name1 = '贵州茅台600519'

file2 = pd.read_csv("./babe/babe/上汽集团600104.SS.csv",index_col=["Date"])
lograte_2 = get_lograte(file2)
name2= "上汽集团600104"

file3 = pd.read_csv("./babe/babe/牧原股份002714.SZ.csv",index_col=["Date"])
lograte_3 = get_lograte(file3)
name3= "牧原股份002714"

file4 = pd.read_csv("./babe/babe/美的集团000333.SZ.csv",index_col=["Date"])
lograte_4 = get_lograte(file4)
name4 = "美的集团000333"

file5 = pd.read_csv("./babe/babe/海康威视002415.SZ.csv",index_col=["Date"])
lograte_5 = get_lograte(file5)
name5 = "海康威视002415"
# 画图部分
plt.figure(figsize=(15,6))

# 设置中文字体
font={'family':'Microsoft Yahei','weight':'bold'}
plt.rc('font',**font)

plt.xlabel("日期")
plt.ylabel("对数变化率")
plt.title("五支股票的对数变化率")
plt.plot(lograte_1, label=name1)
plt.plot(lograte_2, label=name2)
plt.plot(lograte_3, label=name3)
plt.plot(lograte_4, label=name4)
plt.plot(lograte_5, label=name5)
plt.grid()
plt.legend()
l = [i for i in range(0,73,12)]
year = [i for i in range(2015,2022)]
plt.xticks(l,year)
plt.show()

