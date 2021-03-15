import os

PATH_DATA = '../data/'

FILENAME_WIKI_XML = 'frwiki-20201201-pages-articles-multistream.xml'
path_wiki_XML = os.path.join(PATH_DATA, FILENAME_WIKI_XML)

FILENAME_CORPUS_XML = 'corpus.xml'
path_corpus_xml = os.path.join(PATH_DATA, FILENAME_CORPUS_XML)

FILENAME_CORPUS_PLAINTEXT_XML = 'corpus_plaintext.xml'
path_corpus_plaintext = os.path.join(PATH_DATA, FILENAME_CORPUS_PLAINTEXT_XML)

FILENAME_PAGES_TITLE_CSV = 'pages-filtre.csv'
path_pages_title_csv = os.path.join(PATH_DATA, FILENAME_PAGES_TITLE_CSV)

FILENAME_PAGELIST_FIRST_CLEAN_XML = 'pagelist_first_clean.xml'
path_pagelist_first_clean = os.path.join(PATH_DATA, FILENAME_PAGELIST_FIRST_CLEAN_XML)

FILENAME_PAGELIST_PLAINTEXT = 'pagelist_plaintext.serialized'
path_pagelist_plaintext = os.path.join(PATH_DATA, FILENAME_PAGELIST_PLAINTEXT)

FILENAME_PAGELIST_NOCLEAN = 'pagelist_noclean.serialized'
path_pagelist_noclean = os.path.join(PATH_DATA, FILENAME_PAGELIST_NOCLEAN)

FILENAME_PAGELIST_CLEAN = 'pagelist_clean.serialized'
path_pagelist_clean = os.path.join(PATH_DATA, FILENAME_PAGELIST_CLEAN)

FILENAME_CLI = 'CLI.serialized'
path_cli = os.path.join(PATH_DATA, FILENAME_CLI)

FILENAME_DICO = 'dico.serialized'
path_dico = os.path.join(PATH_DATA, FILENAME_DICO)

FILENAME_PAGERANK = 'pagerank.serialized'
path_pagerank = os.path.join(PATH_DATA, FILENAME_PAGERANK)
