from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lis = []
queue = deque([])

for x in range(m):
    temp_input = [int(x) for x in input().split()]
    for y in range(n):
        if temp_input[y] == 1:
            queue.append([x,y])
    lis.append(temp_input)

dx, dy = [0,0,-1,1], [-1,1,0,0]
ans = 1

while queue:
    ans += 1
    next_queue = deque([])
    for _ in range(len(queue)):
        x,y = queue.popleft()
        for i in range(4):
            temp_x = x + dx[i]
            temp_y = y + dy[i]
            if(0 <= temp_x < m and 0 <= temp_y < n):
                if int(lis[temp_x][temp_y]) == 0:
                    next_queue.append([temp_x,temp_y])
                    lis[temp_x][temp_y] = ans
    queue = next_queue

max_num = 0

for x in lis:
    if 0 in x:
        ans = 0
    max_num = max(max(x), max_num)
if (ans == 0):
    print(-1)
else:
    print(max_num - 1)
