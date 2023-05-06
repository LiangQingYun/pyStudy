a = [1, 2, 3]
b = ['a', 'b', 'c']
c = [True, False, True]

result = list(zip(a, b, c))
print(result)

for a, b, c in zip(a, b, c):
    print(a, b, c)
