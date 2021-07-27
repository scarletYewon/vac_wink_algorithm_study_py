def solution(nums):
    answer = 0
    values = len(nums) // 2
    check_list=[]
    for i in nums:
        if i not in check_list:
            check_list.append(i)

    if len(check_list)>values:
        answer=values
    else:
        answer=len(check_list)
    return answer