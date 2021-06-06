for t in range(int(input())):
    n,m=[int(k) for k in input().split()]
    a=[int(k) for k in input().split()]
    b=[int(k) for k in input().split()]
    if m>sum(a):
        print(-1)
        continue
    imp=[]
    non=[]
    for i in range(n):
        if b[i]==2:
            imp+=[a[i]]
        else:
            non+=[a[i]]
    ans=0
    imp.sort(reverse=True)
    non.sort(reverse=True)
    il=len(imp)
    nl=len(non)
    ii=0
    ni=0
    while m>0:
        if (ni<nl):
            m-=non[ni]
            ni+=1
            ans+=1
        else:
            m-=imp[ii]
            ii+=1
            ans+=2
    fin=ans
    ni-=1
    while ni>=0:
        m+=non[ni]
        ans-=1
        ni-=1
        while m>0 and ii<il:
            m-=imp[ii]
            ii+=1
            ans+=2
        if m>0:
            break
        if ans<fin:
            fin=ans
        
    print(fin)
        