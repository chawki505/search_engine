import copy
from parse import pages_to_cli


def error(pi, pre_pi):
    c = 0
    for el1, el2 in zip(pi, pre_pi):
        c += abs(el2 - el1)
    return c


def jsais_pas(C, L, I, Pi, n, k= 0):
    # min_error = 0.3
    # pre_pi = copy.copy(Pi)
    for i in range(n):
        if L[i] == L[i + 1]:  # Empty line
            for j in range(n):
                Pi[j] += 1 / n * Pi[i]
        else:
            for j in range(L[i], L[i + 1]):
                Pi[I[j]] += C[j] * Pi[j]
    if k > 5:
        return Pi
    return jsais_pas(C, L, I, Pi, n, k+1)

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
    C,L,I = pages_to_cli(l_test)

    n = 6
    pi = jsais_pas(C,L,I,[1/n for _ in range (n)],n)
    print(pi)
