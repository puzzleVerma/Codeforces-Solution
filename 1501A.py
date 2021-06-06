#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for t in range(IN()):
    n=IN()
    arr=[]
    dep=[]
    for i in range(n):
        a,b=LI()
        arr+=[a]
        dep+=[b]
    late=LI()
    if n==1:
        print(arr[0]+late[0])
    extra=late[0]
    for i in range(n-1):
        extra-=min(extra,(dep[i]-arr[i])//2)
        extra+=late[i+1]
    print(arr[n-1]+extra)