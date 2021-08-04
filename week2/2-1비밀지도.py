def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        bit = bin(arr1[i] | arr2[i])[2:].zfill(n)
        msg = ""
        for j in range(n):
            if int(bit[j]) == 1:
                msg += "#"
            else:
                msg += " "
        answer.append(msg)
    print(answer)

    return answer