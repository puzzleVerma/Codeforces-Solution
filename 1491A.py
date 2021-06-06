n,r=[int(k) for k in input().split()]
a=[int(k) for k in input().split()]
z=0
o=0
for ele in a:
    if ele==0:
        z+=1
    else:
        o+=1
for i in range(r):
    t,x=[int(k) for k in input().split()]
    if t==1:
        if a[x-1]==0:
            a[x-1]=1
            z-=1
            o+=1
        else:
            a[x-1]=0
            z+=1
            o-=1
    if t==2:
        if x<=o:
            print(1)
        else:
            print(0)
