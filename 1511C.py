#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


n,q=LI()
nli=LI()
qli=LI()

card=[0]*51

for c,ele in enumerate(nli,1):
    if card[ele]==0:
        card[ele]=c

for ele in qli:
    print(card[ele],end=" ")
    for i in range(1,51):
        if card[i]<card[ele]:
            card[i]+=1
    card[ele]=1
