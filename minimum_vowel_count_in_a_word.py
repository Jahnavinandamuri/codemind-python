a=input()
arr=list(a.split())
vow=list("aeiouAEIOU")
ma=100
for i in arr:
    c=0
    for j in i:
        if j in vow:
            c+=1
    if c<ma:
        ma=c
print(ma)