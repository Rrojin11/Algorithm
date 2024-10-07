import sys
input = sys.stdin.readline

n = int(input())
d = list(range(100001))

for i in range(4,n+1):
    if int(i**(1/2))**2 == i:
        d[i] = 1
        pass
    tmp = d[i]
    for j in range(1,i//2+1):
        if tmp>d[j]+d[i-j]:
            tmp = d[j]+d[i-j]
    d[i] = tmp 
print(d[n])
