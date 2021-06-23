# /usr/bin/env python3
# -*- charset: utf-8 -*-

# @Author: yangqixin
# @TIME: 2021/6/18 08:38
# @FILE: 静态方法和类方法.js
# @Email: 958292256@qq.com


class Parent:
    name = 'Parent class name'
    age = 'Parent class age'

    def __init__(self):
        self.name = 'Parent instance name',
        self.age = 'Parent instance age'

    @staticmethod
    def say_name():
        return print(Parent.name)

    @classmethod
    def say_age(cls):
        return print(cls.age)


class Child(Parent):
    name = 'Child name'
    age = 'Child age'

    def __init__(self):
        super().__init__()
        self.name = 'Child instance name'
        self.age = 'Child instance age'

    @staticmethod
    def say_name():
        return print(Child.name)

    @classmethod
    def say_age(cls):
        return print(cls.age)


p = Parent()
Parent.say_name()  # Parent class name
Parent.say_age()  # Parent class age
p.say_name()  # Parent class name
p.say_age()  # Parent class age
c = Child()
c.say_name()  # Child name
c.say_age()  # Child age
Child().say_name()  # Child name
Child().say_age()  # Child age
