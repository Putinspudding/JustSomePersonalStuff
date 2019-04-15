import copy
resource = 150
# process = {"Need": [70, 60, 60, 60], "Allocated": [25, 40, 45, 25]}
need = [70, 60, 60, 60]
allocated = [25, 40, 45, 25]
rest = []
all_measure = []
measure = []



def need_min_all(x):
    for i in range(0, len(need)):
        x.append(need[i]-allocated[i])


def judge_need(x, y):
    for i in x:
        if i > y:
            print("Not enough resource")
            return 0


def judge_rest(x, y, z):
    for i in range(0, len(x)):
        if i in measure:
            continue
        if len(measure) == len(x):
            #print(measure)
            return
        if x[i] <= y:
            measure.append(i)
            copyed_measure = copy.deepcopy(measure)
            #print(measure)
            if len(measure) == 4:
                #print(measure)
                z.append(copyed_measure)
            y = y + need[i]
            judge_rest(x, y, z)
            measure.pop()
            y = y - need[i]


def rest_re(x):
    resource_temp = resource
    for i in x:
        resource_temp = resource_temp-i
    return resource_temp


need_min_all(rest)
judge_need(need, resource)
rest_resource = rest_re(allocated)
judge_rest(rest, rest_resource, all_measure)
print(all_measure)

