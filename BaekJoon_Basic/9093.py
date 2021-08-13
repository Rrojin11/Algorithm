import sys
num = int(sys.stdin.readline())

for _ in range(num):
    s = sys.stdin.readline().split()
    for i in range(len(s)):
        print(s[i][::-1], end =' ') #파이썬 string뒤집기
    print()