from functools import reduce

pairs = lambda s: zip(s[::2], s[1::2])
pairs_dist = lambda s: reduce(
    lambda at, st: (at[0] + st[0] * (st[1] - at[1]), st[1]),
    s, (0, 0))[0]
dist = lambda s: pairs_dist(pairs(s))

print(dist([10, 1, 20, 2]))
print(dist([15, 1, 25, 2, 30, 3, 10, 5]))
