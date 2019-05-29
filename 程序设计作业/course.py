import os
import datastruction
import pandas as pd
import numpy as np
def courseAdd():
    label = pd.read_csv("GradeInformation.csv", encoding='gbk')
    course_name = input("请输入您要增加的课程名称\n")
    label[course_name] = pd.Series()
    label.to_csv("GradeInformation.csv", encoding='gbk', index=False)
    course()
    return 0
def courseEdit():
    label = pd.read_csv("GradeInformation.csv", encoding='gbk')
    course_name = input("请输入您要修改的课程名称\n")
    try:
        label[course_name]
    except KeyError:
        print("您输入的课程不存在！请按回车确认后返回上一页！")
        input()
        os.system('cls')
        course()
        return 0
    finally:
        edited_name = input("请输入更改后课程名称\n")
        label.rename(columns={course_name: edited_name}, inplace=True)
        print(label)
        label.to_csv("GradeInformation.csv", encoding='gbk', index=False)
        confirm = input("修改成功，是否继续修改？Y/ANY\n")
        if confirm == 'Y':
            courseEdit()
        else:
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
        print("修改成功！\n按回车后返回上一页")
        input()
        os.system('cls')
        course()
        return 0
def courseSearch():
    pass
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
