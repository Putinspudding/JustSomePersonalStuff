import os
import datastruction
import pandas as pd
import numpy as np
def courseAdd():
    label = pd.read_csv("GradeInformation.csv", encoding='gbk')
    course_name = input("请输入您要增加的课程名称\n")
    if course_name in label.columns.tolist():
        input("该课程已经存在！按回车返回上一页\n")
        course()
        return 0
    label[course_name] = pd.Series()
    label.to_csv("GradeInformation.csv", encoding='gbk', index=False)
    # 在GradeInformation.csv中增加课程
    sub_label = pd.read_csv("subject.csv", encoding='gbk')
    course_credict = input("请输入课程学分\n")
    course_time = input("请输入课程学时\n")
    sub_label.loc[0, course_name] = course_credict
    sub_label.loc[1, course_name] = course_time
    sub_label.to_csv("subject.csv", encoding='gbk', index=False)
    # 在subject.csv中增加课程相关信息
    input("课程增加成功！按回车键返回上一页")
    course()
    return 0
def courseEdit():
    label = pd.read_csv("GradeInformation.csv", encoding='gbk')
    course_name = input("请输入您要修改的课程名称\n")
    try:
        label[course_name]
        # 判断课程是否存在
    except KeyError:
        print("您输入的课程不存在！请按回车确认后返回上一页！")
        input()
        os.system('cls')
        course()
        return 0
    finally:
        edited_name = input("请输入更改后课程名称\n")
        label.rename(columns={course_name: edited_name}, inplace=True)
        #print(label)
        label.to_csv("GradeInformation.csv", encoding='gbk', index=False)
        # 在GradeInformation.csv中更改课程名称
        sub_label = pd.read_csv("subject.csv", encoding='gbk')
        sub_label.rename(columns={course_name:edited_name}, inplace=True)
        course_credict = input("请输入课程学分\n")
        course_time = input("请输入课程学时\n")
        sub_label.loc[0, course_name] = course_credict
        sub_label.loc[1, course_name] = course_time
        sub_label.to_csv("subject.csv", encoding='gbk', index=False)
        # 在subject.csv中更改课程相关信息
        input("修改成功！按回车键返回上一页")
        course()
        return 0
def courseRemove():
    course_name = input("请输入您要删除的课程名称\n")
    label = pd.read_csv("GradeInformation.csv", encoding='gbk')
    try:
        new_label = label.drop(columns=[course_name])
    except:
        print("您输入的课程不存在！请按回车确认后返回上一页！")
        input()
        os.system('cls')
        course()
        return 0
    finally:
        new_label.to_csv("GradeInformation.csv", encoding='gbk', index=False)
        # 删除GradeInformation.csv中的课程
        sub_label = pd.read_csv("subject.csv", encoding='gbk')
        new_sub_label = sub_label.drop(columns=[course_name])
        new_sub_label.to_csv("subject.csv", encoding='gbk', index=False)
        # 删除subject.csv中的课程
        print("修改成功！\n按回车后返回上一页")
        input()
        os.system('cls')
        course()
        return 0
def courseSearch():
    sub_label = pd.read_csv("subject.csv", encoding='gbk')
    course_name = input("请输入您要查询的课程名称\n")
    try:
        sub_label[course_name]
    except KeyError:
        print("您输入的课程不存在！请按回车确认后返回上一页！")
        input()
        os.system('cls')
        course()
        return 0
    finally:
        sub_list = sub_label[course_name].to_list()
        print("课程名："+course_name+"\n学分："+str(sub_list[0])+"\n学时:"+str(sub_list[1]))
        input("按回车键返回上一页\n")
        os.system('cls')
        course()
        return 0
def quit():
    os.system('cls')
    datastruction.menu()
def course():
    switch = {
        1: courseAdd,
        2: courseEdit,
        3: courseRemove,
        4: courseSearch,
        5: quit
    }
    print("请选择功能：")
    print("1、课程增加")
    print("2、课程修改")
    print("3、课程删除")
    print("4、课程查询")
    print("5、回到上一级")
    try:
        coursechosen = int(input())
    except:
        print("输入不合法，请重新输入")
        input()
        os.system('cls')
        course()
    try:
        switch[coursechosen]()
    except KeyError:
        print("输入不合法，请重新输入")
        input()
        os.system('cls')
        course()
