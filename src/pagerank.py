from parse import clean, pages_to_cli, create_dict
from src.utils import deserialize


def error(pi, pre_pi):
    c = 0
    for el1, el2 in zip(pi, pre_pi):
        c += abs(el2 - el1)
    return c


def page_rank(C, L, I, k=1):
    """
    :param n: Matrix length
    :param k: iteration nb
    :return: List of page rank (indices are pages ids)
    """
    n = len(L) - 1
    Pi = [1 / n for _ in range(n)]
    P = [0] * n
    for _ in range(k):
        for i in range(n):
            if i + 1 < len(L):
                if L[i] == L[i + 1]:  # Empty line
                    for j in range(n):
                        P[j] += 1 / n * Pi[i]
                else:
                    for j in range(L[i], L[i + 1]):
                        P[I[j]] += C[j] * Pi[i]
    return P


def sort_page_by_score(request, dic_word_page, P, alpha=0.5, beta=0.5):
    """
    :param request: list of word
    :param P: Pages rank
    :param dic_word_page: word -> ((pages->tf),idf)
    :return:
        Page list sorted by score
        Dictionnary of ~10k most used words containing all the words from titles in form {word : ({page_id : TF_normalized}, IDF)}
    """
    # TODO : Fo utiliser l'algo WAND *soupire*....
    # Les pages qui contiennent les mots de la requete
    new_dict = {}
    for (key, value) in dic_word_page.items():
        if key in request:
            new_dict[key] = value
    s = set()
    page_of_request = [dic_word_page[word] for word in request]  # [[pages], idf]
    for page_list, idf in page_of_request:
        for page in page_list.keys():
            s.add(page)
    # mot -> (page -> tfidf) score = []
    res = [(page_id, (alpha * (fd(page_id, request, new_dict)) + beta * P[page_id])) for page_id in s]
    return sorted(res, key=lambda t: t[1], reverse=True)


def fd(d, r, dic_word_page):
    import math
    norm = 0
    for _, idf in dic_word_page.values():
        norm += idf ** 2
    norm = math.sqrt(norm)
    res = 0
    for m in r:
        res += dic_word_page[m][1] * dic_word_page[m][0][d] if d in dic_word_page[m][0] else 0
    return res / norm


if __name__ == '__main__':
    # file = "../data/corpus.xml"
    l_test = [
        (0, "Page0", "sdldlkfjasdf[[Page1]]weroiw[[Page2]]erweiru[[Page3]]jhgfdfghj"),
        (1, "Page1", "sdldlkfjasdf[[Page0]]weroiwer[[Page2]]weiru"),
        (2, "Page2", "sdldlkfjasdfweroiwerweiru"),
        (3, "Page3", "sdldlkfjasdf[[Page1]]weroiwerweiru")
    ]
    C, L, I = pages_to_cli(l_test)

    l_test = [(a, b, clean(content)) for a, b, content in l_test]

    P = page_rank(C, L, I, 10)

    dict = create_dict(l_test)

    res = sort_page_by_score(["voiture", "arbre"], dict, P)

    print(C)
    print(L)
    print(I)

    print(P)
    print("VOICI LE RESULSTAT")
    print(res)

    # (C, L, I) = deserialize("../data/CLI.serialized")
    #
    # print(len(C))
    # print(len(L))
    # print(len(I))
    #
    # print("init page rank")
    # P = page_rank(C, L, I, k=1)
    #
    # dicto = deserialize("../data/dict.serialized")
    # req = "theatre comedie française"
    #
    # print("sort page by score")
    # res = sort_page_by_score(clean(req), dicto, P)
    #
    # print("VOICI LE RESULSTAT")
    # print(res[:10])
