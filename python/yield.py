
# https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/


# def simplegenerator():
#     yield 1
#     yield 2
#     yield 3
#
# for value in simplegenerator():
#     print(value)


###################################
#
# def nextSquared():
#     i = 1
#     while True:
#         yield i*i
#         i += 1
#
# for num in nextSquared():
#     if num> 100:
#         break
#     print(num)
#
###################################


def getValues():
    yield "hello"
    yield "world"
    yield 123

def example_get_values():
    print(getValues())

#####################################
#
lista = ["Zso", "Zsolti", "Alma", "Annamária", "Gereben", "Hanna", "Johanna"]

def finder(name):
    if len(name) > 5:
        yield name
    # else:
    #     pass

for name in lista:
    print(next(finder(name)))
