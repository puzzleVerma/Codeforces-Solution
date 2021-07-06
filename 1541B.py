#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range


for t in r(IN()):
    n=IN()
    arr=LI()
    index={}
    ans=0
    for i in range(n):
        index[arr[i]]=i+1
    arr.sort()
    for i in range(n):
        for j in range(i+1,n):
            pro=arr[i]*arr[j]
            if (pro<(2*n)):
                ind=index[arr[i]]+index[arr[j]]
                if ind==pro:
                    ans+=1

            else:
                break
    print(ans)
