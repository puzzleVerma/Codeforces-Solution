for t in range(int(input())):
    n,u,r,d,l=[int(k) for k in input().split()]
    li=[u,r,d,l,u]
    if max(li)<n-1:
        print("YES")
        continue

    newli=[0,0,0,0,0]
    flag=0
    for i in range(4):
        if li[i]==n:
            newli[(i+1)%4]+=1
            newli[(i-1)%4]+=1
        elif li[i]==n-1:
            if (li[(i-1)%4]>li[(i+1)%4]):
                newli[(i-1)%4]+=1
            else:
                newli[(i+1)%4]+=1

    for i in range(4):
        if li[i]<newli[i]:
            print("NO")
            break
    else:
        print("YES")