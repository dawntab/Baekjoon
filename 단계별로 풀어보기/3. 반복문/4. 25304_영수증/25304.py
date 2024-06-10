sum = int(input())
c = int(input())

sum_count = 0

for i in range(1, c + 1):
    a, b = map(int, input().split())
    sum_count = sum_count + (a * b)

if(sum == sum_count):
    print("Yes")
else:
    print("No")