import xml.etree.ElementTree as ET

import string
import re
import math

from bs4 import BeautifulSoup

from utils import delete_brackets, mystopwords

import spacy

nlp = spacy.load("fr_core_news_lg")

def get_links(page_text):
    """
    :param page_text: Page text
    :return:
    The list of external link of the page
    """
    import re
    l = re.findall('\[\[.*?\]\]', page_text)
    return [s[2:-2].split("|")[0] for s in l]


def pages_to_cli(l):
    """
    edge : [[Title]] in page content
    node : page id
    :param l: list of pair containing (id, title, page content)
    :return:
        Adjacency matrix of the web graph in CLI form
    """
    C = []
    L = [0]
    I = []
    for i, (_, title, page) in enumerate(l):
        links = get_links(page)
        edge_nb = len(links)
        val = 1 / edge_nb if edge_nb > 0 else 0
        for link in links:
            try : 
                link_id = next(i for i, (_, title, _) in enumerate(l) if title == link)
            except Exception as e:
                continue
            C.append(val)
            I.append(link_id)
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

    text = delete_brackets(text)

    for line in text.split("\n"):
        if re.match(sub_title_re, line):
            is_in_subtitle = True
            # continue ??
        if re.match("== .* ==", line) and not is_in_subtitle:
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

    

    # supprimer la punctuations
    croch_reg = re.compile(r"\[{2}|\]{2}")
    text = croch_reg.sub(r'', page)

    punctuations_reg = re.compile(r"[!\"#$%&()*+’,-./:;<=>«»?@\[\]^_`{|}~]+|'{2,5}|http(s)?://\S+|www.\S+")
    # digits_reg = re.compile('[%s]' % re.escape(string.digits))
    text = punctuations_reg.sub(r' ', text)
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

    page_list = []
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
                # format html
                soup = BeautifulSoup(content, "html5lib")
                page_list.append((id, title, parse_text_page(soup.get_text(strip=True))))

            elem.clear()

    print(" * Creating CLI")
    C, L, I = pages_to_cli(page_list)
    print(" * Cleaning")
    listsize = len(page_list)
    for i,(id, title, content) in enumerate(page_list):
        if i % 1000 == 0:
            print(str(i/listsize * 100), "%")
        page_list[i] = (id, title, clean(content))
    return page_list, (C, L, I)
