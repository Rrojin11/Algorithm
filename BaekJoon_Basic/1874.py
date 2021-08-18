import sys
'''
* 찾을 문자의 첫번째 위치한 index 출력
find : 찾는 문자가 없을 경우 -1 출력, 문자열만 사용가능
index : 찾는 문자열이 없으면 Value Error, 문자열, 리스트,튜플에서 사용 가능
numpy.where : 여러개 위치할 경우 index 모두 출력 
ex. list를 numpy의 array로 바꾸고 찾기)  np.array(list) >>> np.where(list=='hi)[0]
'''

n = int(sys.stdin.readline())
a = [] # 완성시킬 list
b = list(range(1,n+1)) # 1..n까지 수열
s = [] # 스택
answer = []
check = True
for _ in range(n):
    a.append(int(sys.stdin.readline()))

for i in range(n):
    t = a[i]
    if len(s)==0:
        while(1):
            f = b.pop(0)
            s.append(f)
            answer.append('+')
            if t==f:
                break

    if s[-1]==t: #stack의 top이 현재 원하는 값이면
        s.pop()#스택에서 지우기
        answer.append('-')
    elif s[-1]<t: #스택 top < 현재 원하는 값
        c = b.index(t)
        for _ in range(c+1):
            s.append(b.pop(0))
            answer.append('+')
        s.pop()
        answer.append('-')
    elif s[-1]>t: #스택 top > 현재 원하는 값
        check = False
        break

if check == True:
    for k in answer:
        print(k)
else:
    print('NO')


