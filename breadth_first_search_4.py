import sys
sys.setrecursionlimit(10**9)
rline = sys.stdin.readline
w, h = (int(i) for i in rline().rstrip().split())

di = [1,1,0,0,-1,-1,-1,1]
dj = [1,0,1,-1,0,-1,1,-1]

def dfs(j,i, line,w,h):
		line[j][i] = 0
		for num in range(8):
				x = int(j) + int(di[num])
				y = int(i) + int(dj[num])
				if 0 <= x < h  and 0 <= y < w :
						if line[x][y] == 1:
								dfs(x,y, line,w,h)	
			

answer = []
while (w != 0 or h != 0):
		line = []
		for _ in range(h):
				line.append([int(i) for i in rline().rstrip().split()])
		
		#information about line
		
		cnt = 0
		for i in range(w):
				for j in range(h):
						if line[j][i] == 1:
								dfs(j,i, line, w,h)
								cnt += 1
								
								
		answer.append(cnt)
		
		w, h = (int(i) for i in rline().rstrip().split())

for num in answer:
		print(num)
		
	
