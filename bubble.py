
def bubble(unsorted_list):
    n = len(unsorted_list)
    for i in range(n, 0, -1):
        for j in range(i-1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
    return unsorted_list


print(bubble([1, 5, 6, 3, 8, 11, 67, 3, 100, 23, 44, -4]))
