"""merge dict
using for loop"""
a = {"a": 1, "b": 2, "c": 3}
b = {"d": 4, "e": 5, "f": 8}
result = {}
all_keys, all_values = list(a.keys())+list(b.keys()), list(a.values())+list(b.values())
for key, value in zip(all_keys, all_values):
    result.update({key: value})
print(result)
# a for loop on list
