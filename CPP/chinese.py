'''
    G为邻接矩阵表示的无向图,G=[[]],G[i][j]表示的是点i与j边的数量，原点或无连通距离为0
'''
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

def judgement(G): #每个点关联边数目用字典表示
    oddEven={}
    for i in range(len(G)):
        num = 0
        for j in G[i]:
                num = num +j
        oddEven[i] = num
    return oddEven


def DFS(G,S,x,t):
    k=0 #标记当前访问的节点是否还有邻接边可供访问
    push(S,x) #将本次遍历边所经由的点入栈
    for i in range(t,len(G)): #len(G)代表的是无向图G的点数目
        if G[i][x] > 0:
            k = 1 #标志有邻接边可访问
            G[i][x] = G[i][x]-1 #删除这条边，因为考虑到存在两点之间可能有多条边的情况，所以并不直接将G[i][x]置0而是减1
            G[x][i] = G[x][i]-1 #同理，对另一点上记录的这条边进行删除
            DFS(G,S,i,0) #对i点进行递归操作
            break #结束循环
    if k==0: #标志无邻接边可访问
        pop(S) #将S中最顶端元素进行出栈操作
        m = getTop(S) #将目前S最顶端元素取值赋予m
        G[x][m] = G[x][m]+1 #恢复在上一层中被删除的边
        G[m][x] = G[m][x]+1
        a=x+1 #从当前节点下一条关联边开始选取
        if not stackLength(S) == e: #判断是否已经遍历完全，e是无向图边的数量
            pop(S)
            DFS(G,S,m,a)
        else:
            push(S,x) #把原点放入栈顶


''''''
#测试用例
G=[[0,1,0,1,0,0],
   [1,0,1,1,1,0],
   [0,1,0,0,1,0],
   [1,1,0,0,1,1],
   [0,1,1,1,0,1],
   [0,0,0,1,1,0]]
G1=[[0,2,1,0,1],
    [2,0,1,1,0],
    [1,1,0,0,0],
    [0,1,0,0,1],
    [1,0,0,1,0]]
G2=[[0,2,0,0,0],
    [2,0,2,0,0],
    [0,2,0,1,1],
    [0,0,1,0,1],
    [0,0,1,1,0]]
#print(judgement(G))
S=[]
e = numbers(judgement(G))
DFS(G,S,0,0)
print(S)
S1=[]
e = numbers(judgement(G1))
print(e)
DFS(G1,S1,0,0)
print(S1)
#S2=[]
#e = numbers(judgement(G2))
#DFS(G2,S2,0,0)
#print(S2)
''''''
