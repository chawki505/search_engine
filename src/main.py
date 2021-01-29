import xml.etree.ElementTree as ET

import string
import nltk
import spacy
import re

from utils import delete_brackets

nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords

mystopwords = stopwords.words('french')
nlp = spacy.load("fr_core_news_lg")


def parse_text_page(text):
    """
    Parse text to only get main parts of the text ("== Title ==" paragraphs)
    :param text:
    :return:
        A clean "string" text
    """
    # TODO : Parse links ([], {}..etc) and tags
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
                page_list.append((id, title, parse_text_page(content)))

            elem.clear()

    return page_list


def clean(text):
    """
    :param text: text to clean
    :return:
        Apply lemmeization to @text and return it
    """

    # make str low
    text = text.lower()

    # TODO: fix contrations in french
    # remove contraction
    # text = contractions.fix(text)

    # remove punctuations
    punctuations_reg = re.compile('[%s]' % re.escape(string.punctuation))
    text = punctuations_reg.sub(r'', text)

    # remove stopwords
    text = ' '.join([elem for elem in text.split() if elem not in mystopwords])

    # Lemmatization
    text = ' '.join([x.lemma_ for x in nlp(text)])

    return text


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
    # file = "../data/test.xml"
