def solution(bridge_length, weight, truck_weights):
    answer = 0
    List = [0] * bridge_length

    while List:
        answer += 1
        List.pop(0)
        if len(truck_weights) != 0:
            if sum(List) + truck_weights[0] <= weight:
                List.append(truck_weights.pop(0))
            else:
                List.append(0)
    return answer