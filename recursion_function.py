num = int(input())

def f(n):
		if n == 1:
				return 1
		return 2 * f(n - 1) + 1
		
print(f(num))

def path(n,way):
		if n == 1:
				return [way]
		else:
				if way == '1 3':
						return path(n - 1,'1 2') + [way] + path(n - 1,'2 3')
				elif way == '1 2':
						return path(n - 1,'1 3') + [way] + path(n - 1,'3 2')
				elif way == '3 2':
						return path(n - 1,'3 1') + [way] + path(n - 1,'1 2')
				elif way == '3 1':
						return path(n - 1,'3 2') + [way] + path(n - 1,'2 1')
				elif way == '2 1':
						return path(n - 1,'2 3') + [way] + path(n - 1,'3 1')
				elif way == '2 3':
						return path(n - 1,'2 1') + [way] + path(n - 1,'1 3')

lis = (path(num,'1 3'))
for st in lis:
		print(st)
