# -*- coding: cp949 -*-

class Calc:
    def sum(self, a, b):
        result = a+b
        print("{0:d} + {1:d} = {2:d} �Դϴ�.".format(a,b,result))
    def sub(self, a, b):
        result = a-b
        print("{0:s} - {1:s} = {2:s} �Դϴ�.".format(a,b,result))
    def mul(self, a, b):
        result = a*b
        print("{0:s} * {1:s} = {2:s} �Դϴ�.".format(a,b,result))
    def div(self, a, b):
        result = a/b
        print("{0:s} / {1:s} = {2:s} �Դϴ�.".format(a,b,result))
