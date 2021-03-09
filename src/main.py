from parse import parse, create_dict, pages_to_cli, clean_page_list

from utils import serialize, deserialize


def _pregenerate_and_serialize():
    print(" * Start parse")
    mylist = parse("../data/corpus.xml")

    print(" * Start serialize list before clean")
    serialize(mylist, "../data/pagelist_noclean.serialized")

    # print(" * Start deserialize list before clean")
    # mylist = deserialize("../data/pagelist_noclean.serialized")

    print(" * Start CLI")
    C, L, I = pages_to_cli(mylist)

    print(" * Start serialize CLI")
    serialize((C, L, I), "../data/CLI2.serialized")

    print(" * Start cleaning page list")
    mylist = clean_page_list(mylist)

    print(" * Start serialize list after clean")
    serialize(mylist, "../data/pagelist_clean.serialized")

    # print(" * Start deserialize list after clean")
    # mylist = deserialize("../data/pagelist_clean.serialized")

    print(" * Start create dict")
    mydico = create_dict(mylist)

    print(" * Start serialize dict")
    serialize(mydico, "../data/dico2.serialized")

    print("* Finish")


if __name__ == '__main__':
    _pregenerate_and_serialize()
