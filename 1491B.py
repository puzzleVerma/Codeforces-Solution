for t in range(int(input())):
    n,u,v=[int(k) for k in input().split()]
    a=[int(k) for k in input().split()]
    if max(a)==min(a):
        print(min(u+v,2*v))
        continue
    re=a[0]-1
    ans=0
    for i in range(1,n):
        if re==0:
            ans+=min(u,v)
            re=10**6+1
        if (a[i]-re)>2:
            re=10**6+1
        if (a[i]-re)<0:
            re=10**6+1
        if a[i]==re:
            re-=1
        if a[i]-re==2:
            re+=1
    if re==10**6+1:
        print(ans)
    else:
        ans+=(min(u,v))
        print(ans)
