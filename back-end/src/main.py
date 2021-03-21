from parse import parse_corpus, create_links_pagelist, create_plaintext_pagelist, create_cli, \
    create_clean_tokens_pagelist, create_dico, create_resume_pagelist
from pagerank import create_pagerank

from utils import serialize, deserialize, hms_string

from paths import *

import time


def _pregenerate_and_serialize():
    start_time = time.time()

    print(" * Start parse corpus")
    pagelist_noclean = parse_corpus(path_corpus_xml)
    print(" * Start serialize pagelist no clean")
    serialize(pagelist_noclean, path_pagelist_noclean)
    # print(" * Start deserialize pagelist no clean")
    # pagelist_noclean = deserialize(path_pagelist_noclean)

    print(" * Start create links pageslist")
    pagelist_links = create_links_pagelist(pagelist_noclean)
    print(" * Start serialize links pagelist")
    serialize(pagelist_links, path_pagelist_links)
    # print(" * Start deserialize links pagelist")
    # pagelist_links = deserialize(path_pagelist_links)

    print(" * Start create plaintext pagelist")
    pagelist_plaintext = create_plaintext_pagelist(pagelist_noclean)
    print(" * Start serialize pagelist plaintext")
    serialize(pagelist_plaintext, path_pagelist_plaintext)
    # print(" * Start deserialize pagelist plaintext")
    # pagelist_plaintext = deserialize(path_pagelist_plaintext)

    print(" * Start create resume pagelist")
    pagelist_plaintext_resume = create_resume_pagelist(pagelist_plaintext)
    print(" * Start serialize resume pagelist")
    serialize(pagelist_plaintext_resume, path_pagelist_plaintext_resume)
    # print(" * Start deserialize pagelist plaintext resume")
    # pagelist_plaintext_resume = deserialize(path_pagelist_plaintext_resume)

    print(" * Start create CLI")
    (C, L, I) = create_cli(pagelist_links)
    print(" * Start serialize CLI")
    serialize((C, L, I), path_cli)
    # print(" * Start deserialize CLI")
    # (C, L, I) = deserialize(path_cli)

    print(" * Start create clean tokens pagelist")
    pagelist_clean_tokens = create_clean_tokens_pagelist(pagelist_plaintext)
    print(" * Start serialize clean tokens pagelist")
    serialize(pagelist_clean_tokens, path_pagelist_clean_tokens)
    # print(" * Start deserialize clean tokens pagelist")
    # pagelist_clean_tokens = deserialize(path_pagelist_clean_tokens)

    print(" * Start create dico")
    dico = create_dico(pagelist_clean_tokens)
    print(" * Start serialize dico")
    serialize(dico, path_dico)
    # print(" * Start deserialize dico")
    # dico = deserialize(path_dico)

    print(" * Start create pagerank")
    pagerank = create_pagerank(C, L, I)
    print(" * Start serialize pagerank")
    serialize(pagerank, path_pagerank)
    # print(" * Start deserialize pagerank")
    # dico = deserialize(path_pagerank)

    print(" * Finish")
    elapsed_time = time.time() - start_time
    print(" Elapsed time: {}".format(hms_string(elapsed_time)))


if __name__ == '__main__':
    _pregenerate_and_serialize()
