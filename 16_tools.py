cash_f = {}
cash_g = {}
import sys

sys.setrecursionlimit(4000)

def f(x):
    tmp = cash_f.get(x)
    if cash_f.get(x):
        return tmp

    if x > 18:
        tmp = x
    else:
        tmp = 3 * f(x + 1) + x + 8

    cash_f[x] = tmp
    return tmp

def g(x):
    tmp = cash_g.get(x)
    if cash_g.get(x):
        return tmp

    tmp = f(x - 1) + g(x - 1)

    cash_g[x] = tmp
    return tmp

#ans = [f(i) for i in range(1, 100 + 1) if f(i) > 100]
#print(len(ans))
#print(sum([int(i) for i in str(f(2))]))
print(f(9))