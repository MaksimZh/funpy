from pymonad.tools import curry

# 1 -----------------------------------

@curry(2)
def tag(name, value):
    return f"<{name}>{value}</{name}>"

print(tag("b", "string"))

bold = tag("b")
italic = tag("i")

print(bold("bold string"))
print(italic("italic string"))


# 2 -----------------------------------

@curry(3)
def tag_a(name, attr, value):
    kv = "".join(f' {k}="{v}"' for k, v in attr.items())
    return f"<{name}{kv}>{value}</{name}>"

print(tag_a("li", {}, "item 23"))
print(tag_a("li", {"class": "list-group"}, "item 23"))
print(tag_a("li", {"class": "list-group", "foo": "boo"}, "item 23"))
