from parse import parse


def matrix_to_cli(matrix, size):
    """
    :param matrix: squared adjacency matrix
    :param size: size of @matrix
    :return:
        C L I tuple
    """
    C = []
    L = []
    I = []
    for i in range(size):
        current_row = []
        for j in range(size):

            elem = matrix[i][j]
            if elem == 0:
                continue
            else:
                current_row.append(elem)
                I.append(j)
                C.append(elem)
        if len(current_row) > 0:
            if not L:
                L.append(0)
                L.append(len(current_row))
            else:
                L.append(L[-1] + len(current_row))
    return C, L, I


if __name__ == '__main__':
    file = "../data/corpus2.xml"

    mylist = parse(file)
