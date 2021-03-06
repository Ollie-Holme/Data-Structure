s = {43, 95, 24, 21, 9, 19, 69, 94, 16}
print("Current Set: ", end = "")
print(s)

# len(s)
# return the number of elements in set [s]
print("The length of set is ", end = "")
print(len(s))

# x in s
# test [x] for membership in [s]
print("24 is in s, ", end = "")
print(24 in s)

# x not in s
# test [x] for non-membership in [s]
print("31 is not in s, ", end = "")
print(31 not in s)

# isdisjoint(other)
# return True if the set has no elements in common with [other]
o = {}
print("s is disjoint with o, ", end = "")
print(s.isdisjoint(o))

# issubset(other)
# set <= other
# test whether every element in the [set] is in the [other]
sub = {95, 9, 19}
print("sub is subset of s, ", end = "")
print(sub.issubset(s), end = ", ")
print(sub <= s)

# set > other
# test whether the [set] is a proper superset of [other]
print("set is proper superset of sub, ", end = "")
print(s > sub)

# union(*other)
# set | other | ...
# return a new set with elements from the set and all [others]
un1 = {95, 24, 1}
un2 = {94, 16, 3}
print("The union of s, un1, and un2 is: ", end = "")
print(s.union(un1, un2))
print(s | un1 | un2)

# intersection(*other)
# set & other & ...
# return a new set with elements common to the set and all [others]
in1 = {43, 95, 24}
in2 = {24, 21, 9}
print("The intersection of s, in1, and in2 is: ", end = "")
print(s.intersection(in1, in2))
print(s & in1 & in2)

# difference(*other)
# set - other - ...
# return a new set with elements in the set that are not in the [others]
dif1 = {24, 21, 9}
dif2 = {19, 69, 94, 16}
print("The difference of s, dif1, and dif2 is: ", end = "")
print(s.difference(dif1, dif2))
print(s - dif1 - dif2)

# symmetric_difference(other)
# set ^ other
# return a new set with elements in either the set or [other] but not both
sym = {95, 24, 21, 13}
print("The symmetric_difference of s and sym is: ", end = "")
print(s.symmetric_difference(sym))
print(s ^ sym)

# copy()
# return a new set with a shallow copy of s
copy = s.copy()
print("Copy Set: ", end = "")
print(copy)

# update(*others)
# set |= other | ...
# update the set, adding elements form all [others]
up1 = {49, 29, 71}
up2 = {26, 37, 21}
s.update(up1, up2)
# s |= up1 | up2
print("The updated set is: ", end = "")
print(s)

# intersection_update(*others)
# set &= other & ...
# update the set, keeping only elements found in it and all [others]
inup1 = {21, 9, 19, 69, 94}
s.intersection_update(inup1)
# s &= inup1
print("The intersection updated set is: ", end = "")
print(s)

# difference_update(*others)
# set -= other | ...
# update the set, removing elements found in [others]
difup1 = {69, 94}
s.difference_update(difup1)
# s -= difup1
print("The difference updated set is: ", end = "")
print(s)

# symmetric_difference_update(other)
# set ^= other
# update the set, keeping only elements found in either set, but not in both
symup1 = {19, 21}
s.symmetric_difference_update(symup1)
# s ^= symup1
print("The symmetric difference updated set is: ", end = "")
print(s)

# add(elem)
# add element [elem] to the set
s.add(13)
print("Current Set: ", end = "")
print(s)

# remove(elem)
# remove element [elem] from the set
s.remove(9)
print("Current Set: ", end = "")
print(s)

s = {79, 37, 62, 11, 17}
print("Current Set: ", end = "")
print(s)

# discard(elem)
# remove element [elem] from the set if it is present
s.discard(62)
print("Current Set: ", end = "")
print(s)

# pop()
# remove and return an arbitrary element from the set
p = s.pop()
print("The popped element in s is: ", end = "")
print(p)
print("Current Set: ", end = "")
print(s)

# clear()
# remove all elements from the set
s.clear()
print("Current Set: ", end = "")
print(s)