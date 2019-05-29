import course
import manage
import sstatistics
import os
def quit():
    return 0
def menu():
    switch = {
        1: course.course,
        2: manage.studentManagement,
        3: sstatistics.studentStatistics,
        4: quit
    }
    print("请选择功能：")
    print("1、课程管理")
    print("2、学生成绩管理")
    print("3、学生成绩统计输出")
    print("4、退出")
    try:
        n = int(input())
    except:
        print("输入不合法，请重新输入")
        input()
        os.system('cls')
        menu()
    try:
        os.system('cls')
        switch[n]()
    except KeyError:
        print("输入不合法，请重新输入")
        input()
        os.system('cls')
        menu()

    return


if __name__ == '__main__':
    menu()
