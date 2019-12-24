import pandas as pd
import numpy as np
import math

D={}
filename="t1.csv"
label=pd.read_csv(filename,encoding='gbk')
count=(label["计数"].to_list())
age=(label["年龄"].to_list())
income=(label["收入"].to_list())
student=(label["学生"].to_list())
credict=(label["信誉"].to_list())
buy=(label["归类：买计算机？"].to_list())
chart={"Count":count,"Age":age,"Inccome":income,"Student":student,"Credict":credict,"Buy":buy}


#求D0和D1
def tolists(classes,dicts,filters={}):
    if filters:
        for i in range(0, len(classes)):
            yes = 1
            for k in filters:
                #print(chart[k][i],filters[k])
                if not chart[k][i] == filters[k]:
                    yes = 0
                    break
            #print(yes)
            if yes:
                if classes[i] in dicts:
                    dicts[classes[i]] = dicts[classes[i]] + count[i]
                else:
                    dicts[classes[i]] = count[i]
    else:
        for i in range(0,len(classes)):
            if classes[i] in dicts:
                dicts[classes[i]]=dicts[classes[i]]+count[i]
            else:
                dicts[classes[i]]=count[i]

    return dicts
#D=tolists(buy,D)

#将每个特征按照特征值进行分类统计并输出字典
def classify(classes):
    dicts={}
    for i in range(0,15):
        if classes[i] in dicts:
            if buy[i] in dicts[classes[i]]:
                dicts[classes[i]][buy[i]]=dicts[classes[i]][buy[i]]+count[i]
            else:
                dicts[classes[i]][buy[i]]=count[i]
        else:
            dicts[classes[i]]={}
            dicts[classes[i]][buy[i]]=count[i]
    return dicts

#对买与不买计算机的字典做出整齐规范
def changeToList(dicts):
    for i in dicts:
        if "买" not in dicts[i]:
            dicts[i]["买"]=0
        if "不买" not in dicts[i]:
            dicts[i]["不买"]=0
        dicts[i]=list(dicts[i].values())
    return dicts

#求n*log(2,n)
def nlog(n):
    if n == 0:
        return 0
    return n*math.log(n,2)

#求某特征值的INFO
def classifiedLists(dicts):
    numList=list(dicts.values())
    n=0
    infoA=0
    for i in numList:
        n=n+sum(i)
    for i in numList:
        infoA=infoA+sum(i)/n*(-nlog(i[0]/sum(i))-nlog(i[1]/sum(i)))
    return infoA

#求某一列表所有项总和
def sum(lists,filters={}):
    summary=0
    if filters:
        for i in range(0,len(lists)):
            infilter = 1
            for k in filters:
                if not chart[k][i] == filters[k]:
                    infilter=0
                    break
            if infilter:
                summary = summary+count[i]
    else:
        for i in range(0,len(lists)):
            summary = summary+lists[i]
    return summary

'''
def info(lists,filters={}):
    info=0
    if not filters:
        for i in lists:
            info = info-nlog(i/sum(lists))
        return info
    else:
        for i in range(0,len(lists)):
            infilters = 1
            for k in filters:
                if not chart[k][i] == filters[k]:
                    infilters=0
                    break
            if infilters:
                info=info-nlog
'''

#遍历字典中除filters之外的特征的INFO，从中选取最小的
def iterateInfo(dicts,filters={}):
    min=1
    k=''
    if not filters:
        for i in dicts:
            if i=="Count" or i=="Buy":
                continue
            if classifiedLists(changeToList(classify(chart[i])))<min:
                min = classifiedLists(changeToList(classify(chart[i])))
                k=i
    else:
        for i in dicts:
            if i == "Count" or i == "Buy":
                continue
            if i in filters:
                continue
            if classifiedLists(changeToList(classify(chart[i])))<min:
                min = classifiedLists(changeToList(classify(chart[i])))
                k=i
    return k
'''
#求Info（D）
infoD=info(D)
#print(infoD)
#InfoAge
age=classify(age)
changeToList(age)
infoAge=classifiedLists(age)
income=classify(income)
changeToList(income)
infoIncome=classifiedLists(income)
student=classify(student)
changeToList(student)
infoStu=classifiedLists(student)
credict=classify(credict)
changeToList(credict)
infoCre=classifiedLists(credict)
print(infoAge,infoIncome,infoStu,infoCre)
def Gain(infoAge,infoIncome,infoStu,infoCre):
    gain={"infoAge":infoAge,"infoIncome":infoIncome,"infoStu":infoStu,"infoCre":infoCre}
    max = 0
    k = ""
    for i in gain:
        if infoD-gain[i]>max:
            max = infoD-gain[i]
            k = i
    return k
devideElement = Gain(infoAge,infoIncome,infoStu,infoCre)
print(chart[devideElement])
#print(label)
newD={}
tolists(chart[devideElement],newD)
print(newD)
DW={}
tolists(buy,DW,filters={"infoAge":"中"})
print(DW)
'''