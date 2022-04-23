n = int(input())
lis = []
for _ in range(n):
    temp = input().strip()
    temp1 = []
    for alpha in temp:
        temp1.append(alpha)
    lis.append(temp1)


di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
def dfs(i, j):
    global count
    count += 1
    lis[i][j] = 0
    for _ in range(4):
        ti, tj = i + di[_], j + dj[_]
        if 0 <= ti < m and 0 <= tj < n and lis[ti][tj] == '1':

            dfs(ti, tj)


m = n
count = 0
answer = []
for i in range(m):
    for j in range(n):

        if lis[i][j] == '1':
            if count != 0:
                answer.append(count)
                count = 0
            dfs(i, j)
if count != 0:
    answer.append(count)
print(len(answer))
answer.sort()
for num in answer:
    print(num)

