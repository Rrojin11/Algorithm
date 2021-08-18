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
# 1..n까지 수열--> 이걸 count로 바꿔보기
count =1
s = [] # 스택
answer = []
check = True

for i in range(n):
    t = int(sys.stdin.readline())
    while count<=t:
        s.append(count)
        answer.append('+')
        count+=1
    if s[-1]==t: #stack의 top == 현재 원하는 값
        s.pop()#스택에서 지우기
        answer.append('-')
    else:
        check = False
        break
if check == True:
    for k in answer:
        print(k)
else:
    print('NO')


