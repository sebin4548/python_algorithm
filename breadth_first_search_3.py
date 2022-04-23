import sys
rline = sys.stdin.readline
n,m = (int(i) for i in rline().rstrip().split())
dx = [1,-1,0,0]
dy = [0,0, 1, -1]


line = []
for _ in range(n):
		line.append([i for i in rline().rstrip()])
		#information about line

index = 0
frontier = [(0,0)]
parent = {(0,0) : None}

while frontier:
		next = []
		index += 1
		for spot in frontier:
				(x,y) = spot
				for num in range(4):
						nx = x + dx[num]
						ny = y + dy[num]
						
						if 0 <= nx < n and 0 <= ny < m :
								if line[nx][ny] == '1' and (nx, ny) not in parent:
										
										next.append((nx, ny))
										parent[(nx,ny)] = (x, y)
		if (n - 1, m - 1) in parent:
				break
		frontier = next
print(index + 1)
