from functools import reduce

max_rest = lambda source: reduce(
    lambda mr, v: \
        mr if mr[0] == v \
        else (v, mr[1] + [mr[0]]) if mr[0] < v \
        else (mr[0], mr[1] + [v]),
    source,
    (source[0], []))

max2 = lambda source: max_rest(max_rest(source)[1])[0]

print(max2([1, 2, 3, 4, 5]))
print(max2([5, 4, 3, 2, 1]))
print(max2([2, 1, 4, 3, 1, 5, 2]))
print(max2([2, 1, 5, 2, 1, 4, 3]))
print(max2([2, 2, 5, 2, 1, 4, 3]))
