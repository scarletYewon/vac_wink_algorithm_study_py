def solution(citations):
    citations.sort()
    a = len(citations)
    for i in range(a):
        if citations[i] >= a - i:
            return a - i
    return 0
