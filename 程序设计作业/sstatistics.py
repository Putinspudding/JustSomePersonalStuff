import datastruction
import os
def AllAvg():
    pass
def AllMax():
    pass
def AllMin():
    pass
def PerAvg():
    pass
def PerMax():
    pass
def PerMin():
    pass
def quit():
    datastruction.menu()
def studentStatistics():
    switch = {
        1: AllAvg,
        2: AllMax,
        3: AllMin,
        4: PerAvg,
        5: PerMax,
        6: PerMin,
        7: quit
    }
    print("请选择功能：")
    print("1、所有学生每门功课的平均值")
    print("2、所有学生每门功课的最大值")
    print("3、所有学生每门功课的最小值")
    print("4、单个学生的所有课程的平均值")
    print("5、单个学生的所有课程的最大值")
    print("6、单个学生的所有课程的最小值")
    print("7、返回到上一级")
    try:
        static_number = int(input())
    except:
        print("输入不合法，请重新输入")
        input()
        os.system('cls')
        studentStatistics()
    try:
        os.system('cls')
        switch[static_number]()
    except KeyError:
        print("输入不合法，请重新输入")
        input()
        os.system('cls')
        studentStatistics()
