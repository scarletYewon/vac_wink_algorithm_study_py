import heapq
import sys

f = sys.stdin.readline
n = int(f())
sum_list = []
for i in map(int, f().split()):
    heapq.heappush(sum_list, i)
for i in range(1,n):
    a = list(map(int, f().split()))
    for j in range(n):
        if a[j] > sum_list[0]:
            heapq.heappush(sum_list, a[j])
            heapq.heappop(sum_list)
print(sum_list[0])