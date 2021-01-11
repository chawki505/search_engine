import xml.etree.ElementTree as ET
import re

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
    regex = re.compile("\{\{.*?\}\}", re.MULTILINE | re.DOTALL)
    match = regex.match(text)
    if match:
        # TODO : bug ragex with {{ and }}
        print("==================DEBUT==========================")
        print(match.group())
        text = text.replace(match.group(), "")
        print("==================FIN==========================")

    # match = re.search(r"(\{\{.*\}\})", text, flags=re.MULTILINE)
    # text = text.replace("{{.*}}", "")
    # text = re.sub(r'\{\{.*}\}', '', text, re.)

    for line in text.split("\n"):
        if re.match(sub_title_re, line):
            is_in_subtitle = True
            # continue ??
        if re.match("== .* ==", line) and not is_in_subtitle:
            is_in_subtitle = False
        if not is_in_subtitle:
            final_text += line + "\n"
    return final_text


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


if __name__ == '__main__':
    file = "../data/frwiki10000.xml"

    mylist = parse(file)

    print(mylist[0])
