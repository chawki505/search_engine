from parse import parse, create_dict, pages_to_cli, clean_page_list
from pagerank import page_rank
from wiki2plain import wiki_to_plaintext_pagelist

from utils import serialize, deserialize, hms_string

from paths import path_corpus_xml, path_pagelist_plaintext, path_pagelist_clean, path_cli, path_dico, path_pagerank

import time


def _pregenerate_and_serialize():
    start_time = time.time()

    # print(" * Start parse")
    # pagelist = parse(path_corpus)

    # print(" * Start serialize pagelist no clean")
    # serialize(pagelist, path_pagelist_noclean)

    # print(" * Start deserialize pagelist no clean")
    # pagelist = deserialize(path_pagelist_noclean)

    # print(" * Start parse and create pagelist plaintext")
    # pagelist_plaintext = wiki_to_plaintext_pagelist(path_corpus_xml)

    # print(" * Start serialize pagelist plaintext")
    # serialize(pagelist_plaintext, path_pagelist_plaintext)

    # print(" * Start create CLI")
    # (C, L, I) = pages_to_cli(pagelist)

    # print(" * Start serialize CLI")
    # serialize((C, L, I), path_cli)

    # print(" * Start deserialize CLI")
    # (C, L, I) = deserialize(path_cli)

    # print(" * Start cleaning pagelist")
    # pagelist_clean = clean_page_list(pagelist)
    #
    # print(" * Start serialize clean pagelist")
    # serialize(pagelist_clean, path_pagelist_clean)
    #
    print(" * Start deserialize clean pagelist")
    pagelist_clean = deserialize(path_pagelist_clean)
    #
    print(" * Start create dict")
    dico = create_dict(pagelist_clean)
    #
    print(" * Start serialize dico")
    serialize(dico, path_dico)

    # print(" * Start deserialize dico")
    # dico = deserialize(path_dico)

    # print(" * Start create pagerank")
    # P = page_rank(C, L, I)
    # #
    # print(" * Start serialize pagerank")
    # serialize(P, path_pagerank)

    print(" * Finish")
    elapsed_time = time.time() - start_time
    print(" Elapsed time: {}".format(hms_string(elapsed_time)))


if __name__ == '__main__':
    _pregenerate_and_serialize()
