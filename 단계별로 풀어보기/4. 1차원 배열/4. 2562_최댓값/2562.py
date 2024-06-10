n = []

for _ in range(9):
    s = int(input())
    n.append(s)

max = max(n)
loc = n.index(max) + 1

print(max)
print(loc)