#<<스택>>
#파이썬은 따로 stack 구조 없음 ----> list로 표현
#입출력 속도 비교(faster) : sys.stdin.readline > raw_input() > input()
#리스트 삭제 함수
#1) clear : 리스트 모든 값 삭제 ex. s.clear()
#2) pop : 해당 인덱스 값 삭제 후 삭제한 값 반환 ex. s.pop()  = s.pop(-1)
#3) remove : 해당 요소 검색 후 제일 처음 값 삭제 ex. s.remove('Bob')
#4) del : 해당 인덱스 혹은 범위 삭제 ex. del s[3],  del s[2:5]
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


