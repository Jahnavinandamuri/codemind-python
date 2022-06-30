n=int(input())
a=list(map(int,input().split()))
su=0
for i in range(n):
    su+=a[i]
print(su)