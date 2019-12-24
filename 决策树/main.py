import decide
import pandas as pd
import numpy as np
import copy

class Tree:
    def __init__(self,rootObj=""):
        self.value = rootObj
        self.leftchild=Tree
        self.middlechild=Tree
        self.rightchild=Tree
        self.leftweight=''
        self.middleweight=''
        self.rightweight=''
    def getweight(self,dicts):
        for i in dicts:
            if not self.leftweight:
                self.leftweight=i
                continue
            if not self.middleweight:
                self.middleweight=i
                continue
            if not self.rightweight:
                self.rightweight=i
                continue
    def printf(self):
        print(self.value,self.leftchild,self.middlechild,self.rightchild,self.leftweight,self.middleweight,self.rightweight)
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
#D=decide.tolists(buy,D)
#print(D)
#infoD=decide.info(D)

#以node为节点创建树
def makeTree(node,condiction={}):
    indicator = 0
    if not node:
        return
    print(condiction)
    D={}
    print(decide.tolists(buy,D,condiction))
    if len(decide.tolists(buy,D,condiction))==1:
        #当只有“买”或“不买”时，返回其值
        return Tree(list((decide.tolists(buy,D,condiction)).keys())[0])
    if (decide.tolists(buy,D,condiction))["买"]>20*(decide.tolists(buy,D,condiction))["不买"]:
        return Tree("买")
    if (decide.tolists(buy,D,condiction))["不买"]>20*(decide.tolists(buy,D,condiction))["买"]:
        return Tree("不买")
    #深拷贝condiction字典
    left = copy.deepcopy(condiction)
    middle = copy.deepcopy(condiction)
    right = copy.deepcopy(condiction)
    situation={}
    newcalss = decide.iterateInfo(chart,condiction)
    decide.tolists(chart[newcalss], situation, condiction)
    print(newcalss,situation)
    node = Tree(newcalss)
    node.getweight(situation)
    for m in chart:
        if m == "Count" or m == "Buy":
            continue
        if m not in condiction:
            indicator = 1
    if not indicator:
        return node
    #将situtation加进condiction里进行递归
    left[node.value]=node.leftweight
    middle[node.value]=node.middleweight
    right[node.value]=node.rightweight
    #print(left,middle,right)
    print("---------")
    if node.leftweight:
        node.leftchild=makeTree(node.leftchild,left)
    if node.middleweight:
        node.middlechild=makeTree(node.middlechild,middle)
    if node.rightweight:
        node.rightchild=makeTree(node.rightchild,right)
    return node

def run_test(node,example):
    if node.value in example:
        if node.leftweight == example[node.value]:
            return run_test(node.leftchild,example)
        if node.middleweight == example[node.value]:
            return run_test(node.middlechild, example)
        if node.rightweight == example[node.value]:
            return run_test(node.rightchild, example)
    else:
        return node.value


root=Tree("")
tree = makeTree(root)
print("---------")
test1={"Age":"老","Inccome":"中","Student":"否","Credict":"优"}
test2={"Age":"青","Inccome":"中","Student":"否","Credict":"良"}
test3={"Age":"青","Inccome":"中","Student":"是","Credict":"优"}
print("result:")
print(run_test(tree,test1))
print(run_test(tree,test2))
print(run_test(tree,test3))