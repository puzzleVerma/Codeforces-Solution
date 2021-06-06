def jump(i):
    global a
    ans=0
    step=i
    while step<n:
        if a[step]>1:
            ans+=1
            step+=a[step]
        else:
            step+=a[step]
    return ans

def chng(i):
    global a
    step=i
    while step<n:
        if a[step]>1:
            t=step
            step+=a[step]
            a[t]-=1
        else:
            step+=a[step]
    return a


for t in range(int(input())):
    n=int(input())
    a=[int(k) for k in input().split()]
    if n==1:
        print(a[0]-1)
    # pas=0
    # ans=0
    # mxi=0
    # while sorted(a)[-2]>1:
    #     pas+=1
    #     for i in range(n):
    #         if jump(i)>ans:
    #             ans=jump(i)
    #             mxi=i
    #     print(mxi)
    #     print(jump(mxi))
    #     a=chng(mxi)
    #     print(a)
    # pas+=sorted(a)[-1]-1
    # print(pas)
    if sorted(a)[-2]==1:
        print(sorted(a)[-1]-1)
    else:
        print(sorted(a)[-1])
