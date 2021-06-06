for t in range(int(input())):
    n=int(input())
    tot=n//2020
    n-=(tot*2020)
    if n<=tot:
        print("YES")
    else:
        print("NO")