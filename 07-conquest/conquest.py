from functools import reduce

conquest_campaign = lambda n, m, battalion: \
    fight(n, m, pairs(battalion), 1)

pairs = lambda a: _pairs(a, set())

def _pairs(source, dest):
    if len(source) == 0:
        return dest
    return _pairs(source[2:], {tuple(source[:2])} | dest)

neighbors = lambda point: {
    point,
    (point[0] - 1, point[1]),
    (point[0] + 1, point[1]),
    (point[0], point[1] - 1),
    (point[0], point[1] + 1),
    }

all_neighbors = lambda points: reduce(
    lambda a, point: a | neighbors(point), points, set())

valid = lambda n, m: lambda pair: \
    pair[0] > 0 and pair[0] <= n and pair[1] > 0 and pair[1] <= m


def fight(n, m, points, count):
    if len(points) == n * m:
        return count
    return fight(n, m, set(filter(valid(n, m), all_neighbors(points))), count + 1)


print(conquest_campaign(3, 4, [2, 2, 3, 4]))
