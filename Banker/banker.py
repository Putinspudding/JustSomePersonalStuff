import random
resource = 150
# process = {"Need": [70, 60, 60, 60], "Allocated": [25, 40, 45, 25]}
need = [70, 60, 60, 60]
allocated = [25, 40, 45, 25]
rest = []
all_measure = []
measure = []
digit = 0



def need_min_all(x):
    for i in range(0, len(need)):
        x.append(need[i]-allocated[i])


def judge_need(x, y):
    for i in x:
        if i > y:
            print("Not enough resource")
            return 0


def judge_rest(x, y):
    y_backup = y
    global digit
    while digit < len(x):
        while digit in measure:
            digit = digit + 1
        if x[digit] <= y:
            measure.append(digit)
            y = y + need[digit]
            digit = 0
            if len(measure) == len(x):
                y = y_backup
                all_measure.append(measure)
                print(measure)
                del measure[::]
        else:
            digit = digit + 1



def rest_re(x):
    resource_temp = resource
    for i in x:
        resource_temp = resource_temp-i
    return resource_temp


need_min_all(rest)
judge_need(need, resource)
rest_resource = rest_re(allocated)
judge_rest(rest, rest_resource)
print(all_measure)

