# 1
import datetime

def day_diff(release_date, code_complete_day):
    release_date_format = '%d/%m/%Y' 
    release_date_obj = datetime.datetime.strptime(release_date, release_date_format)

    code_complete_day_format = '%Y-%d-%m' 
    code_complete_day_obj = datetime.datetime.strptime(code_complete_day, code_complete_day_format)
    return (code_complete_day_obj - release_date_obj).days

    pass

def alpha_num(sentence):
    sentence_lst = sentence.split()
    alpha_num_lst = []
    existAlpha = False
    existNum = False    
    for item in sentence_lst:
         existAlpha = False
         existNum = False
         for i in item:
             if i.isalpha():
                 existAlpha = True
             if i.isnumeric():
                 existNum = True
             if (existAlpha and existNum):
                 alpha_num_lst.append(item)
                 break

    return alpha_num_lst
    pass
# 2


print(day_diff('30/09/2021','2021-30-10'))
print(alpha_num('fdfd1 dddd hgg1 gf 1123 fgff'))
