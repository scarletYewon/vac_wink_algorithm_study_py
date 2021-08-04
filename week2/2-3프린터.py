def solution(priorities, location):
    seq = []
    List = []
    for i in range(len(priorities)):
        seq.append(i)
    while len(priorities) != 0:
        if priorities[0] == max(priorities):
            List.append(seq.pop(0))
            priorities.pop(0)
        else:
            seq.append(seq.pop(0))
            priorities.append(priorities.pop(0))

    answer = List.index(location) + 1
    return answer
