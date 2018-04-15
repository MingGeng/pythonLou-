numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = [x for x in numbers if x % 2 == 0]

print(a)

b = [x * x for x in numbers]
print(b)

f = filter(lambda x: x % 2 == 0, numbers)
m = map(lambda x: x * x, numbers)

print(f)
print(b)
