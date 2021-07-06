#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range

def sm(arr , n):
    ans = 0
    for i in range(0, n):
        ans = ans + arr[i]
    return int(ans * math.pow(2, n - 1))



for t in r(IN()):
    n=IN()
    li=LI()
    if n<3:
        print(0)
        continue
    li.sort()
    ans=li[-1]
    diff=[0]*n
    for i in range(1,n):
        dif=li[i]-li[i-1]
        diff[i]=dif
    temp=0
    for i in range(1,n):
        temp+=((i)*(diff[i]))
        ans-=temp
    print(ans)

    # smo=sum(diff)
    # sma=sm(diff,len(diff))
    # print(smo-sma)
    
