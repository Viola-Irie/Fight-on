# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 12:32:07 2020

@author: Syd
"""
# 第一种方法：不对 因为数组的索引必须是整数
# x=1234554321
# i=0
# if x>0:
#     a=len(str(x))
#     if a%2==0:
#         b=a/2
#         while i<=b:
#             if str(x)[b+i]==str(x)[b-1-i]:
#                         i+=1
#             else:
#                 print("false")
            
#     if a%2!=0:
#         b=(a-1)/2
            
# if x<0:
#     print("false")

# 第二种方法
x=120111021
if x>0:
    a=len(str(x))
    while a>=3:
        left=x//(10**(a-1))
        right=x%10
        if left==right:
            x=(x-left*(10**(a-1)))//10
            a-=2
        else:
            print("wrong")
            break
    if a==1:
        print("yes!")
    elif a==2:
        left=x//(10**(a-1))
        right=x%10
        if left==right:
            print("yes!")
elif x<0:
    print("wrong")
        

