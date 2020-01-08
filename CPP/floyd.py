'''
    对于邻接矩阵G，G[i][j]表示点i到j的距离,若i与j之间无直接边连接则用math.inf表示
'''
import copy
import math #用于调用math.inf

path = [[-1 for col in range(5)] for row in range(5)] #初始化path二维列表，并将其中所有元素置-1
route = [] #对最后所得路径进行初始化
def node_num(G): #根据无向图的邻接矩阵获取节点数目
    return len(G)

def getPath(i, j): #根据path列表获取从i到j的路径
    if not i == j: #判断递归出口
        if path[i][j] == -1:
            route.append(j)
        else:
            getPath(i, path[i][j])
            getPath(path[i][j], j)


def printPath(i, j): #对路径进行输出
    route.append(i)
    getPath(i, j)

def floyd(G):
    dis = copy.deepcopy(G) #创建一个新列表，对无向图的邻接矩阵进行深拷贝
    for k in range(node_num):
        for i in range(node_num):
            for j in range(node_num):
                if dis[i][j] > dis[i][k] + dis[k][j]:
                    dis[i][j] = dis[i][k] + dis[k][j]
                    path[i][j] = k #将节点路径写入path
    return dis

G1=[[0,5,1,math.inf,1],
    [5,0,3,2,math.inf],
    [4,3,0,math.inf,math.inf],
    [math.inf,2,math.inf,0,7],
    [1,math.inf,math.inf,7,0]]
node_num = node_num(G1)
floyd(G1)
printPath(1,4)
print(route)
