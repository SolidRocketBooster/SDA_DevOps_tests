# A[0] = -1
# A[1] = 3
# A[2] = -4
# A[3] = 5
# A[4] = 1
# A[5] = -6
# A[6] = 2
# A[7] = 1
A = [-1, 3, -4, 5, 1, -6, 2, 1]
B = [0, 3, -2, 5, -1, -8, 3, 1]

def solution(list_raw):
    list_p_eq = []
    for p in range(0, len(A)+1):
        if sum(list_raw[0:p]) == sum(list_raw[p+1:len(A)+1]):
            list_p_eq.append(p)
    if len(list_p_eq) == 0:
        return -1
    else:
        return list_p_eq


print(solution(A))