for t in range(int(input())):
    n,k=[int(k) for k in input().split()]
    if k<n:
        k*=(int((n-1)/k)+1)
    print(((k-1)//n)+1)