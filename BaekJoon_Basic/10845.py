import sys
n = int(sys.stdin.readline())
if __name__ == '__main__':
    s = []
    for _ in range(n):
        a = sys.stdin.readline().split()
        if a[0]=='push':
            s.append(a[1])
        elif a[0]=='pop':
            if len(s)==0:
                print(-1)
            else:
                print(s.pop(0))
        elif a[0]=='size':
            print(len(s))
        elif a[0]=='empty':
            if len(s)==0:
                print(1)
            else:
                print(0)
        elif a[0]=='front':
            if len(s)==0:
                print(-1)
            else:
                print(s[0])
        elif a[0]=='back':
            if len(s)==0:
                print(-1)
            else:
                print(s[-1])
    #print(s)
