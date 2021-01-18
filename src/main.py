import xml.etree.ElementTree as ET

# from nltk import pos_tag, word_tokenize

import string
import nltk
import spacy
# import contractions
import re

from utils import delete_brackets

nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords

mystopwords = stopwords.words('french')
nlp = spacy.load("fr_core_news_lg")


def filter_pages(list_pages):
    """
    Get only pages that talk about our topic
    :param list_pages:
    :return:
    """

    def valid_pages(tuple_page): return valid_category(tuple_page[2])

    return filter(valid_pages, list_pages)


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


# TODO: change this function to read corpus diractly (in stream like create_corpus())
def parse(file_name):
    """
    :param file_name:
        XML file containing pages data
    :return:
        List of tuple containing (id, title, content) for each page
    """

    page_list = []

    for event, elem in ET.iterparse(file_name, events=('start', 'end')):

        tname = elem.tag

        if event == 'start':
            if tname == 'page':
                title = ''
                id = -1
                content = ''
        elif event == 'end':

            if tname == 'title':
                title = elem.text

            elif tname == 'id':
                id = int(elem.text)

            elif tname == 'text':
                content = elem.text

            elif tname == 'page':

                page_list.append((id, title, parse_text_page(content)))
                total_pages_count += 1

                if total_pages_count == 2:
                    break

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


if __name__ == '__main__':
    file = "../data/corpus.xml"

    mylist = parse(file)

    print(mylist)
