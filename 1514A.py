#######puzzleVerma#######


import sys
import math
LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for i in range(IN()):
    n=IN()
    a=LI()
    for ele in a:
        flag=0
        for i in range(1,int(ele**0.5)+1):
            if ((ele%i==0) and (ele//i==i)):
                flag=1
                break
        if flag==0:
            break

    if flag==0:
        print("YES")
    else:
        print("NO")