#! /usr/bin/env python3
from pickletools import string1
import string


print("hello,Python")
'''
这是多行注释
'''

var1 = 1
var2 = 2 + 2
print(var2)

# 整数除法返回浮点数型 //
var3 = 13//2
print(var3)

# 幂运算
var4 = 5 ** 2
print(var4)

# 字符串
string1 = 'runoob'
string2 = string1[1]
print(string2)

string3 = string1[1:3]
print(string3)

print("update string :",string3 + 'hello',string2)

print(" 格式化字符串 %s 数组%d",'2',2)

if('u' in string3) :
    print('在')
else :
    print('no')

if('x' not in string3) :
    print('no')
else :
    print('yes')    

para_str = """
        这是个多行的字符串
        啦啦啦
"""
print(para_str)

print(f'{1+1=}')

list = ['1','2','3','4','5','6']
print(list[1])
print(list[1:2])
print(list[:5])

list[2] = 2
print(list)

del list[2]
print(list)


for string in 'runbood' :
    if string == 'r' :
        pass
        print('pass yes')
    else:
        print('no')
    


print(range(1,20,1))

