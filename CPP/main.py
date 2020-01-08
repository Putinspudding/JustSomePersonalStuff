import copy
import math #用于调用math.inf
import random


S = [] #用列表作栈，用来表示最终最短路径顺序
route = [] #对最后所得路径进行初始化
path = []
route = [] #初始化用来表示两奇点之间最短路径顺序



def judgeG(G): #当邻接矩阵数值表示边数量时每个点关联边数目用字典表示
    oddEven={}
    for i in range(len(G)):
        num = 0
        for j in G[i]:
                num = num +j
        oddEven[i] = num
    return oddEven

def judgement(G): #当邻接矩阵数值表示路径长度时每个点关联边数目用字典表示
    oddEven={}
    for i in range(len(G)):
        num = 0
        for j in G[i]:
            if j>0 and not j == math.inf:
                num = num + 1
        oddEven[i] = num
    return oddEven


def DFS(G,S,e,x,t):
    k=0 #标记当前访问的节点是否还有邻接边可供访问
    push(S,x) #将本次遍历边所经由的点入栈
    for i in range(t,len(G)): #len(G)代表的是无向图G的点数目
        if G[i][x] > 0:
            k = 1 #标志有邻接边可访问
            G[i][x] = G[i][x]-1 #删除这条边，因为考虑到存在两点之间可能有多条边的情况，所以并不直接将G[i][x]置0而是减1
            G[x][i] = G[x][i]-1 #同理，对另一点上记录的这条边进行删除
            DFS(G,S,e,i,0) #对i点进行递归操作
            break #结束循环
    if k==0: #标志无邻接边可访问
        pop(S) #将S中最顶端元素进行出栈操作
        m = getTop(S) #将目前S最顶端元素取值赋予m
        G[x][m] = G[x][m]+1 #恢复在上一层中被删除的边
        G[m][x] = G[m][x]+1
        a=x+1 #从当前节点下一条关联边开始选取
        if not stackLength(S) == e: #判断是否已经遍历完全，e是无向图边的数量
            pop(S)
            DFS(G,S,e,m,a)
        else:
            push(S,x) #把原点放入栈顶

def push(lists,x): #入栈操作
    lists.append(x)

def pop(lists): #出栈操作
    lists.pop()

def getTop(lists): #获取栈顶元素
    return lists[-1]

def stackLength(lists): #获取栈长度
    return len(lists)

def numbers(dicts): #计算无向图共有多少边
    num = 0
    for i in dicts.values():
        num = num+i
    return num//2

def change(G): #将无向图G的邻接矩阵其中的值由路径长度变为边的数量
    Gnew = copy.deepcopy(G)
    for i in range(len(Gnew)):
        for j in range(len(Gnew)):
            if Gnew[i][j] == math.inf:
                Gnew[i][j]=0
                continue
            if Gnew[i][j]>0:
                Gnew[i][j]=1
    return Gnew


def cpp(G,x):
    odd = []
    dicts = judgement(G)
    for i in dicts:
        if dicts[i]%2 == 1: #判断有无奇点
            odd.append(i) #记录奇点序号
    if odd:
        path = initPath(G)
        floyd(G,path)
        printPath(path,odd[0],odd[1])
        newG = change(G)
        for i in range(0,len(route)-1): #对两奇点之间最小路径上每条边边数加一
            newG[route[i]][route[i]+1] = newG[route[i]][route[i]+1]+1
            newG[route[i]+1][i] = newG[route[i]+1][i]+1
        e = numbers(judgeG(newG))
        DFS(newG,S,e,x,0)
        pass
    else:
        newG=change(G)
        e = numbers(judgeG(newG))
        DFS(newG,S,e,x,0)

def initPath(G):
    return [[-1 for col in range(len(G))] for row in range(len(G))] #初始化path二维列表，并将其中所有元素置-1




def node_num(G): #根据无向图的邻接矩阵获取节点数目
    return len(G)

def getPath(path,i, j): #根据path列表获取从i到j的路径
    if not i == j: #判断递归出口
        if path[i][j] == -1:
            route.append(j)
        else:
            getPath(path,i, path[i][j])
            getPath(path,path[i][j], j)


def printPath(path,i, j): #对路径进行输出
    route.append(i)
    getPath(path,i, j)

def floyd(G,path):
    dis = copy.deepcopy(G) #创建一个新列表，对无向图的邻接矩阵进行深拷贝
    for k in range(node_num(G)):
        for i in range(node_num(G)):
            for j in range(node_num(G)):
                if dis[i][j] > dis[i][k] + dis[k][j]:
                    dis[i][j] = dis[i][k] + dis[k][j]
                    path[i][j] = k #将节点路径写入path
    return dis









G1=[[0,1,0,1,0,0],
   [1,0,1,1,1,0],
   [0,1,0,0,1,0],
   [1,1,0,0,1,1],
   [0,1,1,1,0,1],
   [0,0,0,1,1,0]]
G2=[[0,5,4,math.inf,1],
    [5,0,3,2,math.inf],
    [4,3,0,math.inf,math.inf],
    [math.inf,2,math.inf,0,7],
    [1,math.inf,math.inf,7,0]]
#print(judgement(G1))
cpp(G1,0)
print("G1:",S)
S = []
cpp(G2,1)
print("G2:",S)
route=[]
#print(route)
#cpp(G1,0)