import time
import xml.etree.ElementTree as ET

import math

from utils import print_percentage, hms_string, get_links, get_resume, wiki_to_paintext, get_clean_tokens


def parse_corpus(file_name, pages_count=252374):
    """
    :param file_name:
        XML file containing pages data
    :param pages_count:
        number of pages
    :return:
        List of tuple containing (id, title, content) for each page
    """
    start_time = time.time()

    pagelist_noclean = []
    total_pages_count = 0

    id = None
    title = None
    content = None

    for event, elem in ET.iterparse(file_name, events=('start', 'end')):
        tname = elem.tag

        if event == 'start':

            if tname == 'page':
                title = ''
                id = -1
                content = ''
        else:
            if tname == 'title':
                title = elem.text

            elif tname == 'id':
                id = int(elem.text)

            elif tname == 'text':
                content = elem.text

            elif tname == 'page':
                total_pages_count += 1
                pagelist_noclean.append((id, title, content))
                print_percentage(total_pages_count, pages_count)

            elem.clear()

    elapsed_time = time.time() - start_time
    print("  ** Finish parse corpus")
    print("  - Elapsed time parse corpus : {}".format(hms_string(elapsed_time)))

    return pagelist_noclean


def create_links_pagelist(pagelist_noclean):
    start_time = time.time()
    pagelist_links = []
    listsize = len(pagelist_noclean)

    for i, (id, title, content) in enumerate(pagelist_noclean):
        links = get_links(content)
        pagelist_links.append((id, title, links))
        print_percentage(i, listsize)

    elapsed_time = time.time() - start_time
    print("  ** Finish create links pagelist")
    print("  - Elapsed time create links pagelist : {}".format(hms_string(elapsed_time)))
    return pagelist_links


def create_plaintext_pagelist(pagelist_noclean):
    start_time = time.time()
    pagelist_plaintext = []
    listsize = len(pagelist_noclean)

    for i, (id, title, content) in enumerate(pagelist_noclean):
        text = wiki_to_paintext(content)
        pagelist_plaintext.append((id, title, text))
        print_percentage(i, listsize)

    elapsed_time = time.time() - start_time
    print("  ** Finish create plaintext pagelist")
    print("  - Elapsed time create plaintext pagelist : {}".format(hms_string(elapsed_time)))
    return pagelist_plaintext


def create_clean_tokens_pagelist(pagelist_plaintext):
    start_time = time.time()
    pagelist_clean_tokens = []
    listsize = len(pagelist_plaintext)

    for i, (id, title, content) in enumerate(pagelist_plaintext):
        content_clean_tokens = get_clean_tokens(content, remove_section=True)
        pagelist_clean_tokens.append((id, title, content_clean_tokens))
        print_percentage(i, listsize)

    elapsed_time = time.time() - start_time
    print("  ** Finish create clean tokens pagelist")
    print("  - Elapsed time create clean tokens pagelist : {}".format(hms_string(elapsed_time)))
    return pagelist_clean_tokens


def create_cli(pagelist_links):
    """
    edge : [[Title]] in page content
    node : page id
    :param pagelist_links: list of pair containing (id, title, list links content)
    :return:
        Adjacency matrix of the web graph in CLI form
    """
    start_time = time.time()
    listsize = len(pagelist_links)
    dic = {}
    dic_edges = {}

    for id_list, (_, title, _) in enumerate(pagelist_links):
        dic[title] = id_list

    for _, id_list in dic.items():
        dic_edges[id_list] = [link for link in pagelist_links[id_list][2] if link in dic.keys()]

    C = []
    L = [0]
    I = []

    for i, _ in enumerate(pagelist_links):
        links = dic_edges[i]
        edge_nb = len(links)
        val = 1 / edge_nb if edge_nb > 0 else 0

        for link in links:
            if link not in dic.keys():
                continue

            id_link = dic[link]
            C.append(val)
            I.append(id_link)

        L.append(L[-1] + edge_nb)
        print_percentage(i, listsize)

    elapsed_time = time.time() - start_time
    print("  ** Finish create cli")
    print("  - Elapsed time create cli : {}".format(hms_string(elapsed_time)))
    return C, L, I


def create_dico(pagelist_clean_tokens):
    """
    :param pagelist_clean_tokens: list of pages to parse
    :return:
        Dictionnary of ~200k most used words containing all the words from titles in form {word : ({page_id : TF_normalized}, IDF)}
    """
    start_time = time.time()

    dico_title = dict()
    dico_text = dict()
    listsize = len(pagelist_clean_tokens)

    for id, (_, title, content) in enumerate(pagelist_clean_tokens):
        # Tokeniser le titre
        title_clean = get_clean_tokens(title)

        # for word in title_lemmatized:
        for word in title_clean:

            if word not in dico_title.keys():  # word not in dict
                dico_title[word] = ({id: 1}, 0)
            else:  # word in dict
                if id not in dico_title[word][0].keys():  # page is not in list
                    dico_title[word][0][id] = 100
                else:  # page already in list
                    dico_title[word][0][id] += 50

        for word in content:
            if word not in dico_text.keys():
                dico_text[word] = ({id: 1}, 0)
            else:
                if id not in dico_text[word][0].keys():  # page is not in list
                    dico_text[word][0][id] = 10
                else:  # page already in list
                    dico_text[word][0][id] += 5

        print_percentage(id, listsize)

    dico_title.update({key: value for key, value in
                       sorted(list(dico_text.items()), key=lambda item: len(item[1][0].items()))
                       [-200000:]})

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
        idf = math.log10(listsize / len(dico_title[word][0].keys()))
        dico_title[word] = (dico_title[word][0], idf)

        for page, tf in dico_title[word][0].items():
            dico_title[word][0][page] = tf / math.sqrt(tf_norm[page])

    elapsed_time = time.time() - start_time
    print("  ** Finish create dico")
    print("  - Elapsed time create dico : {}".format(hms_string(elapsed_time)))
    return dico_title


def create_resume_pagelist(pagelist_plaintext):
    start_time = time.time()
    pagelist_plaintext_resume = []
    listsize = len(pagelist_plaintext)

    for i, (id, title, content) in enumerate(pagelist_plaintext):
        resume = get_resume(content)
        pagelist_plaintext_resume.append((id, title, resume))
        print_percentage(i, listsize)

    elapsed_time = time.time() - start_time
    print("  ** Finish create resume pagelist")
    print("  - Elapsed time create resume pagelist : {}".format(hms_string(elapsed_time)))
    return pagelist_plaintext_resume
