#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range


n,m=LI()
s=S()
t=S()
j=0
i=0
sml=[]
big=[]
while (i<n and j<m):
    if s[i]==t[j]:
        sml+=[i]
        j+=1
    i+=1
i=n-1
j=m-1
while (i>-1 and j>-1):
    if s[i]==t[j]:
        big+=[i]
        j-=1
    i-=1
width=0
for i in r(m-1):
    width=max(width,big[m-2-i]-sml[i])
print(width)