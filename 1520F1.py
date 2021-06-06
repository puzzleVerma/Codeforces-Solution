#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range

n,t=LI()
k=IN()
st=1
en=n

while en>st:
    mid=(en+st)//2
    print("?",1,mid,flush=True)
    ans=int(input())
    ans=mid-ans
    if ans>=k:
        en=mid
    else:
        st=mid+1
print("!",st,flush=True)
sys.exit()