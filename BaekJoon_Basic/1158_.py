import sys
if __name__=='__main__':
    n,k = map(int, sys.stdin.readline().split())
    k = k-1
    a = list(range(1,n+1))
    cur = 0
    ans = []
    for _ in range(n):
        s = len(a)
        t = (cur+k)%s
        ans.append(str(a.pop(t)))
        cur = t

    print('<',end='')
    print(', '.join(ans),end = '')
    print('>')
