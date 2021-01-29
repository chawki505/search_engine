from parse import parse, nlp
import math


def get_links(page_text):
    """
    :param page_text: Page text
    :return:
    The list of external link of the page
    """
    import re
    l = re.findall('\[\[.*?\]\]', page_text)
    return [s[2:-2] for s in l]


def pages_to_cli(l):
    """
    edge : [[Title]] in page content
    node : page id
    :param l: list of pair containing (id, title, page content)
    :return:
        Adjacency matrix of the web graph in CLI form
    """
    C = []
    L = []
    I = []
    m_len = len(l)
    matrix = [[0 for i in range(m_len)] for j in range(m_len)]
    for i, (_, title, page) in enumerate(l):
        links = get_links(page)
        edge_nb = len(links)
        val = 1 / edge_nb
        for link in links:
            link_id = next(i for i, (_, title, page) in enumerate(l) if title == link)
            C.append(val)
            I.append(link_id)
            matrix[i][link_id] = val
        if edge_nb > 0:
            if not L:
                L.append(0)
                L.append(edge_nb)
            else:
                L.append(L[-1] + edge_nb)
    return C, L, I


def create_dict(page_list):
    """
    :param page_list: list of pages to parse
    :return:
        Dictionnary of ~10k most used words containing all the words from titles in form {word : ({page_id : TF_normalized}, IDF)}
    """
    dico_title = dict()
    dico_text = dict()
    for (id, title, content) in page_list:
        title_lemmatized = [x.lemma_ for x in nlp(title)]
        for word in title_lemmatized:
            if word not in dico_title.keys():  # word not in dict
                dico_title[word] = ({id: 1}, 0)
            else:  # word in dict
                if id not in dico_title[word][0].keys():  # page is not in list
                    dico_title[word][0][id] = 1
                else:  # page already in list
                    dico_title[word][0][id] += 1
        for word in content:
            if word not in dico_text.keys():
                dico_text[word] = ({id: 1}, 0)
            else:
                if id not in dico_text[word][0].keys():  # page is not in list
                    dico_text[word][0][id] = 1
                else:  # page already in list
                    dico_text[word][0][id] += 1
    dico_title.update({key: value for key, value in
                       sorted(list(dico_text.items()), key=lambda item: len(item[1][0].items()))[-10000:]})
    tf_norm = dict()  # normalized TF
    for word, (occ_dic, idf) in dico_title.items():
        for pageid, freq in occ_dic.items():
            if freq > 0:
                if pageid not in tf_norm.keys():
                    tf_norm[pageid] = (1 + math.log10(freq)) ** 2
                else:
                    tf_norm[pageid] += (1 + math.log10(freq)) ** 2
    # writing IDF and normalized TF
    for word in dico_title.keys():
        idf = math.log10(len(page_list) / len(dico_title[word][0].keys()))
        dico_title[word] = (dico_title[word][0], idf)
        for page, tf in dico_title[word][0].items():
            dico_title[word][0][page] = tf / math.sqrt(tf_norm[page])
    return dico_title


if __name__ == '__main__':
    pass
