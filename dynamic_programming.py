import sys
from math import inf
input = sys.stdin.readline

q = int(input())
lis = []
an = [[inf] * (n+1) for n in range(q)]


for _ in range(q):
    lis.append(list(map(int,input().split())))
def a(n,k):
    if an[n][k] != inf:
        return an[n][k]
    else:
        if n == 0:
            an[n][k] = lis[0][0]
            return an[n][k]
        elif k == 0:
            an[n][k] = lis[n][k] + a(n - 1, k)
            return an[n][k]
        elif k == n:
            an[n][k] = lis[n][k] + a(n - 1, k - 1)
            return an[n][k]
        else:
            an[n][k] = max(a(n - 1, k - 1), a(n - 1, k)) + lis[n][k]
            return an[n][k]
candidate = []
for x in range(q):
    candidate.append(a(q - 1, x))
    
print(max(candidate))

