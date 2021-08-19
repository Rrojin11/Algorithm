'''
insert(a, b): 리스트의 a번째 위치에 b를 삽입하는 함수
readline()으로 입력 시, rstrip('\n')로 개행문자 삭제
*요소 뒤집기
1) list.reverse() -> 반환값 없음
2) reversed(iterator형 변수) -> reversed객체 반환
'''
import sys
if __name__=='__main__':
    sl = list(sys.stdin.readline().rstrip('\n'))
    sr = list()
    n = int(sys.stdin.readline())
    for _ in range(n):
        i = sys.stdin.readline().split()
        if i[0]=='L' and sl:
            sr.append(sl.pop())
        elif i[0]=='D' and sr:
            sl.append(sr.pop())
        elif i[0]=='B' and sl:
            sl.pop()
        elif i[0]=='P':
            sl.append(i[1])

    print(''.join(sl)+''.join(reversed(sr)))
