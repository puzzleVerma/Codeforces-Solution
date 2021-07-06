#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range

n,k=LI()
s=S()
ref=s[0]*k
for i in range(1,n):
    if (s[i]>s[0]):
        break
    temp=s[:i+1]*(k//i+10)
    ref=min(ref,temp[:k])
# div=[1]
# for i in range(2,int(k**0.5)+1):
#     if k%i==0:
#         div+=[i]
#         if (k//i)!=i:
#             div+=[k//i]
# div+=[k]
# 
# for i in div:
#     if n>=i:
#         ref=min(ref,s[:i]*(k//i))
print(ref)
