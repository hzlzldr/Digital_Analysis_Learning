#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = lanzili
__mtime__ = '2018/4/18'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓   ┏┓
            ┏┛┻━━━┛┻┓
            ┃   ☃    ┃
            ┃ ┳┛  ┗┳ ┃
            ┃   ┻    ┃
            ┗━┓    ┏━┛
              ┃    ┗━━━┓
              ┃  神兽保佑 ┣┓
              ┃  永无BUG！ ┏┛
              ┗┓┓┏━┳┓┏┛
               ┃┫┫ ┃┫┫
               ┗┻┛ ┗┻┛

Pycharm多行注释解注释：按快捷键Ctrl + /
Pycharm多行注释解注释：按快捷键Ctrl + /
Pycharm多行注释解注释：按快捷键Ctrl + /

"""

"""
    aitken迭代算法的实现
"""
import time


def dest_func(x):
    return pow(x,2)-6*x+3==0

def iter__func(x):
    return float((pow(x,2)+3)/6)


def normal_iter():
    k=0
    x=iter__func(initial_value)
    result_array.append(initial_value)
    result_array.append(x)
    while  abs(float(result_array[k+1])- float(result_array[k]))>precision_value:
        if dest_func(result_array[k]):
            return result_array[k]

        else:
            k=k+1
            result_array.append(iter__func(result_array[k]))

    return result_array[-1]

def aitken_iter():
    k=0
    y=iter__func(initial_value)
    z=iter__func(y)
    if z-2*y+initial_value==0:
        return initial_value
    x=initial_value-((pow((y-z),2))/(z-2*y+initial_value))

    result_array.append(initial_value)
    result_array.append(x)

    while abs(float(result_array[k+1])- float(result_array[k]))>precision_value:
        k=k+1
        y=iter__func(result_array[k])
        z=iter__func(y)

        if z-2*y+result_array[k]==0:
            return result_array[k]

        x=result_array[k]-((pow((y-z),2))/(z-2*y+result_array[k]))
        result_array.append(x)

    return result_array[-1]

if __name__=="__main__":
    print("hello world")

    start=time.time()
    k=0
    while k<10000:
        initial_value = 2.5
        precision_value = 0.000000000000000000000001
        result_array = list()
        normal_iter()
        k+=1

    end=time.time()

    #print(result_array)
    print(end-start)

    start=time.time()
    k=0
    while k<10000:
        initial_value = 2.5
        precision_value = 0.000000000000000000000001
        result_array = list()
        aitken_iter()
        k+=1

    end=time.time()
    print(end-start)
    #print(result_array)
