from pymonad import curry, State, unit

items = {
    "apples": 70,
    "wine": 300,
    "milk": 80,
    "chips": 100,
}

@curry
def buy(item, customer):
    @State
    def func(total_cost):
        if not item in items:
            return (customer, total_cost)
        cost = items[item]
        if cost > customer["money"]:
            return (customer, total_cost)
        return (
            {
                "items": customer["items"] + [item],
                "money": customer["money"] - cost,
            },
            total_cost + cost)
    return func


initial = lambda money: unit(State, {"items": [], "money": money})

print((initial(2000))(0))
print((initial(2000) >> buy("apples") >> buy("milk") >> buy("apples"))(0))
print((initial(2000) >> buy("car"))(0))
print((initial(200) >> buy("apples") >> buy("wine") >> buy("chips"))(0))
