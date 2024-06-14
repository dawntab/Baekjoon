N, M =  map(int, input().split())
list = [a for a in range(1, N + 1)]
sel_list = []
rev_list = []


for b in range(M):
    i, j = map(int, input().split())
    sel_list = list[i - 1 : j]
    del list[i - 1 : j]
    rev_list = sel_list[::-1]
    for c in range(len(rev_list)):
        list.insert(i - 1, rev_list[c])
        i += 1

print(*list)