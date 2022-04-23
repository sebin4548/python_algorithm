from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
input = stdin.readline

t = int(input())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
answer = []
def dfs(y, x):
		global lis
		lis[y][x] = 0
		for num in range(4):
				b = dy[num] + y
				a = dx[num] + x
				if 0 <= b < n and 0 <= a < m and lis[b][a] == 1:
						dfs(b,a)


for num in range(t): #iterate t times
		count = 0
		m, n, k = map(int, input().split())
		lis = [[0] * m for _ in range(n)]
		for _ in range(k):
				a,b = map(int, input().split())
				lis[b][a] = 1
		for y in range(n):
				for x in range(m):
						if lis[y][x] == 1:
								dfs(y,x)
								count += 1
		answer.append(count)
		
for num in answer:
		print(num)
