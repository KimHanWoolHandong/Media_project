import pandas as pd
import csv, codecs
import matplotlib.pyplot as plt
import scipy.stats as stats


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

date_list = date_range('2013', '02', '2017', '05')
#print(date_list)






def read_csv_return_frame_index(csv_name):
    with codecs.open(csv_name, 'r', encoding='utf-8') as csvf:
        rd = csv.reader(csvf)
        next(rd)
        frame = []
        index = []
        for line in rd:
            if line[0] in date_list:
                frame.append([float(line[1]), float(line[2])])
                index.append(line[0])
            else:
                pass
    return frame, index
frame, index = read_csv_return_frame_index('kospi_n_donga.csv')
df = pd.DataFrame(frame, index=index, columns=['kospi', 'emotion'])
corr = stats.spearmanr(df.kospi, df.emotion)
print('donga')
print(corr)
"""

frame, index = read_csv_return_frame_index('kospi_n_hangyeong.csv')
df = pd.DataFrame(frame, index=index, columns=['kospi', 'emotion'])
corr = stats.spearmanr(df.kospi, df.emotion)
print('hangyeong')
print(corr)

frame, index = read_csv_return_frame_index('kospi_n_hangyeorea.csv')
df = pd.DataFrame(frame, index=index, columns=['kospi', 'emotion'])
corr = stats.spearmanr(df.kospi, df.emotion)
print('hangyeorea')
print(corr)

frame, index = read_csv_return_frame_index('kospi_n_hankook.csv')
df = pd.DataFrame(frame, index=index, columns=['kospi', 'emotion'])
corr = stats.spearmanr(df.kospi, df.emotion)
print('hankook')
print(corr)

frame, index = read_csv_return_frame_index('kospi_n_josun.csv')
df = pd.DataFrame(frame, index=index, columns=['kospi', 'emotion'])
corr = stats.spearmanr(df.kospi, df.emotion)
print('josun')
print(corr)
frame, index = read_csv_return_frame_index('kospi_n_jungang.csv')
df = pd.DataFrame(frame, index=index, columns=['kospi', 'emotion'])
corr = stats.spearmanr(df.kospi, df.emotion)
print('jungang')
print(corr)

frame, index = read_csv_return_frame_index('kospi_n_kookmin.csv')
df = pd.DataFrame(frame, index=index, columns=['kospi', 'emotion'])
corr = stats.spearmanr(df.kospi, df.emotion)
print('kookmin')
print(corr)

frame, index = read_csv_return_frame_index('kospi_n_kyenghyang.csv')
df = pd.DataFrame(frame, index=index, columns=['kospi', 'emotion'])
corr = stats.spearmanr(df.kospi, df.emotion)
print('kyeonghyang')
print(corr)

frame, index = read_csv_return_frame_index('kospi_n_meagyeong.csv')
df = pd.DataFrame(frame, index=index, columns=['kospi', 'emotion'])
corr = stats.spearmanr(df.kospi, df.emotion)
print('myeagyeong')
print(corr)

frame, index = read_csv_return_frame_index('kospi_n_moonhwa.csv')
df = pd.DataFrame(frame, index=index, columns=['kospi', 'emotion'])
corr = stats.spearmanr(df.kospi, df.emotion)
print('moonhwa')
print(corr)

frame, index = read_csv_return_frame_index('kospi_n_seagyea.csv')
df = pd.DataFrame(frame, index=index, columns=['kospi', 'emotion'])
corr = stats.spearmanr(df.kospi, df.emotion)
print('seagyea')
print(corr)

frame, index = read_csv_return_frame_index('kospi_n_seoul.csv')
df = pd.DataFrame(frame, index=index, columns=['kospi', 'emotion'])
corr = stats.spearmanr(df.kospi, df.emotion)
print('seoul')
print(corr)
"""