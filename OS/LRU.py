wait = []

def findleast(memo):
    list_key = list(memo.keys())
    list_value = list(memo.values())
    max = list_value[0]
    max_num = 0
    for i in range(1, len(list_value)):
        if list_value[i] > max:
            max = list_value[i]
            max_num = i
    max_key = list_key[max_num]
    del memo[max_key]

def lru(mem, wait, num):
    count = 0
    for i in wait:
        if i in mem.items():
            mem[i] = 0
        else:
            mem[i] = 0
            if(len(mem)>num):
                findleast(mem)
                count = count+1
        for j in list(mem.keys()):
            mem[j] += 1
        print(mem)
    print((float(count)+num)/len(wait))


request = [2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 2]
mem = {}
lru(mem, request, 3)
