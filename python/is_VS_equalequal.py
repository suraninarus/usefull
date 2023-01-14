"""
==: checks if two values are equal
is: checks the identity, are two values are the same in the memory
"""

a = "cfgh"
b = "cfgh"

if a == b:
    print("== : True")
else:
    print("==: False")

if a is b:
    print("is : True")
else:
    print("is: False")

#======================
def equal(x, y):
    if x == y:
        print("== : True")
    else:
        print("==: False")


def same(x, y):
    if x is y:
        print("is : True")
    else:
        print("is: False")

equal(a, b)
same(a, b)

#======================
l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5]
l3 = l1

if l1 == l2:
    print("l1 == l2:", True)
else:
    print("l1 == l2:", False)

if l1 is l2:
    print("l1 is l2:",True)
else:
    print("l1 is l2:", False)


if l1 == l3:
    print("l1 == l3:", True)
else:
    print("l1 == l3:", False)

if l1 is l3:
    print("l1 is l3:",True)
else:
    print("l1 is l3:", False)


print("a id: ", id(a))
print("b id: ", id(b))
print("l3 id: ", id(l1))
print("l2 id: ", id(l2))
print("l3 id: ", id(l3))