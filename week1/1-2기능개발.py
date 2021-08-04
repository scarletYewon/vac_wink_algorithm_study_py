def solution(progresses,speeds):
    answer = []
    day = 0
    distribution = 0

    while len(progresses) > 0:
        if (progresses[0]+day*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            distribution +=1

        else:
            if distribution>0:
                answer.append(distribution)
                distribution=0
            day+=1
    answer.append(distribution)
    return answer
