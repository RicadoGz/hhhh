from collections import namedtuple, deque, Counter

# Create a namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

# Create a deque
d = deque([1, 2, 3])
d.appendleft(0)
print(d)

# Create a Counter
c = Counter('hello world')
print(c)
