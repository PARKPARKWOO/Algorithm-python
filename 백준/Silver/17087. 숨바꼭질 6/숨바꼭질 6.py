import math
n, s = map(int, input().split())
bro = list(map(int, input().split())) # λμ μμΉ
a = []
for i in bro:
    if s > i:
        a.append(s - i)
    else:
        a.append(i - s)
print(math.gcd(*a))