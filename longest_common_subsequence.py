import sys
input = sys.stdin.readline

a = ' ' + input().strip()
b = ' ' + input().strip()


lis = []
for _ in range(len(b)):
	  lis.append([0 for _ in range(len(a))])
for i in range(1, len(b)):
	  for j in range(1, len(a)):
		  if b[i] == a[j]: 
			  lis[i][j] = (lis[i - 1][j - 1]) + 1
		  else:
			  lis[i][j] = max(lis[i - 1][j], lis[i][j - 1])

print(lis[i][j])
