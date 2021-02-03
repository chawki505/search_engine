from parse import pages_to_cli


def error(pi, pre_pi):
    c = 0
    for el1, el2 in zip(pi, pre_pi):
        c += abs(el2 - el1)
    return c


def oskour(C, L, I, n, k=1):
    Pi = [1 / n for _ in range(n)]
    P = [0] * n
    for _ in range(k):
        for i in range(n):
            if (i + 1 < len(L)):
                if L[i] == L[i + 1]:  # Empty line
                    for j in range(n):
                        P[j] += 1 / n * Pi[i]
                else:
                    for j in range(L[i], L[i + 1]):
                        P[I[j]] += C[j] * Pi[i]
    return P


if __name__ == '__main__':
    file = "../data/corpus.xml"
    l_test = [
        (0, "Page0", "sdldlkfjasdf[[Page1]]weroiw[[Page3]]erweiru"),
        (0, "Page1", "sdldlkfjasdf[[Page0]]weroiwerweiru"),
        (0, "Page2", "sdldlkfjasdf[[Page1]]wer[[Page4]]oiwerweiru"),
        (0, "Page3", "sdldlkfjasdf[[Page3]]weroiwerwe[[Page4]]iru"),
        (0, "Page4", "sdldlkfjasdfweroiwerweiru"),
        (0, "Page5", "sdldlkfjasdfweroiwerweiru")
    ]
    C, L, I = pages_to_cli(l_test)

    print(C)
    print(L)
    print(I)

    print(oskour(C, L, I, 6))
