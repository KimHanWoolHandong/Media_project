import csv, codecs

president = ['김대중', '노무현', '이명박', '박근혜', '문재인']
date = {'김대중': '200301', '노무현': '200801', '이명박': '201301',
        '박근혜': '201704', '문재인': '201912'}
presd_sum = {'김대중':0, '노무현': 0, '이명박':0, '박근혜':0, '문재인':0}
presd_count = {'김대중':0, '노무현': 0, '이명박':0, '박근혜':0, '문재인':0}

def calculate_csv(csv_locate):
    with codecs.open(csv_locate, 'r', encoding='utf-8') as csvf:
        rd = csv.reader(csvf)
        i = 0
        all_sum = 0
        all_count = 0
        for line in rd:
            presd_sum[president[i]] += float(line[2])
            all_sum += float(line[2])
            presd_count[president[i]] += float(line[3])
            all_count += float(line[3])
            if date[president[i]] == line[1]:
                i+=1
        print('전체')
        print(all_sum/all_count)
        for i in range(len(president)):
            print(president[i])
            print(presd_sum[president[i]]/presd_count[president[i]])


calculate_csv('./donga_result.csv')

"""
content = "지금 상황이 안좋네요"

content_morphs = komoran.pos(content)
cal_pos_neg(content_morphs, pos_dic, neg_dic)
"""






