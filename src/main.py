from parse import parse, create_dict

from utils import serialize, deserialize


def _pregenerate_and_serialize():
    print(" * Start parse")
    mylist, (C,L,I) = parse("../data/test.xml")
    print(" * Start serialize list")
    serialize(mylist, "../data/pagelist.serialized")
    print(" * Start serialize CLI")
    serialize((C,L,I), "../data/CLI.serialized")
    print(" * Start create dict")
    d = create_dict(mylist)
    print(" * Start serialize dict")
    serialize(d, "../data/dict.serialized")


if __name__ == '__main__':
    _pregenerate_and_serialize()
    pass
