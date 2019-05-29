import pandas as pd
import numpy as np
label = pd.read_csv("GradeInformation.csv",encoding='gbk')
#label['TEST'] = pd.Series()
#label.rename(columns={'TEST':'Eng'},inplace=True)
#print(label.append({'姓名': '小黄'}, ignore_index=True))
#print(label.drop(columns=['Python']))
#label.to_csv("GradeInformation.csv",encoding='gbk',index=False)
#label.index[label['姓名'] == '小白'].astype(int)
label.loc[label.index[label['姓名'] == '小白'],'语文']=80
print(label)