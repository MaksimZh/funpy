from pymonad.tools import curry

# 1 -----------------------------------

@curry(2)
def combine(a, b):
    return a + b

hello = combine("Hello, ")

print(hello("Max"))


# 2 -----------------------------------

@curry(4)
def fun(greeting, sep, end, name):
    return f"{greeting}{sep} {name}{end}"

# Важно, чтобы `name` был последним параметром,
# по крайней мере пока мы не знаем
# как выбирать параметр при частичном применении.
final = fun("Hello")(",")("!")
print(final("Petya"))
