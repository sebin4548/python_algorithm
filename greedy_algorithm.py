n = int(input())
a,b,c,d,e,f = map(int, input().split())

sum1 = min(a,b,c,d,e,f)
sum2 = min(a+b,a+c,a+d,a+e,b+c,b+d,b+f,c+f,c+e,d+e,d+f,e+f)
sum3 = min(a+b+c,a+b+d, a+c+e, a+d+e, b+c+f,b+d+f,c+f+e,e+d+f)


sum = 0
if n > 2:
    sum = (5 * n * n - 16 * n + 12) * sum1 + \
          (8 * n - 12) * sum2 + \
        4 * (sum3)
elif n == 2:
    sum = 4 * (sum2) + \
              4 * (sum3)

elif n == 1:
    sum = (a+b+c+d+e+f - max(a,b,c,d,e,f))
print(sum)
