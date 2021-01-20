from parse import parse


def get_links(page_text):
    """
    :param page_text: Page texte
    :return:
    The list of externals link of the page
    """
    import re
    l = re.findall('\[\[.*?\]\]', page_text)
    return [s[2:-2] for s in l]


def pages_to_matrix(l):
    """
    edge : [[Title]] in page content
    node : page id
    :param l: list of pair containing (title, page content)
    :return:
        adjacency matrix of the web graph
    """
    m_len = len(l)
    matrix = [[0 for i in range(m_len)] for j in range(m_len)]
    for i, (title, page) in enumerate(l):
        links = get_links(page)
        for link in links:
            link_id = next(i for i, (title, page) in enumerate(l) if title == link)
            matrix[i][link_id] = 1 / len(links)
    return matrix


if __name__ == '__main__':
    file = "../data/corpus.xml"

    mylist = parse(file)

    print(mylist)
