def prime(num):
    for i in range(2, int(num**0.5)+1):
        if (num % i) == 0:
            return False
    return True

for t in range(int(input())):
    d=int(input())
    ans=1
    for i in range(ans+d,10**9):
        if prime(i):
            ans*=i
            break
    for i in range(ans+d,10**9):
        if prime(i):
            ans*=i
            break
    print(ans)