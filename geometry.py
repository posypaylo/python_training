from geom2d import *

l = [Point(i, i*i) for i in range(-5, 6)]

# l = map(lambda i: Point(i, i*i), range(-5, 6)) - не работает

# for i in range(-5, 6):
#     l.append(Point(i, i*i))

l2 = [Point(el.x, -el.y) for el in l]

# for el in l:
#     l2.append(Point(el.x, -el.y))

print(l)
print(l2)

# print(Point(0, 0).distance(Point(3, 4)))
# a = Point(0, 0)
# b = Point(3, 4)
# print(a.distance(b))
# print(a == b)
# print(a == Point(0, 0))

# l1 = [Point(3, 1), Point(0, 0), Point(1, 2)]

# def x(p):
#     return p.x
#
# def y(p):
#     return p.y

# l2 = sorted(l1, key=lambda p: p.x)
# l2 = sorted(l1, key=lambda p: p.distance(Point(0, 0)))
#
# print(l1)
# print(l2)