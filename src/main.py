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


if __name__ == '__main__':
    file = "../data/corpus.xml"

    mylist = parse(file)

    print(mylist)
