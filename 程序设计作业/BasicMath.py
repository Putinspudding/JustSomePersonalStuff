def Avg(a:list):
    sum = 0
    n = 0
    for numbers in a:
        if numbers == 'NULL':
            n = n+1
            continue
        sum = sum + numbers
    return sum/(len(a)-n)

def Max(a:list):
    max = 0
    for numbers in a:
        if numbers == 'NULL':
            continue
        if numbers>max:
            max = numbers
    return max

def Min(a:list):
    min = a[0]
    for numbers in a:
        if numbers == 'NULL':
            continue
        if numbers < min:
            min = numbers
    return min
