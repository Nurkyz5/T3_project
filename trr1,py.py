# l=[8, 6,7, 10, 6, 14, 6, 6, 6, 11, 12, 7, 9, 15, 8, 11, 12, 9, 8, 9]
# mean=sum(l)/len(l)

# px_more9=1-sum([Poisson(i) for i in range(0,10)])
# px_less7=sum([Poisson(i) for i in range(1,7)])
# print(px_less7)

import math


def poisson_pmf(k, lam):
    return math.exp(-lam) * lam**k / math.factorial(k)

lam = 20/6

cdf = 0
for s in range(0, 20):
    cdf += poisson_pmf(s, lam)
    if cdf >= 0.9:
        print("s =", s)
        break

pv=sum([poisson_pmf(i,lam) for i in range(0,7)])
print(pv)


p5=sum([poisson_pmf(i,lam) for i in range(0,6)])
print(p5)
print(1-p5)
print(poisson_pmf(5,lam))
