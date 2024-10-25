from bisect import bisect_left, bisect_right

#프로그래머스 가사검색x
def solution(words, queries):
    answers = []
    array = [[] for _ in range(10001)]
    array_r = [[] for _ in range(10001)]
    check = [False for _ in range(10001)]
    check_r = [False for _ in range(10001)]
    
    for w in words:
        array[len(w)].append(w)
        array_r[len(w)].append(w[::-1])
            
    for q in queries:
        
        if q[0]!='?':
            if not check[len(q)]:
                array[len(q)].sort()
                check[len(q)] = True
            left = bisect_left(array[len(q)], q.replace('?','a')) #doaaa
            right = bisect_right(array[len(q)], q.replace('?','z')) #dozzz
        else:
            if not check_r[len(q)]:
                array_r[len(q)].sort()
                check_r[len(q)] = True
            left = bisect_left(array_r[len(q)], q[::-1].replace('?','a')) #aaado
            right = bisect_right(array_r[len(q)], q[::-1].replace('?','z')) #zzzdo
            
        answers.append(right-left)
    return answers
