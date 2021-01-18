import xml.etree.ElementTree as ET
from xml.dom import minidom
import html
import csv
import time
import os
import io

from utils import valid_category, strip_tag_name, hms_string

PATH_DATA = '../data/'
FILENAME_WIKI = 'frwiki-20201201-pages-articles-multistream.xml'
# FILENAME_WIKI = 'frwiki10000.xml'

FILENAME_PAGES_TITLE_CSV = 'pages-filtre.csv'

FILENAME_CORPUS_XML = 'corpus.xml'

pathWikiXML = os.path.join(PATH_DATA, FILENAME_WIKI)
pathPages = os.path.join(PATH_DATA, FILENAME_PAGES_TITLE_CSV)
pathCorpus = os.path.join(PATH_DATA, FILENAME_CORPUS_XML)


def create_corpus():
    total_pages_count = 0
    total_filtre_pages_count = 0
    title = None
    is_created = False

    start_time = time.time()

    with io.open(pathPages, 'w') as pagesFH, \
            io.open(pathCorpus, 'w') as corpusFH:

        page_writer_csv = csv.writer(pagesFH, quoting=csv.QUOTE_MINIMAL)
        page_writer_csv.writerow(['id', 'title'])

        for event, elem in ET.iterparse(pathWikiXML, events=('start', 'end')):
            tname = strip_tag_name(elem.tag)
            if event == 'start':

                if tname == 'mediawiki':
                    corpusFH.write("<mediawiki>\n")
                    is_created = True

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
                        print("Current pages : {:,}".format(total_pages_count))
                        print("Current pages filtre: {:,}".format(total_filtre_pages_count))

                elem.clear()

        if is_created:
            corpusFH.write("</mediawiki>")

    elapsed_time = time.time() - start_time
    print("Total pages: {:,}".format(total_pages_count))
    print("Total pages filtre: {:,}".format(total_filtre_pages_count))
    print("Elapsed time: {}".format(hms_string(elapsed_time)))


if __name__ == '__main__':
    create_corpus()
