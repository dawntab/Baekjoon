N, M = map(int, input().split())
N_basket = []

for a  in range(N):
    N_basket.append(0)

for b in range(M):
    i, j, k = map(int, input().split())

    for c in range(i - 1, j):
        N_basket[c] = k

for d in range(len(N_basket)):
    print(N_basket[d], end = " ")