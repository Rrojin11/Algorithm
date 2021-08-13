#리스트를 문자열로 일정하게 합쳐주기 -> join
#'구분자'.join(리스트)
import sys
num = int(sys.stdin.readline())

for _ in range(num):
    s = sys.stdin.readline().split()
    for i in range(len(s)):
        print(s[i][::-1], end =' ') #파이썬 string뒤집기
    print()