from pymonad import curry, Just, Nothing, List

@curry
def add(x, y):
    return x + y

add10 = add * Just(10)

print(add10 & Just(5))
print(add10 & List(3, 4, 5))
