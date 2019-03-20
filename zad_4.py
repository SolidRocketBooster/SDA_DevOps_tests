A = [-1, 3, -4, 5, 1, -6, 2, 1]
B = [0, 3, -2, 5, -1, -8, 3, 1]


def solution(list_raw):
    list_p_eq = []
    for p in range(0, len(list_raw)):
        if sum(list_raw[0:p]) == sum(list_raw[p+1:len(list_raw)]):
            list_p_eq.append(p)
    if len(list_p_eq) == 0:
        return -1
    else:
        return list_p_eq


print(solution(A))
print(solution(B))
