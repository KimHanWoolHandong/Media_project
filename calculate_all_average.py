from konlpy.tag import Komoran
import csv, codecs


"""
komoran = Komoran()
content = "내가 지금 무엇을 하고 있을까?"
content_morphs = komoran.pos(content)
print(content_morphs)
"""

def calculate_csv(csv_locate, pos_dic, neg_dic, komoran):
    news = {'경향신문': 0, '국민일보': 0, '동아일보': 0, '문화일보': 0,
            '서울신문': 0, '세계일보': 0, '조선일보': 0, '중앙일보': 0,
            '한겨레': 0, '한국일보': 0, '매일경제': 0, '한국경제': 0}
    count = {'경향신문': 0, '국민일보': 0, '동아일보': 0, '문화일보': 0,
            '서울신문': 0, '세계일보': 0, '조선일보': 0, '중앙일보': 0,
            '한겨레': 0, '한국일보': 0, '매일경제': 0, '한국경제': 0}
    with codecs.open(csv_locate, 'r', encoding='utf-8') as csvf:
        rd = csv.reader(csvf)
        next(rd)
        i = 0
        for line in rd:
            if line[1] == "" or line[1] not in news.keys():
                pass
            else:
                morphs = komoran.pos(line[2])
                score = cal_pos_neg(morphs, pos_dic, neg_dic)
                news[line[1]] = score + news[line[1]]
                print(line[1] + " " + str(score))
                count[line[1]] = 1 + count[line[1]]
            print(str(i)+"th")
            i += 1
    print(news)
    print(count)
    average = {'경향신문': 0, '국민일보': 0, '동아일보': 0, '문화일보': 0,
            '서울신문': 0, '세계일보': 0, '조선일보': 0, '중앙일보': 0,
            '한겨레': 0, '한국일보': 0, '매일경제': 0, '한국경제': 0}
    for name in average.keys():
        if count[name] == 0:
            average[name] = 'None'
        else:
            average[name] = news[name] / count[name]
    print(average)

def dictionary_creating():
    pos_dic = {}
    with codecs.open('./pos.csv', 'r', encoding='utf-8') as csvf:
        rd = csv.reader(csvf)
        for line in rd:
            char = line[0].split('+')
            text_comprehensive = []
            for text in char:
                morph_n_type = text.split('/')
                text_comprehensive.append((morph_n_type[0],morph_n_type[1]))
            if len(text_comprehensive) == 1:
                pos_dic[(text_comprehensive[0])] = line[1]
            else:
                pos_dic[tuple(text_comprehensive)] = line[1]

    neg_dic = {}
    with codecs.open('./neg.csv', 'r', encoding='utf-8') as csvf:
        rd = csv.reader(csvf)
        for line in rd:
            char = line[0].split('+')
            #print(char)
            text_comprehensive = []
            for text in char:
                morph_n_type = text.split('/')
                text_comprehensive.append((morph_n_type[0], morph_n_type[1]))
            if len(text_comprehensive) == 1:
                neg_dic[(text_comprehensive[0])] = line[1]
            else:
                neg_dic[tuple(text_comprehensive)] = line[1]

    return pos_dic, neg_dic

def find_word(word, pos_dic, neg_dic):
    Flag = True
    pos = 0
    neg = 0
    if word in pos_dic.keys():
        #print('pos')
        pos = float(pos_dic[word])
        Flag = False
    if word in neg_dic.keys():
        #print('neg')
        neg = float(neg_dic[word])
        Flag = False
    return pos, neg, Flag

def cal_pos_neg(content, pos_dic, neg_dic):
    print(content)
    length = len(content)
    neg_count = 0
    pos_count = 0
    for i in range(length):
        if length-i >= 3:
            three_word = (content[i], content[i+1], content[i+2])
            pos, neg, Flag = find_word(three_word, pos_dic, neg_dic)
            if Flag:
                second_word = (content[i], content[i + 1])
                pos, neg, Flag = find_word(second_word, pos_dic, neg_dic)
                if Flag:
                    word = (content[i])
                    pos, neg, Flag = find_word(word, pos_dic, neg_dic)
                    pos_count += pos
                    neg_count += neg
                else:
                    pos_count += pos
                    neg_count += neg
            else:
                pos_count += pos
                neg_count += neg
        elif length-i == 2:
            second_word = (content[i], content[i + 1])
            pos, neg, Flag = find_word(second_word, pos_dic, neg_dic)
            if Flag:
                word = (content[i])
                pos, neg, Flag = find_word(word, pos_dic, neg_dic)
                pos_count += pos
                neg_count += neg
            else:
                pos_count += pos
                neg_count += neg
        else:
            word = (content[i])
            pos, neg, Flag = find_word(word, pos_dic, neg_dic)
            pos_count += pos
            neg_count += neg
    print(pos_count)
    print(neg_count)
    score = 0
    if pos_count > neg_count:
        score = pos_count / (pos_count + neg_count)
    elif neg_count > pos_count:
        score = -neg_count / (pos_count + neg_count)
    else:
        score = 0
    return score



komoran = Komoran()
pos_dic, neg_dic = dictionary_creating()
calculate_csv('./MJI.csv', pos_dic, neg_dic, komoran)

"""
content = "지금 상황이 안좋네요"

content_morphs = komoran.pos(content)
cal_pos_neg(content_morphs, pos_dic, neg_dic)
"""






