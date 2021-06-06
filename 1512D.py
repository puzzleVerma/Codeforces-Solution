#######puzzleVerma#######


import sys
import math
LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()

#######Code Starts here#######
for i in range(IN()):
    n=IN()
    li=LI()
    li=sorted(li)
    sm=0
    flag=0
    for i in range(n+1):
        sm+=li[i]

    diff=int(sm-li[n+1])
    if diff in li[:n+1]:
        li.remove(diff)
    
    elif (sm/2 == li[n]):
        pass        

    else:
        print(-1)
        flag=1
    
    if flag==0:
        for i in range(n):
            print(li[i],end=" ")
        print()

