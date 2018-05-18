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
"""
"""
    to implement the Lagrange-interpolation
    Ln(x)=Σli(x)*f(xi)  i∈（0，n)
    li(x)=П(x-xj)/(xi-xj) j∈（0，n)&& j!=i
"""

"""
    不足：没有想到怎么输出多项式的表达式，只能直接输出结果
"""

def Lagrange(x_list,y_list,var):
    """
    :param x_list: x取值
    :param y_list: 对应y的取值
    :param var:待求的x值
    :return: 对应的y值
    """
    Lx=0
    n=len(x_list)
    x=var
    for i in range(n):
        temp=y_list[i]
        for j in range(n):
            if j!=i:
                temp=temp*(x-float(x_list[j]))/(float(x_list[i])-float(x_list[j]))
            else:
                continue
        Lx+=temp

    return Lx
def main(x,y,var):
    Lx=Lagrange(x,y,var)
    print(Lx)#out:0.2559999999999998

if __name__ == '__main__':

    x_list=[-2,0,1,2]
    y_list=[17,1,2,17]#y=f(x)
    var=0.6
    main(x_list,y_list,var)

