#######puzzleVerma#######


import sys
import math
from typing import DefaultDict
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range

dd=DefaultDict(int)
dd[0]=0
dd[1]=1
dd[2]=5
dd[5]=2
dd[8]=8

real=[0,1,2,5,8]

def check(th,tm,h,m):
    flag=False
    if ((th//10) in real):
        if ((th%10) in real):
            if ((tm//10) in real):
                if ((tm%10) in real):
                    # print("fgsughbsd")
                    # print(th//10,th%10,tm//10,tm%10)
                    flag=(check2(th,tm,h,m))
                    
    return flag

def check2(th,tm,h,m):
    flag=False
    if (int(10*dd[tm%10]+dd[tm//10])<h):
        if (int(10*dd[th%10]+dd[th//10])<m):
            # print(int(10*dd[tm%10]+dd[tm//10]),h,int(10*dd[th%10]+dd[th//10]),m)
            flag=True
    return flag    

def invert(th,tm):
    newtime=""
    newtime+=str(th//10)
    newtime+=str(th%10)
    newtime+=":"
    newtime+=str(tm//10)
    newtime+=str(tm%10)
    return newtime



for t in r(IN()):
    h,m=LI()
    s=S()
    th=int(s[:2])
    tm=int(s[3:])
    if check(th,tm,h,m)==True:
        newtime=invert(th,tm)
        print(newtime)
        continue

    while not (check(th,tm,h,m)):
        tm+=1
        if tm>=m:
            tm=0
            th+=1
        if th>=h:
            th=0
        
    newtime=invert(th,tm)
    print(newtime)
