import xml.etree.ElementTree as ET
from xml.dom import minidom
import html

import csv
import time
import os
import io

from src.utils import valid_category

PATH_WIKI_XML = '../data/'
FILENAME_WIKI = 'frwiki-20201201-pages-articles-multistream.xml'
# FILENAME_WIKI = 'frwiki10000.xml'
FILENAME_ARTICLES = 'pages-filtre.csv'
FILENAME_CORPUS = 'corpus.xml'

pathWikiXML = os.path.join(PATH_WIKI_XML, FILENAME_WIKI)
pathPages = os.path.join(PATH_WIKI_XML, FILENAME_ARTICLES)
pathCorpus = os.path.join(PATH_WIKI_XML, FILENAME_CORPUS)


# Nicely formatted time string
def hms_string(sec_elapsed):
    h = int(sec_elapsed / (60 * 60))
    m = int((sec_elapsed % (60 * 60)) / 60)
    s = sec_elapsed % 60
    return "{}:{:>02}:{:>05.2f}".format(h, m, s)


def strip_tag_name(t):
    idx = t.rfind("}")
    if idx != -1:
        t = t[idx + 1:]
    return t


def create_corpus():
    total_pages_count = 0
    total_filtre_pages_count = 0
    title = None
    root = None

    start_time = time.time()

    with io.open(pathPages, 'w') as pagesFH:

        page_writer_csv = csv.writer(pagesFH, quoting=csv.QUOTE_MINIMAL)

        page_writer_csv.writerow(['id', 'title'])

        for event, elem in ET.iterparse(pathWikiXML, events=('start', 'end')):
            tname = strip_tag_name(elem.tag)
            if event == 'start':
                if tname == 'mediawiki':
                    root = ET.Element(tname)
                if tname == 'page':
                    ns = 0
                    title = ''
                    id = -1
                    inrevision = False
                    content = ''
                elif tname == 'revision':
                    # Do not pick up on revision id's
                    inrevision = True
            else:
                if tname == 'title':
                    title = elem.text
                elif tname == 'id' and not inrevision:
                    id = int(elem.text)
                elif tname == 'ns':
                    ns = int(elem.text)
                elif tname == 'text' and inrevision:
                    content = elem.text

                elif tname == 'page':
                    total_pages_count += 1

                    if ns == 0 and valid_category(content):
                        total_filtre_pages_count += 1
                        page_elem = ET.SubElement(root, tname)

                        title_elem = ET.SubElement(page_elem, 'title')
                        title_elem.text = title

                        id_elem = ET.SubElement(page_elem, 'id')
                        id_elem.text = str(id)

                        text_elem = ET.SubElement(page_elem, 'text')
                        text_elem.text = content

                        page_writer_csv.writerow([id, title])

                    if total_pages_count > 1 and (total_pages_count % 10000) == 0:
                        print("Current pages : {:,}".format(total_pages_count))
                        print("Current pages filtre: {:,}".format(total_filtre_pages_count))

                elem.clear()
            # limit corpus to 500K pages
            if total_filtre_pages_count == 500000:
                break
    xmlstr = minidom.parseString(ET.tostring(root, encoding='unicode')).toprettyxml()

    with io.open(pathCorpus, 'w') as corpusFH:
        # corpusFH.write(html.unescape(xmlstr))
        corpusFH.write(xmlstr)

    elapsed_time = time.time() - start_time
    print("Total pages: {:,}".format(total_pages_count))
    print("Total pages filtre: {:,}".format(total_filtre_pages_count))
    print("Elapsed time: {}".format(hms_string(elapsed_time)))

if __name__ == '__main__':
    create_corpus()
