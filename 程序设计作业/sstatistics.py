import datastruction
import BasicMath
import os
import pandas as pd
import numpy as np
def AllAvg():
    label = pd.read_csv("GradeInformation.csv", encoding='gbk')
    course_name = input("请输入课程名称\n")
    try:
        label[course_name]
        # 判断课程是否存在
    except KeyError:
        print("您输入的课程不存在！请按回车确认后返回上一页！")
        input()
        os.system('cls')
        studentStatistics()
        return 0
    finally:
        course_list = (label[course_name].fillna("NULL")).to_list()
        print(course_name+"的平均值为： "+str(BasicMath.Avg(course_list))+"\n")
        input("按回车键返回上一页\n")
        os.system('cls')
        studentStatistics()
        return 0
def AllMax():
    label = pd.read_csv("GradeInformation.csv", encoding='gbk')
    course_name = input("请输入课程名称\n")
    try:
        label[course_name]
        # 判断课程是否存在
    except KeyError:
        print("您输入的课程不存在！请按回车确认后返回上一页！")
        input()
        os.system('cls')
        studentStatistics()
        return 0
    finally:
        course_list = label[course_name].to_list()
        print(course_name + "的最大值为： " + str(BasicMath.Max(course_list)) + "\n")
        input("按回车键返回上一页\n")
        os.system('cls')
        studentStatistics()
        return 0
def AllMin():
    label = pd.read_csv("GradeInformation.csv", encoding='gbk')
    course_name = input("请输入课程名称\n")
    try:
        label[course_name]
        # 判断课程是否存在
    except KeyError:
        print("您输入的课程不存在！请按回车确认后返回上一页！")
        input()
        os.system('cls')
        studentStatistics()
        return 0
    finally:
        course_list = label[course_name].to_list()
        print(course_name + "的最小值为： " + str(BasicMath.Min(course_list)) + "\n")
        input("按回车键返回上一页\n")
        os.system('cls')
        studentStatistics()
        return 0
def PerAvg():
    stu_name = input("请输入您要查询的学生姓名\n")
    label = pd.read_csv("GradeInformation.csv", encoding='gbk')
    if (label.index[label['姓名'] == stu_name]).size == 0:
        input("您输入的学生姓名不存在！按回车返回上一页\n")
        studentStatistics()
        return 0
    else:
        dataset = np.delete((label.loc[label.index[label['姓名'] == stu_name]]).values[0], 0)
        print(stu_name+"学生的平均成绩是： "+str(BasicMath.Avg(dataset))+"\n")
        input("按回车键返回上一页\n")
        os.system('cls')
        studentStatistics()
        return 0
def PerMax():
    stu_name = input("请输入您要查询的学生姓名\n")
    label = pd.read_csv("GradeInformation.csv", encoding='gbk')
    if (label.index[label['姓名'] == stu_name]).size == 0:
        input("您输入的学生姓名不存在！按回车返回上一页\n")
        studentStatistics()
        return 0
    else:
        dataset = np.delete((label.loc[label.index[label['姓名'] == stu_name]]).values[0], 0)
        print(stu_name + "学生的最好成绩是： " + str(BasicMath.Max(dataset)) + "\n")
        input("按回车键返回上一页\n")
        os.system('cls')
        studentStatistics()
        return 0
def PerMin():
    stu_name = input("请输入您要查询的学生姓名\n")
    label = pd.read_csv("GradeInformation.csv", encoding='gbk')
    if (label.index[label['姓名'] == stu_name]).size == 0:
        input("您输入的学生姓名不存在！按回车返回上一页\n")
        studentStatistics()
        return 0
    else:
        dataset = np.delete((label.loc[label.index[label['姓名'] == stu_name]]).values[0], 0)
        print(stu_name + "学生的最差成绩是： " + str(BasicMath.Min(dataset)) + "\n")
        input("按回车键返回上一页\n")
        os.system('cls')
        studentStatistics()
        return 0
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
        return 0
    try:
        os.system('cls')
        switch[static_number]()
    except KeyError:
        print("输入不合法，请重新输入")
        input()
        os.system('cls')
        studentStatistics()
        return 0
