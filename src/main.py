import xml.etree.ElementTree as ET

import string
import re

from bs4 import BeautifulSoup

from utils import delete_brackets, mystopwords

import spacy

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


def matrix_to_cli(matrix, size):
    """
    :param matrix: squared adjacency matrix
    :param size: size of @matrix
    :return:
        C L I tuple
    """
    C = []
    L = []
    I = []
    for i in range(size):
        current_row = []
        for j in range(size):

            elem = matrix[i][j]
            if elem == 0:
                continue
            else:
                current_row.append(elem)
                I.append(j)
                C.append(elem)
        if len(current_row) > 0:
            if not L:
                L.append(0)
                L.append(len(current_row))
            else:
                L.append(L[-1] + len(current_row))
    return C, L, I


def clean(page):
    """
    :param page: text to clean
    :return:
        Apply cleanup and return a list of words
    """

    # format html
    soup = BeautifulSoup(page, "html5lib")
    text = soup.get_text(strip=True)

    # supprimer la punctuations
    croch_reg = re.compile(r"\[{2}|\]{2}")
    text = croch_reg.sub(r'', text)

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


if __name__ == '__main__':
    file = "../data/corpus2.xml"

    mylist = parse(file)
