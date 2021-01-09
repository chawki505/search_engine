import xml.etree.ElementTree as ET

litterature_keywords = []


def filter_pages(list):
    """
    Get only pages that talk about our topic
    :param text:
    :return:
    """
    f = lambda id, title, text :
        if (ta_fonction(text) == False ) return None


    filter(list, f)


def contain_key_words(text) :
    return False


def parse_text_page(text):


    pass


def parse(file):
    """

    :param file:
    :return:
        List of tuple containing (id, title, content) for each page
    """
    tree = ET.parse(file)
    root = tree.getroot()
    page_list = []
    for child in root:
        if child.tag == "page":
            for page in child.attrib :
                id = None
                title = None
                content = None
                if page.tag == title : title = page.attrib
                if page.tag == id : id = page.attrib
                if page.tag == text : text = page.attrib
                page_list.append(id, title, parse_text_page(text))
    return page_list