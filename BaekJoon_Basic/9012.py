import sys
num = int(sys.stdin.readline())
for _ in range(num):
    s=sys.stdin.readline()
    n = len(s)-1
    tmp = []
    b = True
    for i in range(n):

        if s[i]=='(':
            tmp.append('(')
        else:#')'
            if len(tmp)==0:
                b= False
                break
            else:
                tmp.pop()
    if len(tmp)>0:
        b=False
    if b == True:
        print("YES")
    else:
        print("NO")

