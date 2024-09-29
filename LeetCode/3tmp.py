import sys
num = int(sys.stdin.readline())
s = []
for i in range(num):
    a = sys.stdin.readline().split()
    if a[0]=='push':
        s.append(int(a[1])) #넣기
    elif a[0]=='pop':
        if len(s)==0:
            print(-1)
        else:
            print(s.pop())
    elif a[0]=='size':
        print(len(s))
    elif a[0]=='empty':
        if len(s)==0:
            print(1)
        else:
            print(0)
    elif a[0]=='top':
        if len(s)==0:
            print(-1)
        else:
            print(s[-1])
