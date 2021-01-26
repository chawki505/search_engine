import re

# for serialization 
import pickle

def valid_category(page):
    """
        Test if our page talk about our topic
        :param page
        :return: true if the page talk about our topic
    """
    categorie_re = re.compile(r'\[+Catégorie:(.*?)('
                              r'([lL]itt[ée]rature(s)?)|'
                              r'([lL]itt[ée]raire(s)?)|'
                              r'([lL]ivre(s)?)|'
                              r'([fF]able(s)?)|'
                              r'([fF]abuliste(s)?)|'
                              r'([pP]o[ée]sie(s)?)|'
                              r'([pP]o[èe]me(s)?)|'
                              r'([pP]o[èe]te(s)?(sse(s)?)?)|'
                              r'([hH]omonymie(s)?)|'
                              #  r'([ÉEée]cri((vain)|(ture)|(t(e)?))(s)?)|'
                              r'([ÉEée]crivain(s)?)|'
                              r'([Pp]resse(s)?)|'
                              r'([lL]inguistique(s)?)|'
                              r'([rR]oman((cier)|(ci[eè]re))?(s)?)|'
                              r'([dD]ocument(aire)?(s)?)|'
                              r'([eE]ncyclop[ée]die(s)?)|'
                              r'([vV]ers)|'
                              r'([lL]ang((ue)|(age))(s)?)|'
                              r'([aA]rticle(s)?)|'
                              r'([aA]uteur)|'
                              r'([rR]echerche)|'
                              r'([oO]uvrage(s)?)|'
                              #     r'([tT]exte)|'
                              r'([nN]arratologie)|'
                              r'([rR][eé]cit)|'
                              r'([pP]hilologie)|'
                              r'([rR]evue)|'
                              r'([pP]rix)|'
                              r'([tT]raduct((ion)|(eur))(s)?)|'
                              r'([ÉEée]diteur)|'
                              r'([ÉEée]tude)|'
                              r'(Œuvre(s)?)|'
                              r'([oO]euvre(s)?)|'
                              r'([bB]iblioth[èe]que(s)?)'
                              # r'([mM]us[eé]e(s)?)|'
                              #   r'([cC]ulture(s)?)|'
                              #      r'([aA]rt)'
                              r')(.*?)\]+')

    # categorie_re = re.compile(r'\[+Catégorie:(.*)((Littérature(s)?)|(littéraire(s)?))(.*)\]+')
    # categorie_re = re.compile(r'\[+Catégorie:(.*)((Littérature(s)?)|(Littérature(s)?))(.*)\]+')

    if page:
        match = categorie_re.search(page)

        if match:
            # print("matching ", match, "status :", match.groups())
            return match is not None

    return False


def delete_brackets(s):
    """
    Delete all brackets in out page content
    :param s: our page content
    :return new page content without brackets
    """
    stack = []
    i = 0
    size = len(s)
    while i < size - 1:
        c = s[i]
        if i == size - 2:
            return s
        if c == '{' and s[i + 1] == '{':
            stack.append(('{', i))
            i += 2
        if c == '}' and s[i + 1] == '}':
            if len(stack) == 1:
                start_index = stack.pop()[1]
                s = s[: start_index] + s[i + 2:]
                i = start_index
                size = len(s)
            else:
                if stack:
                    stack.pop()
                else:
                    s = s[: i] + s[i + 2:]
                    size = len(s)
                i += 2
        else:
            i += 1
    return s


def namespace(element):
    """
    :param element: the XML element
    :return the namespace of element
        Exemple namespace("'{http://maven.apache.org/POM/4.0.0}project'" -> {http://maven.apache.org/POM/4.0.0}
    """
    m = re.match(r'\{.*\}', element.tag)
    return m.group(0) if m else ''


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


def serialize(d, path):
    with open(path, "wb") as file:
        file.write(pickle.dumps(d))

def deserialize(path):
    with open(path, "rb") as file:
        return pickle.load(file)
