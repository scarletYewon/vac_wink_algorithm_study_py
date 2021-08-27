def check(list):
    for j in range(len(list) // 2 + 1):
        if list[j] != list[-1 - j]:
            return False
    else:
        return True

N = int(input())
N += 1
N = list(map(int,list(str(N))))

while True:
    for i in range(0,len(N)//2+1):
        if N[i] < N[-1-i]:
            N[-2-i] += 1

        N[-1-i] = N[i]

        for i in range(len(N)-1, -1, -1):
            if N[i] >= 10:
                N[i], N[i - 1] = N[i] % 10, N[i - 1] + N[i] // 10
    if check(N):
        break

for i in N:
    print(i,end="")






