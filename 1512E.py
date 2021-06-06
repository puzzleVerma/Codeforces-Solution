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
    n,l,r,s=LI()
    num=r-l+1
    baki=n-num
    numsum=num*(num+1)//2
    totalsum=n*(n+1)//2
    bakisum=baki*(baki+1)//2
    maxsum=totalsum-bakisum
    if ((s<numsum) or (s>maxsum)):
        print(-1)
        continue
    else:
        permu=[int(i+1) for i in range(n)]
        st=1
        en=n
        cursum=0
        ans=[0 for i in range(n)]
        l-=1
        r-=1
        for i in range(l,r+1):
            ans[i]=st
            st+=1
            cursum+=ans[i]
        if cursum<s:
            for i in range(r,l-1,-1):
                while ((ans[i]<en) and (cursum<s)):
                    ans[i]+=1
                    cursum+=1
                en-=1
        for i in range(l,r+1):
            permu.remove(ans[i])
        for i in range(n):
            if ((i<l) or (i>r)):
                ans[i]=permu.pop()
    print(*ans)