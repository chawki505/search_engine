import io
import os
import time
import xml.etree.ElementTree as ET

import string
import re
import math

from utils import mystopwords, print_percentage, hms_string, remove_html_tags, remove_brackets, get_links
from paths import path_pagelist_first_clean

import spacy

nlp = spacy.load("fr_core_news_lg")


def pages_to_cli(l):
    """
    edge : [[Title]] in page content
    node : page id
    :param l: list of pair containing (id, title, page content)
    :return:
        Adjacency matrix of the web graph in CLI form
    """
    start_time = time.time()
    dic = {}
    dic_edges = {}
    for i, (_, title, _) in enumerate(l):
        dic[title] = i

    for _, id in dic.items():
        dic_edges[id] = [link for link in get_links(l[id][2]) if link in dic.keys()]
    C = []
    L = [0]
    I = []
    for i, (_, _, page) in enumerate(l):
        # if i not in dic_edges.keys():
        #    continue
        links = dic_edges[i]
        edge_nb = len(links)
        val = 1 / edge_nb if edge_nb > 0 else 0
        for link in links:
            if link not in dic.keys():
                continue
            link_id = dic[link]
            C.append(val)
            I.append(link_id)
        L.append(L[-1] + edge_nb)
        print_percentage(i, len(l))
    print("     ** Finish pages_to_cli()")
    elapsed_time = time.time() - start_time
    print("     Elapsed time pages_to_cli() : {}".format(hms_string(elapsed_time)))
    return C, L, I


def create_dict(page_list):
    """
    :param page_list: list of pages to parse
    :return:
        Dictionnary of ~200k most used words containing all the words from titles in form {word : ({page_id : TF_normalized}, IDF)}
    """
    start_time = time.time()

    dico_title = dict()
    dico_text = dict()
    pages_list_size = len(page_list)

    for id, (_, title, content) in enumerate(page_list):
        # Tokeniser le titre
        # tokens = nlp(title)
        # title_lemmatized = [str(x.lemma_).lower() for x in tokens]
        title_clean = clean(title)

        # for word in title_lemmatized:
        for word in title_clean:

            if word not in dico_title.keys():  # word not in dict
                dico_title[word] = ({id: 1}, 0)
            else:  # word in dict
                if id not in dico_title[word][0].keys():  # page is not in list
                    dico_title[word][0][id] = 100
                else:  # page already in list
                    dico_title[word][0][id] += 100

        for word in content:
            if word not in dico_text.keys():
                dico_text[word] = ({id: 1}, 0)
            else:
                if id not in dico_text[word][0].keys():  # page is not in list
                    dico_text[word][0][id] = 1
                else:  # page already in list
                    dico_text[word][0][id] += 1

        print_percentage(id, pages_list_size)

    dico_title.update({key: value for key, value in
                       sorted(list(dico_text.items()), key=lambda item: len(item[1][0].items()))[-200000:]})
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

    print("     ** Finish create_dict()")
    elapsed_time = time.time() - start_time
    print("     Elapsed time create_dict() : {}".format(hms_string(elapsed_time)))
    return dico_title


def parse_text_page(text):
    """
    Parse text to only get main parts of the text ("== Title ==" paragraphs)
    :param text:
    :return:
        A clean "string" text
    """
    is_in_subtitle = False
    sub_title_re = "=== Bibliographie ===|== Notes et références ==|== Voir aussi =="
    final_text = ""

    text_clean_htmls = remove_html_tags(text)

    text_clean_brackets = remove_brackets(text_clean_htmls)

    for line in text_clean_brackets.split("\n"):
        if re.match(sub_title_re, line):
            is_in_subtitle = True
            # continue ??
        if re.match("== .*? ==", line) and not is_in_subtitle:
            is_in_subtitle = False
        if not is_in_subtitle:
            final_text += line + "\n"
    return final_text


def clean(page):
    """
    :param page: text to clean
    :return:
        Apply cleanup and return a list of words
    """

    # supprimer les links
    # croch_reg = re.compile(r"\[{2}|\]{2}")
    # sub crochet
    croch_reg = re.compile(r"(\[\[([^][]*)\|([^][]*)\]\])|(\[\[([^][]*)\]\])")
    text = croch_reg.sub(r"\3\5", page)

    # supprimer la punctuations
    punctuations_reg = re.compile(r"[!\"#$%&()*+’,-./:;<=>«»?@\[\]^_`{|}~]+|'{2,5}|http(s)?://\S+|www.\S+")
    text = punctuations_reg.sub(' ', text)

    text = " ".join(text.split())

    # Tokeniser le text
    tokens = nlp(text)

    # Lemmatization
    lemm_tokens = [str(x.lemma_).lower() for x in tokens if
                   str(x.text).lower() not in mystopwords and str(x.lemma_).lower() not in mystopwords]

    return lemm_tokens


def parse(file_name):
    """
    :param file_name:
        XML file containing pages data
    :return:
        List of tuple containing (id, title, content) for each page
    """
    start_time = time.time()

    page_list = []
    total_pages_count = 0

    id = None
    title = None
    content = None

    with io.open(path_pagelist_first_clean, 'w') as pagesFC:

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
                    content = parse_text_page(elem.text)

                elif tname == 'page':
                    total_pages_count += 1

                    page_elem = ET.Element('page')
                    page_elem.text = "\n\t"
                    page_elem.tail = "\n"

                    title_elem = ET.SubElement(page_elem, 'title')
                    title_elem.text = title
                    title_elem.tail = "\n\t"

                    id_elem = ET.SubElement(page_elem, 'id')
                    id_elem.text = str(id)
                    id_elem.tail = "\n\t"

                    text_elem = ET.SubElement(page_elem, 'text')
                    text_elem.text = content + "\t"
                    text_elem.tail = "\n"

                    pagesFC.write(ET.tostring(page_elem, encoding='unicode'))

                    page_list.append((id, title, content))

                    print_percentage(total_pages_count, 252374)

                elem.clear()

    print("     ** Finish parse()")
    elapsed_time = time.time() - start_time
    print("     Elapsed time parse() : {}".format(hms_string(elapsed_time)))

    return page_list


def clean_page_list(page_list):
    start_time = time.time()

    page_list_clean = []
    listsize = len(page_list)

    for i, (id, title, content) in enumerate(page_list):
        content_clean = clean(content)
        page_list_clean.append((id, title, content_clean))
        print_percentage(i, listsize)

    print("     ** Finish clean_page_list()")
    elapsed_time = time.time() - start_time
    print("     Elapsed time clean_page_list() : {}".format(hms_string(elapsed_time)))
    return page_list_clean
