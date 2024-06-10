H, M = map(int, input().split())
U = int(input())

M = M + U

if(M / 60 != 0):
    H = H + (int(M / 60))
    M = M % 60
    if(H == 24):
        H = 0
        print(H, M)
    elif(H > 24):
        H = H - 24
        print(H, M)
    else:
        print(H, M)
else:
    print(H, M)