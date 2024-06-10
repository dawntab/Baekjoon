H, M = map(int, input().split())

if(H != 0):
    if(M - 45 >= 0):
        print(H, M - 45)
    elif(M - 45 < 0):
        print(H - 1, M + 15)
else:
    if(M - 45 >= 0):
        print(H, M - 45)
    else:
        H = 23
        print(H, M + 15)
    