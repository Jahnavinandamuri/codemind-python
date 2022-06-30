import math
def isperfect(c):
    if c>0:
        sr=int(math.sqrt(c))
        return(sr*sr==c)
    return false
n=int(input())
a=list(map(int,input().split()))
su=0
for i in range(n):
    if isperfect(a[i]):
        su+=a[i]
print(su)