import sys
import math
input = sys.stdin.readline

n = int(input())
d = list(map(int, input().split()))

for i in range(n):   
    for k in range(math.ceil(i/2)):
        tmp = d[k]+d[i-k-1]       
        if tmp<d[i]:
            d[i]=tmp
print(d[n-1])
