import pandas as pd
import csv, codecs
import matplotlib.pyplot as plt

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

date_list = date_range('2017', '05', '2020', '01')






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


frame, index = read_csv_return_frame_index('kospi_n_seoul.csv')
df = pd.DataFrame(frame, index=index, columns=['kospi', 'emotion'])
corr = df.corr(method='spearman')
df.plot.line()
plt.show()

#print(df)
print(corr)

'''
lst = [[1,2,3,4,5,6,7],
       [10,15,20,25,50,55,60],
       [0,0,0,0,0,0,0],
       [-1,-20,-30,-45,-50,-55,-70]]
df = pd.DataFrame(lst).T
corr = df.corr(method='pearson')
print(corr)
'''
