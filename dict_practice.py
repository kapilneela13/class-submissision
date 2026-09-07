d = {"a": 1, "b": 2}

print(d.get("a"))

print(d.keys())

print(d.values())

print(d.items())

d_copy = d.copy()
print(d_copy)

keys = ["x", "y"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)

val = d.pop("b")
print(val, d)

item = d.popitem()
print(item, d)

d = {"a": 1}
val = d.setdefault("b", 5)
print(val, d)

d.update({"c": 3, "d": 4})
print(d)

d.clear()
print(d)
