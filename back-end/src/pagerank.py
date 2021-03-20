import time

from utils import deserialize, serialize, print_percentage, hms_string, get_clean_tokens
import numpy as np


def error(pi, pre_pi):
    c = 0
    for el1, el2 in zip(pi, pre_pi):
        c += abs(el2 - el1)
    return c


def create_pagerank(C, L, I, k=1):
    """
    :param n: Matrix length
    :param k: iteration nb
    :return: List of page rank (indices are pages ids)
    """
    start_time = time.time()

    n = len(L) - 1
    Pi = [1 / n for _ in range(n)]
    P = [0] * n
    for _ in range(k):
        for i in range(n):

            if i + 1 < n + 1:
                if L[i] == L[i + 1]:  # Empty line
                    for j in range(n):
                        P[j] += 1 / n * Pi[i]
                else:
                    for j in range(L[i], L[i + 1]):
                        P[I[j]] += C[j] * Pi[i]
            print_percentage(i, n)

    print("     ** Finish create_pagerank()")
    elapsed_time = time.time() - start_time
    print("     Elapsed time create_pagerank() : {}".format(hms_string(elapsed_time)))
    return P


def sort_page_by_score(request, dic_word_page, page_rank, alpha=5e-4, beta=.9995):
    """
    :param beta:
    :param alpha:
    :param request: list of word
    :param page_rank: Pages rank
    :param dic_word_page: word -> ((pages->tf),idf)
    :return:
        Page list sorted by score
        Dictionnary of ~200k most used words containing all the words from titles in form {word : ({page_id : TF_normalized}, IDF)}
    """
    # TODO : Fo utiliser l'algo WAND *soupire*....
    # Les pages qui contiennent les mots de la requete
    new_dict = {}
    for (key, value) in dic_word_page.items():
        if key in request:
            new_dict[key] = value
    s = set()
    page_of_request = [dic_word_page[word] for word in request if word in dic_word_page.keys()]  # [[pages], idf]
    for page_list, idf in page_of_request:
        for page in page_list.keys():
            s.add(page)
    # mot -> (page -> tfidf) score = []
    res = [(page_id, (alpha * (fd(page_id, request, new_dict)) + beta * page_rank[page_id])) for page_id in s]
    return sorted(res, key=lambda t: t[1], reverse=True)


def fd(d, r, dic_word_page):
    import math
    norm = 0
    for _, idf in dic_word_page.values():
        norm += idf ** 2
    norm = math.sqrt(norm)
    res = 0
    for m in r:
        if m in dic_word_page.keys():
            res += dic_word_page[m][1] * dic_word_page[m][0][d] if d in dic_word_page[m][0] else 0
    return res / norm


if __name__ == '__main__':

    print("deserialize pagerank")
    P = deserialize("../data/pagerank.serialized")

    print("deserialize dico")
    dicto = deserialize("../data/dico.serialized")

    print("deserialize page list")
    page_list = deserialize("../data/pagelist_noclean.serialized")

    while True:

        req = input("Req : ")

        if req == "exit 0":
            break

        clean_req = get_clean_tokens(req)

        print("clean req = ", req.split())
        print("sort page by score")
        for alpha in np.arange(0, 0.2, 0.001):
            # alpha = 0.001
            beta = 1 - alpha

            if beta > 0:

                res = sort_page_by_score(req.split(), dicto, P, alpha, beta)

                print("\nVOICI LE RESULSTAT pour alpha = ", alpha, "beta = ", beta)

                for i in res[:5]:
                    link = "https://fr.wikipedia.org/?curid={0}"
                    # print(page_list[i[0]][1], " ", link.format(page_list[i[0]][1].replace(" ", "_").replace("'", "%27")))
                    print(page_list[i[0]][1], " ", link.format(page_list[i[0]][0]))
