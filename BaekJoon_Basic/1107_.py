target = int(input())
n = int(input())
broken = [False]*10
if n>0:
    a = list(map(int,input().split()))
else:
    a = []
for x in a:
    broken[x]=True

def possible(c):
    if c==0:
        if broken[0]:
            return 0 #이동불가
        else:
            return 1 #이동가능 1번에
    l = 0
    while c>0:
        if broken[c%10]:
            return 0 #불가능
        l+=1
        c//=10
    return l
        

ans = abs(target-100)
for i in range(0,1000000+1):
    c = i
    l = possible(c)
    if l>0: #누룰수 있음
        press = abs(target-c)
        if ans>l+press:
            ans = l+press
print(ans)
        
