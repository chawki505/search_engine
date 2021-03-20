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

FILENAME_PAGELIST_PLAINTEXT = 'pagelist_plaintext.serialized'
path_pagelist_plaintext = os.path.join(PATH_DATA, FILENAME_PAGELIST_PLAINTEXT)

FILENAME_PAGELIST_PLAINTEXT_RESUME = 'pagelist_plaintext_resume.serialized'
path_pagelist_plaintext_resume = os.path.join(PATH_DATA, FILENAME_PAGELIST_PLAINTEXT_RESUME)

FILENAME_PAGELIST_NOCLEAN = 'pagelist_noclean.serialized'
path_pagelist_noclean = os.path.join(PATH_DATA, FILENAME_PAGELIST_NOCLEAN)

FILENAME_PAGELIST_LINKS = 'pagelist_links.serialized'
path_pagelist_links = os.path.join(PATH_DATA, FILENAME_PAGELIST_LINKS)

FILENAME_PAGELIST_CLEAN_TOKENS = 'pagelist_clean_tokens.serialized'
path_pagelist_clean_tokens = os.path.join(PATH_DATA, FILENAME_PAGELIST_CLEAN_TOKENS)

FILENAME_CLI = 'cli.serialized'
path_cli = os.path.join(PATH_DATA, FILENAME_CLI)

FILENAME_DICO = 'dico.serialized'
path_dico = os.path.join(PATH_DATA, FILENAME_DICO)

FILENAME_PAGERANK = 'pagerank.serialized'
path_pagerank = os.path.join(PATH_DATA, FILENAME_PAGERANK)
