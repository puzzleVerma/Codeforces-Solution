#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range


n=IN()
print("?",1,n,flush=True)
ans=IN()
if n==2:
    if ans==2:
        print("!",1,flush=True)
    else:
        print("!",2,flush=True)
    sys.exit()
if (ans==1):
    a=ans-1
elif (ans==n):
    a=ans
else:
    print("?",1,ans,flush=True)
    a=IN()
if a==ans:
    st=1
    en=ans
    while en-st>1:
        mid=(st+en)//2
        # if mid==ans:
        #     print("!",ans-1,flush=True)
        #     sys.exit()
        # if mid==st:
        #     print("?",en,ans,flush=True)
        #     a=IN()
        #     if a==ans:
        #         print("!",en,flush=True)
        #     else:
        #         print("!",st,flush=True)
        #     sys.exit()
        print("?",mid,ans,flush=True)
        a=IN()
        if a==ans:
            st=mid
        else:
            en=mid-1
    if en==ans:
        print("!",st,flush=True)
        sys.exit()
    if en==(st+1):
            print("?",en,ans,flush=True)
            a=IN()
            if a==ans:
                print("!",en,flush=True)
            else:
                print("!",st,flush=True)
            sys.exit()
    print("!",en,flush=True)

else:
    st=ans
    en=n
    while en-st>1:
        mid=(st+en)//2
        # if mid==ans:
        #     print("!",ans+1,flush=True)
        #     sys.exit()
        # if mid==st:
        #     print("?",ans,st,flush=True)
        #     a=IN()
        #     if a==ans:
        #         print("!",st,flush=True)
        #     else:
        #         print("!",en,flush=True)
        #     sys.exit()
        print("?",ans,mid,flush=True)
        a=IN()
        if a==ans:
            en=mid
        else:
            st=mid+1
    if st==ans:
        print("!",en,flush=True)
        sys.exit()
    if en==(st+1):
            print("?",ans,st,flush=True)
            a=IN()
            if a==ans:
                print("!",st,flush=True)
            else:
                print("!",en,flush=True)
            sys.exit()
    print("!",st,flush=True)
sys.exit()