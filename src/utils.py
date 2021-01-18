import re


def valid_category(page):
    """
        Test if our page talk about our topic
        :param page
        :return: true if the page talk about our topic
    """
    categorie_re = re.compile(r'\[+Catégorie:(.*)([Ll](ittérature)|ittéraire)|(ivre)(.*)\]+')

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


# Nicely formatted time string
def hms_string(sec_elapsed):
    h = int(sec_elapsed / (60 * 60))
    m = int((sec_elapsed % (60 * 60)) / 60)
    s = sec_elapsed % 60
    return "{}:{:>02}:{:>05.2f}".format(h, m, s)


def strip_tag_name(elem):
    t = elem.tag
    idx = k = t.rfind("}")
    if idx != -1:
        t = t[idx + 1:]
    return t
