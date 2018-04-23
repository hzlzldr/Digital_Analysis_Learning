#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = lanzili
__mtime__ = '2018/4/23'
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

when I wrote this,only God and I understood what I was doing.
Now,God only knows.

"""
"""
    to implement the Newton Interpolation 
    Nn(x)=f(X0)+f[X0,X1](X-X0)+f[X0,X1,X2](X-X0)(X-X1)+...+f[X0,X1,X2,...,Xn](X-X0)(X-X1)..(X-Xn-1)
    Nn+1(x)=Nn(x)+f[X0,X1,X2,...Xn-1,Xn](X-X0)(X-X1)(X-X2)...(X-Xn-1)(X-Xn)
    
    牛顿插值法相较于拉格朗日插值的有点在于，更高的阶可以由低阶推演出来，从而不会浪费之前的运算
    
    f[X0,X1,X2,...，Xn)=Σ(f(Xi)П(1/Xi-Xj) i∈(0,k),j∈(0,k)&&j!=i
    
    f[X0,X1，X2,X3,...Xn-1,Xn]=Σf(Xi)П(1/xi-xj) i∈（0，k),j∈（0，k)&&j!=i
    
"""

def Difference_quotient(x_list,y_list,n,init=0):
    """
    to computer the Difference quotient
    :param x_list:x的取值
    :param y_list:对应y的取值
    :param n:阶数
    :param init:从整个数据值选部分数值的第一个起始位置
    :return: 对应的差商值
    """
    x=x_list
    y=y_list
    if n>len(x_list):
        print("please enter the 3th parameter less than  %d",n)
        return None

    result=0
    for i in range(n+1):
        fx=float(y_list[i+init])
        temp=1
        for j in range(n+1):
            if j!=i:
                temp*=pow((float(x_list[i+init])-float(x_list[j+init])),-1)#最好是不用除法，容易出现误差！！！
            else:
                continue

        result+=fx*temp
    
    return result

def Newton_interpolation(x_list,y_list,var_value,n,init=0):
    """
    :param x_list:x的取值
    :param var_value:待求的x的取值
    :param n:插值多项式的阶数
（卧槽，岂不是还可以加一个间隔）
    :return: 待求点再对应n阶多项式下的值
    """
    xlst=x_list
    ylst=y_list
    x=var_value
    if n>len(xlst)-1:
        n=len(xlst)
        print("please enter the 4th parameter less than len %d",n-1)


    Nx=0
    for i in range(n+1):
        Diff=Difference_quotient(x_list,y_list,i,init)
        temp=1
        for j in range(i):#这里会默认取值是从第一值开始的，若运用从第二个数值开始的4个值计算出来的插值与这个不同
            temp*=(x-float(xlst[j+init]))
        Nx+=temp*Diff

    return Nx


def main():
    x_list=[1,2,3,5,6]
    y_list=[0,2,6,20,90]
    result=Newton_interpolation(x_list,y_list,3.5,3,1)#out:3.125
    result = Newton_interpolation(x_list, y_list, 3.5, 3, 0)  # out:8.75
    result = Newton_interpolation(x_list, y_list, 3.5, 4)  # out:5.9375
    print(result)



if __name__ == '__main__':
    main()
