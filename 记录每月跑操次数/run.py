import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import html5lib
date = []
datedic = {}
number = input("请输入学号：")
name = input("请输入姓名:")
data = {'number': number, 'name': name}
r = requests.post('http://zccx.tyb.njupt.edu.cn/student', data=data)
soup = BeautifulSoup(r.text, "html5lib")
datearr = soup.find_all("td", {"arg": "日期"})
for i in datearr:
    text = i.text[1:]
    date.append(text)
while date:
    start = date.pop()
    end = date.pop()
    if(not start[5:7] in datedic):
        datedic[start[5:7]] = 0
    datedic[start[5:7]]=datedic[start[5:7]]+1
print(datedic)
plt.bar(datedic.keys(), datedic.values(), width=0.25)
plt.xlabel("Month")
for x, y in zip(datedic.keys(), datedic.values()):
    plt.text(x, y, '%d' % y, ha='center', va='bottom')
plt.savefig("大二上跑操记录")
plt.show()
