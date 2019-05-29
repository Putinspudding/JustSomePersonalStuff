import os
import pandas as pd
import numpy as np
import datastruction
def gradeAdd():
    label = pd.read_csv("GradeInformation.csv", encoding='gbk')
    course_name = input("请输入您要增加的学生姓名\n")
    new_label = label.append({'姓名': course_name}, ignore_index=True)
    new_label.to_csv("GradeInformation.csv", encoding='gbk', index=False)
    print("修改成功！\n按回车后返回上一页")
    input()
    os.system('cls')
    studentManagement()
    return 0
def gradeEdit():
    stu_name = input("请输入您要更改的学生姓名\n")
    label = pd.read_csv("GradeInformation.csv", encoding='gbk')
    if (label.index[label['姓名'] == stu_name]).size == 0:
        input("您输入的学生姓名不存在！按回车返回上一页\n")
        studentManagement()
        return 0
    else:
        course_name = input("请输入您要更改的科目名称\n")
        try:
            label[course_name]
        except KeyError:
            print("您输入的课程不存在！请按回车确认后返回上一页！\n")
            input()
            os.system('cls')
            gradeEdit()
            return 0
        finally:
            try:
                grade = float(input("请输入更改后的成绩\n"))
            except:
                print("输入不合法,请按回车后返回上一页\n")
                input()
                os.system('cls')
                studentManagement()
                return 0
            finally:
                label.loc[label.index[label['姓名'] == stu_name], course_name] = grade
                label.to_csv("GradeInformation.csv", encoding='gbk', index=False)
                input("更改成功！按回车返回上一页\n")
                studentManagement()
                return 0
def gradeRemove():
    stu_name = input("请输入您要删除的学生姓名\n")
    label = pd.read_csv("GradeInformation.csv", encoding='gbk')
    if (label.index[label['姓名'] == stu_name]).size == 0:
        input("您输入的学生姓名不存在！按回车返回上一页\n")
        studentManagement()
        return 0
    else:
        new_label = label.drop(label.index[label['姓名'] == stu_name])
        new_label.to_csv("GradeInformation.csv", encoding='gbk', index=False)
        input("删除成功！按回车返回上一页\n")
        studentManagement()
        return 0
def gradeSearch():
    stu_name = input("请输入您要查询的学生姓名\n")
    label = pd.read_csv("GradeInformation.csv", encoding='gbk')
    if (label.index[label['姓名'] == stu_name]).size == 0:
        input("您输入的学生姓名不存在！按回车返回上一页\n")
        studentManagement()
        return 0
    else:
        print((label.loc[label.index[label['姓名'] == stu_name]]).to_string(index=False))
        input("按回车键返回上一页\n")
        os.system('cls')
        studentManagement()
        return 0
def quit():
    datastruction.menu()
def studentManagement():
    switch = {
        1: gradeAdd,
        2: gradeEdit,
        3: gradeRemove,
        4: gradeSearch,
        5: quit
    }
    print("请选择功能：")
    print("1、学生成绩增加")
    print("2、学生成绩修改")
    print("3、学生成绩删除")
    print("4、学生成绩查询")
    print("5、返回上一级")
    try:
        manage_number = int(input())
    except:
        print("输入不合法，请重新输入")
        input()
        os.system('cls')
        studentManagement()
    try:
        os.system('cls')
        switch[manage_number]()
    except KeyError:
        print("输入不合法，请重新输入")
        input()
        os.system('cls')
        studentManagement()
