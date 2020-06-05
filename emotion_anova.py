import pandas as pd
import csv, codecs
import matplotlib.pyplot as plt
import scipy.stats as stats

import scipy.stats as stats
import pandas as pd
import urllib
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import numpy as np

date = [[('1990','01'), ('1993','02')], [('1993','02'), ('1998','02')],
        [('1998','02'), ('2003','02')], [('2003','02'), ('2008','02')],
        [('2008','02'), ('2013','02')], [('2013','02'), ('2017','05')],
        [('2017','05'), ('2020','01')]]

def date_range(first_year, first_month, last_year, last_month):
    date_list = []
    current_year = first_year
    current_month = first_month
    Flag = True
    while Flag:
        date_list.append(current_year + current_month)
        if current_month == "12":
            current_year = str(int(current_year)+1)
            current_month = "01"
        else:
            current_month = str(int(current_month)+1).zfill(2)
        if (current_year+current_month) == (last_year+last_month):
            Flag = False
    return date_list


def anova(data):
    F_statistic, pVal = stats.f_oneway(data[0], data[1], data[2], data[3])
    print(F_statistic)
    print(pVal)



def read_csv_return_frame_index(csv_name, start_num):
    with codecs.open(csv_name, 'r', encoding='utf-8') as csvf:
        rd = csv.reader(csvf)
        next(rd)
        all_list = []
        emotion_list = []
        current_num = start_num
        for line in rd:
            dates = date[current_num]
            date_list = date_range(dates[0][0], dates[0][1], dates[1][0], dates[1][1])
            if line[0] in date_list:
                emotion_list.append(float(line[2]))
            else:
                current_num+=1
                all_list.append(emotion_list)
                emotion_list = []
        all_list.append(emotion_list)
    return all_list

data_list = read_csv_return_frame_index('kospi_n_josun.csv', 3)
anova(data_list)