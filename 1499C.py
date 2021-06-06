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
    cn=LI()
    om=cn[1]
    em=cn[0]
    oamt=n*om
    eamt=n*em
    amt=oamt+eamt
    for i in range(2,n):
        if (i%2):
            if cn[i]<om:
                ob=i//2
                obk=n-ob
                oamt-=(obk*(om-cn[i]))
                om=cn[i]
            else:
                oamt+=(cn[i]-om)
        else:
            if cn[i]<em:
                eb=i//2
                ebk=n-eb
                eamt-=(ebk*(em-cn[i]))
                em=cn[i]
            else:
                eamt+=(cn[i]-em)
        amt=min(amt,oamt+eamt)
        # print(amt,eamt,oamt)
        if (em==1 and om==1):
            break
    print(amt)

