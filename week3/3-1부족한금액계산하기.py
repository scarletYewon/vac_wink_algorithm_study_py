def solution(price, money, count):
    Sum = 0
    for i in range(1,count+1):
        Sum += price*i
    if Sum >= money:
        answer = Sum -money
    else:
        answer = 0
    return answer