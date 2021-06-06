for t in range(int(input())):
    n=int(input())
    if n%2==1:
        print("YES")
        continue
    while n%2==0:
        n/=2
    if n>1:
        print("YES")
    else:
        print("NO")