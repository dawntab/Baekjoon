num = []
div = []

for i in range(10):
    num.append(int(input()))
    div.append(num[i] % 42)

div_set = set(div)

print(len(div_set))