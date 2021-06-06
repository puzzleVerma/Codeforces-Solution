#######puzzleVerma#######


import sys
import math
LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for i in range(IN()):
    n,m=LI()
    mli=[]
    tli=[]
    for ii in range(n):
        tl=LI()
        mli.append(tl)
        tli+=tl
    mnli=sorted(tli)[:m]
    vis=[(i) for i in range(m)]
    # print(mnli)
    skip=[]
    while(mnli!=[]):
        flag=1
        for nnn in range(n):
            li=mli[nnn]
            if flag==0:
                break
            for nn in range(m):
                if ((li[nn] in mnli) and ([nnn,nn] not in skip)):
                    # print("hfso",nn)
                    if nn in vis:
                        # print("fsygfs",li[nn])
                        vis.remove(nn)
                        mnli.remove(li[nn])
                        flag=0
                        skip.append([nnn,nn])
                        break
                        
                    else:
                        # print("sgffsf",li[nn])
                        mndel=li[nn]
                        skind=vis[0]
                        temp=li[vis[0]]
                        li[vis[0]]=li[nn]
                        li[nn]=temp
                        vis.remove(vis[0])
                        mnli.remove(mndel)
                        flag=0
                        skip.append([nnn,skind])
                        break
            
    for iii in range(n):
        for ele in mli[iii]:
            print(ele,end=" ")
        print()


