a, b, c = map(int, input().split())

M = 10000
T = 1000
H = 100

if(a == b == c):
    print(M + a * T)
elif(a == b):
    print(T + a * H)
elif(b == c):
    print(T + b * H)
elif(c == a):
    print(T + c * H)
else:
    print(max(a, b, c) * 100)