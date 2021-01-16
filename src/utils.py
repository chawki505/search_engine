import re


def valid_category(page):
    """
        Test if our page talk about our topic
        :param page
        :return: true if the page talk about our topic
    """
    categorie_re = re.compile(r'\[+Catégorie:(.*)('
                              r'([lL]itt[ée]rature(s)?)|'
                              r'([lL]itt[ée]raire(s)?)|'
                              r'([lL]ivre(s)?)|'
                              r'([fF]able(s)?)|'
                              r'([fF]abuliste(s)?)|'
                              r'([pP]o[ée]sie(s)?)|'
                              r'([pP]o[èe]me(s)?)|'
                              r'([pP]o[èe]te(s)?(sse(s)?)?)|'
                              r'([hH]omonymie(s)?)|'
                              r'([ÉEée]crivain)|'
                              r'([rR]oman)|'
                              r'([aA]rticle(s)?)|'
                              r'([aA]uteur)|'
                              r'([rR]echerche)|'
                              r'([oO]uvrage(s)?)|'
                              r'([tT]exte)|'
                              r'([nN]arratologie)|'
                              r'([rR][eé]cit)|'
                              r'([pP]hilologie)|'
                              r'([rR]evue)|'
                              r'([pP]rix)|'
                              r'([tT]raduction)|'
                              r'([tT]raducteur)|'
                              r'([ÉEée]diteur)|'
                              r'([ÉEée]tude)|'
                              r'(Œuvre)|([oO]euvre)|'
                              r'([bB]iblioth[èe]que)|'
                              r'([mM]us[eé]e)'
                              r')(.*)\]+')

    match = None
    try:
        match = categorie_re.search(page)
    except TypeError:
        print(page)
    return match is not None


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
    :param The XML element
    :return The namespace of element
        Exemple namespace("'{http://maven.apache.org/POM/4.0.0}project'" -> {http://maven.apache.org/POM/4.0.0}
    """
    m = re.match(r'\{.*\}', element.tag)
    return m.group(0) if m else ''
