from parse import clean, pages_to_cli,create_dict


def error(pi, pre_pi):
    c = 0
    for el1, el2 in zip(pi, pre_pi):
        c += abs(el2 - el1)
    return c


def page_rank(C, L, I, n, k=1):
    """
    :param n: Matrix length
    :param k: iteration nb
    :return: List of page rank (indices are pages ids)
    """
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


def sort_page_by_score(request,  dic_word_page, P, alpha=0.5, beta=0.5):
    """
    :param request: list of word
    :param P: Pages rank
    :return:
        Page list sorted by score
        Dictionnary of ~10k most used words containing all the words from titles in form {word : ({page_id : TF_normalized}, IDF)}
    """
    # TODO : Fo utiliser l'algo WAND *soupire*....
    # Les pages qui contiennent les mots de la requete
    page_of_request = [dic_word_page[word] for word in request]  # [[pages], idf]
    s = set()
    for page_list, idf in page_of_request:
        for page in page_list:
            s.add(page)
    # mot -> (page -> tfidf) score = []
    res = [(page_id, (alpha * (fd(page_id, request, dic_word_page)) + beta * P[page_id])) for page_id in s]
    return sorted(res)


def fd(d, r, dic_word_page):
    import math
    norm = 0
    for _,idf in dic_word_page.values():
        norm += idf**2
    norm = math.sqrt(norm)
    res = 0
    for m in r:
        res += dic_word_page[m][1] * dic_word_page[m][d]
    return res / norm


if __name__ == '__main__':
    file = "../data/corpus.xml"
    l_test = [
        (0, "Page0", "voiture lol hiboux arbre chien chat [[Page1]]weroiw[[Page3]]erweiru"),
        (0, "Page1", "sdldlvoiture lol hiboux arbre chien chat voiture lol hiboux arbre chien chat kfjasdf[[Page0]]weroiwerweiru"),
        (0, "Page2", "sdldlkfjasdf[[Page1]]wer[[Page4]]oiwerweivoiture lol hiboux arbre chien chat ru"),
        (0, "Page3", "svoiture lol hiboux arbre chien chat dldlkfjasdf[[Page3]]weroiwerwe[[Page4]]iru"),
        (0, "Page4", "sdldlkfjasdfweroiwerweiruvoiture lol hiboux arbre chien chat "),
        (0, "Page5", "sdldlkfjasdfweroiwerwvoiture lol hiboux arbre chien chat eiru")
    ]
    C, L, I = pages_to_cli(l_test)

    l_test = [(a,b,clean(content)) for a,b,content in l_test]

    P = page_rank(C,L,I,6, 10)

    dict = create_dict(l_test)

    res = sort_page_by_score(["voiture", "arbre"],dict,P)

    print(C)
    print(L)
    print(I)

    print(page_rank(C, L, I, 6))
