# input: 3, 5
# result: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

def gen_lists(lists, elements):
    out_list = []
    for element_1 in range(lists):
        in_list = []
        for element_2 in range(elements):
            in_list.append(element_2 * element_1)
        out_list.append(in_list)
    return out_list


print(gen_lists(4, 5))


def gen_lists2(lists, elements):
    return [[n_2*n_1 for n_2 in range(elements)] for n_1 in range(lists)]

print(gen_lists2(2, 5))
