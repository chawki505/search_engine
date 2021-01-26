from parse import parse



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
        Dictionnary of ~10k most used words cpntaining all the words from titles
    """
    dico_title = dict()
    dico_text = dict()
    for (id, title, content) in page_list:
        title_lematised = [x.lemma_ for x in nlp(title)]
        for word in title_lematised:
            if word not in dico_title.keys():
                dico_title[word] = [id]
            else:
                if not id in dico_title[word] :
                    dico_title[word].append(id)
        for word in clean(content).split():
            if word not in dico_text.keys():
                dico_text[word] = [id]
            else:
                if not id in dico_text[word]:
                    dico_text[word].append(id)
    dico_title.update({key: value for key, value in sorted(list(dico_text.items()), key=lambda item: len(item[1]))[-10000:]})
    return dico_title
    
            

if __name__ == '__main__':
    # file = "../data/corpus.xml"
    # file = "../data/frwiki10000.xml"