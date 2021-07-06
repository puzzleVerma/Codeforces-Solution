#######puzzleVerma#######

import sys,os
import sys
import math
from heapq import *
mod = 10**9+7
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
# will print on Console if file I/O is not activated
#if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
 
# inputs template
from io import BytesIO, IOBase


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range


def main():
    n,k,x=LI()
    a=LI()
    a.sort()
    dl=[]
    ans=1
    for i in range(1,n):
        if a[i]-a[i-1]>x:
            heappush(dl,a[i]-a[i-1])
            ans+=1
    ans-=1
    while ans:
        k-=(heappop(dl)-1)//x
        if k>=0:
            ans-=1
        else:
            break
    ans+=1
    print(ans)



# region fastio
 
BUFSIZE = 8192
 
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
 
 
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
#for array of integers
def MI():return (map(int,input().split()))
# endregion
#for fast output, always take string
def outP(var): sys.stdout.write(str(var)+'\n')  
# end of any user-defined functions
 
MOD=10**9+7
mod=998244353
 
# main functions for execution of the program.
 
if __name__ == '__main__':  
    #This doesn't works here but works wonders when submitted on CodeChef or CodeForces 
    main()
