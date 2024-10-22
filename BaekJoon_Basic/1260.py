import sys
from collections import deque

n,m,v = map(int, input().split())
a = [ [] for _ in range(n+1)]
for _ in range(m):
    s,e = map(int,input().split())
    a[s].append(e)
    a[e].append(s)

check = [False]*(n+1)

for k in range(1,n+1):
    a[k] = sorted(a[k])
def dfs(v):
    check[v]=True
    print(v, end = ' ')
    for i in a[v]:
        if check[i]==False:
            #방문
            dfs(i)

check1 = [False]*(n+1)
dq = deque()
def bfs(v):
    check1[v]=True
    print(v, end=' ')
    dq.append(v)
    while dq:
        k = dq.popleft()
        for i in a[k]:
            if check1[i]==False:
                check1[i]=True
                print(i, end=' ')
                dq.append(i)


dfs(v)
print()
bfs(v)
