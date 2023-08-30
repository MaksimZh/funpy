from pymonad import Just, Nothing

put = lambda dl, dr: lambda lr: Just((lr[0] + dl, lr[1] + dr))
stands = lambda max_delta: lambda lr: \
    Just(lr) if abs(lr[0] - lr[1]) <= max_delta else Nothing

to_left = lambda num: lambda lr: Just(lr) >> put(num, 0) >> stands(4)
to_right = lambda num: lambda lr: Just(lr) >> put(0, num) >> stands(4)
banana = lambda lr: Nothing

show = lambda maybe: print("fail" if maybe == Nothing else "OK")

begin = lambda: Just((0, 0))

show(begin() >> to_left(2) >> to_right(5) >> to_left(-2))
show(begin() >> to_left(2) >> to_right(5) >> to_left(-1))
show(begin() >> to_left(2) >> banana >> to_right(5) >> to_left(-1))
