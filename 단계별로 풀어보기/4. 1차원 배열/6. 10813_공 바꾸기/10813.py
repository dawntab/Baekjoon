N, M = map(int, input().split())
N_basket = []

for i in range(N):
    N_basket.append(i + 1)

for j in range(M):
    a, b = map(int, input().split())

    loc_a = a - 1
    loc_b = b - 1    

    N_basket[loc_a], N_basket[loc_b] = N_basket[loc_b], N_basket[loc_a]

for k in range(len(N_basket)):
    print(N_basket[k], end = " ")