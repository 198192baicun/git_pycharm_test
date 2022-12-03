# -*- coding:utf-8 -*-
# author：LJ
# 日期：2022年12月03日


class Student(object):  # 学生类
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self):  # 魔法函数
        return f"学生信息：{self.id}     {self.name}     {self.age}"


class Student_System(object):  # 学生管理系统类
    def __init__(self):
        self.sys_dict = {}  # 存储学生信息 键：学号   值：学生对象

    def add(self):  # 添加学生信息
        stu_id = input("学号：")
        if stu_id not in self.sys_dict.keys():
            name = input("姓名：")
            age = input("年龄：")
            s = Student(stu_id, name, age)
            self.sys_dict[stu_id] = s  # 添加学生学习 键：学号   值：学生对象

    def find(self):  # 查找所有学生信息
        for i in self.sys_dict.values():
            print(i)  # i是学生对象，但因为在Student类中使用魔法函数 所以不是打印对象地址 而是__str__ 返回的字符串
            print("-" * 50)  # 分割线

    @staticmethod
    def show():  # 显示菜单系统
        print("这是学生系统：\n1、增加学生信息\n2、查找学生信息\n3、退出")

    @staticmethod
    def quit():  # 退出函数
        exit()  # 退出当前程序，并重启shell 还可以使用 quit()

    def start(self):  # 启动程序
        cz_dict = {1: self.add, 2: self.find, 3: self.quit}     # 这是使用字典来简化if
        while True:
            self.show()
            cz = int(input("输入你需要的操作："))
            cz_dict.get(cz)()  # 得到字典的值 使用括号执行函数

            # 使用if做判断进行执行

            # if cz == 1:
            #     self.add()
            # elif cz == 2:
            #     self.find()
            # elif cz == 3:
            #     break
            # else:
            #     print("未知命令")
            #     break


if __name__ == '__main__':
    sys = Student_System()
    sys.start()

