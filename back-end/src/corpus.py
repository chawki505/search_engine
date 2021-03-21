import xml.etree.ElementTree as ET
import csv
import time
import io

from utils import valid_category, strip_tag_name, hms_string, print_percentage, wiki_to_paintext
from paths import path_pages_title_csv, path_corpus_xml, path_wiki_XML, path_corpus_plaintext


def create_corpus_wiki(filename_wiki):
    total_pages_count = 0
    total_filtre_pages_count = 0
    title = None
    id = None
    content = None
    ns = None
    in_revision = False
    is_created = False
    is_redirection = False

    start_time = time.time()

    with io.open(path_pages_title_csv, 'w') as pagesFH, \
            io.open(path_corpus_xml, 'w') as corpusFH:

        page_writer_csv = csv.writer(pagesFH, quoting=csv.QUOTE_MINIMAL)
        page_writer_csv.writerow(['id', 'title'])

        for event, elem in ET.iterparse(filename_wiki, events=('start', 'end')):
            tname = strip_tag_name(elem.tag)

            if event == 'start':

                if tname == 'mediawiki':
                    corpusFH.write("<mediawiki>\n")
                    is_created = True

                elif tname == 'page':
                    ns = 0
                    title = ''
                    id = -1
                    is_redirection = False
                    in_revision = False
                    content = ''

                elif tname == 'redirect':
                    is_redirection = True

                elif tname == 'revision':
                    # Do not pick up on revision id's
                    in_revision = True
            else:
                if tname == 'title':
                    title = elem.text
                elif tname == 'id' and not in_revision:
                    id = int(elem.text)
                elif tname == 'ns':
                    ns = int(elem.text)
                elif tname == 'text' and in_revision:
                    content = elem.text

                elif tname == 'page':
                    total_pages_count += 1

                    if not is_redirection and ns == 0 and valid_category(content):
                        total_filtre_pages_count += 1
                        page_elem = ET.Element('page')
                        page_elem.text = "\n\t\t"
                        page_elem.tail = "\n"

                        title_elem = ET.SubElement(page_elem, 'title')
                        title_elem.text = title
                        title_elem.tail = "\n\t\t"

                        id_elem = ET.SubElement(page_elem, 'id')
                        id_elem.text = str(id)
                        id_elem.tail = "\n\t\t"

                        text_elem = ET.SubElement(page_elem, 'text')
                        text_elem.text = content
                        text_elem.tail = "\n\t"

                        page_writer_csv.writerow([id, title])
                        corpusFH.write("\t")
                        corpusFH.write(ET.tostring(page_elem, encoding='unicode'))

                    if total_pages_count > 1 and (total_pages_count % 10000) == 0:
                        print("   Current pages : {:,}".format(total_pages_count))
                        print("   Current pages filtre: {:,}".format(total_filtre_pages_count))
                elem.clear()

        if is_created:
            corpusFH.write("</mediawiki>")

    elapsed_time = time.time() - start_time
    print(" ** Finish create_corpus_wiki()")
    print("   - Total pages: {:,}".format(total_pages_count))
    print("   - Total pages filtre: {:,}".format(total_filtre_pages_count))
    print("   - Elapsed time create_corpus_wiki() : {}".format(hms_string(elapsed_time)))


def corpus_wiki_to_corpus_plaintext(file_name, pages_count=252374):
    """
    :param pages_count:
    :param file_name:
        XML file containing pages data
    :return:
        List of tuple containing (id, title, content) for each page in plaintext
    """
    start_time = time.time()
    total_pages_count = 0

    id = None
    title = None
    content = None

    with io.open(path_corpus_plaintext, 'w') as corpusPT:

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
                    text = elem.text
                    text = wiki_to_paintext(text)
                    content = text

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

                    corpusPT.write(ET.tostring(page_elem, encoding='unicode'))

                    print_percentage(total_pages_count, pages_count)

                elem.clear()

    elapsed_time = time.time() - start_time
    print(" ** Finish corpus_wiki_to_corpus_plaintext()")
    print("   - Elapsed time corpus_wiki_to_corpus_plaintext() : {}".format(hms_string(elapsed_time)))


if __name__ == '__main__':
    print(" * Start create corpus wiki")
    create_corpus_wiki(path_wiki_XML)
