import xml.etree.ElementTree as ET
import re

nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords

mystopwords = stopwords.words('french')

import spacy

nlp = spacy.load("fr_core_news_md")

litterature_keywords = ["littérature"]


def contains_key_words(text):
    return any(srchstr in text for srchstr in litterature_keywords)


def filter_pages(list):
    """
    Get only pages that talk about our topic
    :param text:
    :return:
    """
    valid_page = lambda tuple: None if not contains_key_words(tuple[1]) and not contains_key_words(tuple[2]) else (
        tuple[0], tuple[1], tuple[2])
    return [x for x in filter(valid_page, list)]


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


def delete_brackets(s):
    stack = []
    i = 0
    size = len(s)
    while i < size - 1:
        c = s[i]
        if i == size - 2:
            return s
        if c == '{' and s[i + 1] == '{':
            stack.append(('{', i))
            i += 2
        if c == '}' and s[i + 1] == '}':
            if len(stack) == 1:
                start_index = stack.pop()[1]
                s = s[: start_index] + s[i + 2:]
                i = start_index
                size = len(s)
            else:
                if stack:
                    stack.pop()
                else:
                    s = s[: i] + s[i + 2:]
                    size = len(s)
                i += 2
        else:
            i += 1
    return s


def namespace(element):
    """
    :param element
        The xml element
    :return:
        The namespace of element
        Exemple namespace("'{http://maven.apache.org/POM/4.0.0}project'" -> {http://maven.apache.org/POM/4.0.0}
    """
    m = re.match(r'\{.*\}', element.tag)
    return m.group(0) if m else ''


def parse(file_name):
    """
    :param file_name:
        XML file containing pages data
    :return:
        List of tuple containing (id, title, content) for each page
    """
    tree = ET.parse(file_name)
    root = tree.getroot()
    nspace = namespace(root)

    page_list = []

    for page in root.findall("{}page".format(nspace)):
        title = page.findtext("{}title".format(nspace))
        id = page.findtext("{}id".format(nspace))
        content = page.find("{}revision".format(nspace)).findtext("{}text".format(nspace))
        page_list.append((id, title, parse_text_page(content)))

    # TODO : filter pages
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
            if elem == 0 :
                continue
            else :
                current_row.append(elem)
                I.append(j)
                C.append(elem)
        if len(current_row) > 0 :
            if not L:
                L.append(0)
                L.append(len(current_row))
            else: L.append(L[-1]+len(current_row))
    return C,L,I


if __name__ == '__main__':
    file = "../data/frwiki10000.xml"
    # file = "../data/frwikionepage.xml"

    mylist = parse(file)

    print(mylist[0][2])
