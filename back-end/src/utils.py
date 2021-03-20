import re

# for serialization
import pickle

import spacy
import string

nlp = spacy.load("fr_core_news_lg")

mystopwords = ["a", "abord", "absolument", "afin", "ah", "ai", "aie", "aient", "aies", "ailleurs", "ainsi", "ait",
               "allaient", "allo", "allons", "allô", "alors", "anterieur", "anterieure", "anterieures", "apres",
               "après", "as", "assez", "attendu", "au", "aucun", "aucune", "aucuns", "aujourd", "aujourd'hui", "aupres",
               "auquel", "aura", "aurai", "auraient", "aurais", "aurait", "auras", "aurez", "auriez", "aurions",
               "aurons", "auront", "aussi", "autant", "autre", "autrefois", "autrement", "autres", "autrui", "aux",
               "auxquelles", "auxquels", "avaient", "avais", "avait", "avant", "avec", "avez", "aviez", "avions",
               "avoir", "avons", "ayant", "ayez", "ayons", "b", "bah", "bas", "basee", "bat", "beau", "beaucoup",
               "bien", "bigre", "bon", "boum", "bravo", "brrr", "c", "car", "ce", "ceci", "cela", "celle", "celle-ci",
               "celle-là", "celles", "celles-ci", "celles-là", "celui", "celui-ci", "celui-là", "celà", "cent",
               "cependant", "certain", "certaine", "certaines", "certains", "certes", "ces", "cet", "cette", "ceux",
               "ceux-ci", "ceux-là", "chacun", "chacune", "chaque", "cher", "chers", "chez", "chiche", "chut", "chère",
               "chères", "ci", "cinq", "cinquantaine", "cinquante", "cinquantième", "cinquième", "clac", "clic",
               "combien", "comme", "comment", "comparable", "comparables", "compris", "concernant", "contre", "couic",
               "crac", "d", "da", "dans", "de", "debout", "dedans", "dehors", "deja", "delà", "depuis", "dernier",
               "derniere", "derriere", "derrière", "des", "desormais", "desquelles", "desquels", "dessous", "dessus",
               "deux", "deuxième", "deuxièmement", "devant", "devers", "devra", "devrait", "different", "differentes",
               "differents", "différent", "différente", "différentes", "différents", "dire", "directe", "directement",
               "dit", "dite", "dits", "divers", "diverse", "diverses", "dix", "dix-huit", "dix-neuf", "dix-sept",
               "dixième", "doit", "doivent", "donc", "dont", "dos", "douze", "douzième", "dring", "droite", "du",
               "duquel", "durant", "dès", "début", "désormais", "e", "effet", "egale", "egalement", "egales", "eh",
               "elle", "elle-même", "elles", "elles-mêmes", "en", "encore", "enfin", "entre", "envers", "environ", "es",
               "essai", "est", "et", "etant", "etc", "etre", "eu", "eue", "eues", "euh", "eurent", "eus", "eusse",
               "eussent", "eusses", "eussiez", "eussions", "eut", "eux", "eux-mêmes", "exactement", "excepté",
               "extenso", "exterieur", "eûmes", "eût", "eûtes", "f", "fais", "faisaient", "faisant", "fait", "faites",
               "façon", "feront", "fi", "flac", "floc", "fois", "font", "force", "furent", "fus", "fusse", "fussent",
               "fusses", "fussiez", "fussions", "fut", "fûmes", "fût", "fûtes", "g", "gens", "h", "ha", "haut", "hein",
               "hem", "hep", "hi", "ho", "holà", "hop", "hormis", "hors", "hou", "houp", "hue", "hui", "huit",
               "huitième", "hum", "hurrah", "hé", "hélas", "i", "ici", "il", "ils", "importe", "j", "je", "jusqu",
               "jusque", "juste", "k", "l", "la", "laisser", "laquelle", "las", "le", "lequel", "les", "lesquelles",
               "lesquels", "leur", "leurs", "longtemps", "lors", "lorsque", "lui", "lui-meme", "lui-même", "là", "lès",
               "m", "ma", "maint", "maintenant", "mais", "malgre", "malgré", "maximale", "me", "meme", "memes", "merci",
               "mes", "mien", "mienne", "miennes", "miens", "mille", "mince", "mine", "minimale", "moi", "moi-meme",
               "moi-même", "moindres", "moins", "mon", "mot", "moyennant", "multiple", "multiples", "même", "mêmes",
               "n", "na", "naturel", "naturelle", "naturelles", "ne", "neanmoins", "necessaire", "necessairement",
               "neuf", "neuvième", "ni", "nombreuses", "nombreux", "nommés", "non", "nos", "notamment", "notre", "nous",
               "nous-mêmes", "nouveau", "nouveaux", "nul", "néanmoins", "nôtre", "nôtres", "o", "oh", "ohé", "ollé",
               "olé", "on", "ont", "onze", "onzième", "ore", "ou", "ouf", "ouias", "oust", "ouste", "outre", "ouvert",
               "ouverte", "ouverts", "o|", "où", "p", "paf", "pan", "par", "parce", "parfois", "parle", "parlent",
               "parler", "parmi", "parole", "parseme", "partant", "particulier", "particulière", "particulièrement",
               "pas", "passé", "pendant", "pense", "permet", "personne", "personnes", "peu", "peut", "peuvent", "peux",
               "pff", "pfft", "pfut", "pif", "pire", "pièce", "plein", "plouf", "plupart", "plus", "plusieurs",
               "plutôt", "possessif", "possessifs", "possible", "possibles", "pouah", "pour", "pourquoi", "pourrais",
               "pourrait", "pouvait", "prealable", "precisement", "premier", "première", "premièrement", "pres",
               "probable", "probante", "procedant", "proche", "près", "psitt", "pu", "puis", "puisque", "pur", "pure",
               "q", "qu", "qu'", "quand", "quant", "quant-à-soi", "quanta", "quarante", "quatorze", "quatre",
               "quatre-vingt",
               "quatrième", "quatrièmement", "que", "quel", "quelconque", "quelle", "quelles", "quelqu'un", "quelque",
               "quelques", "quels", "qui", "quiconque", "quinze", "quoi", "quoique", "r", "rare", "rarement", "rares",
               "relative", "relativement", "remarquable", "rend", "rendre", "restant", "reste", "restent", "restrictif",
               "retour", "revoici", "revoilà", "rien", "s", "sa", "sacrebleu", "sait", "sans", "sapristi", "sauf", "se",
               "sein", "seize", "selon", "semblable", "semblaient", "semble", "semblent", "sent", "sept", "septième",
               "sera", "serai", "seraient", "serais", "serait", "seras", "serez", "seriez", "serions", "serons",
               "seront", "ses", "seul", "seule", "seulement", "si", "sien", "sienne", "siennes", "siens", "sinon",
               "six", "sixième", "soi", "soi-même", "soient", "sois", "soit", "soixante", "sommes", "son", "sont",
               "sous", "souvent", "soyez", "soyons", "specifique", "specifiques", "speculatif", "stop", "strictement",
               "subtiles", "suffisant", "suffisante", "suffit", "suis", "suit", "suivant", "suivante", "suivantes",
               "suivants", "suivre", "sujet", "superpose", "sur", "surtout", "t", "ta", "tac", "tandis", "tant",
               "tardive", "te", "tel", "telle", "tellement", "telles", "tels", "tenant", "tend", "tenir", "tente",
               "tes", "tic", "tien", "tienne", "tiennes", "tiens", "toc", "toi", "toi-même", "ton", "touchant",
               "toujours", "tous", "tout", "toute", "toutefois", "toutes", "treize", "trente", "tres", "trois",
               "troisième", "troisièmement", "trop", "très", "tsoin", "tsouin", "tu", "té", "u", "un", "une", "unes",
               "uniformement", "unique", "uniques", "uns", "v", "va", "vais", "valeur", "vas", "vers", "via", "vif",
               "vifs", "vingt", "vivat", "vive", "vives", "vlan", "voici", "voie", "voient", "voilà", "voire", "vont",
               "vos", "votre", "vous", "vous-mêmes", "vu", "vé", "vôtre", "vôtres", "w", "x", "y", "z", "zut", "à", "â",
               "ça", "ès", "étaient", "étais", "était", "étant", "état", "étiez", "étions", "été", "étée", "étées",
               "étés", "êtes", "être", "ô"]


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
                              #  r'([hH]omonymie(s)?)|'
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
                              # r'([tT]exte)|'
                              # r'([nN]arratologie)|'
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
                              # r'([cC]ulture(s)?)|'
                              #      r'([aA]rt)'
                              r')(.*?)\]+')

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


def print_percentage(current_i, max_size):
    if current_i % 1000 == 0:
        print("\t\t- ", "%.4f" % (current_i / max_size * 100), " %")


def remove_html_tags(page):
    """Remove html tags from a string"""
    # clean = re.compile('<.*?>')
    clean_double_tags = re.compile(r"<(.*?)>(.*?)<(.*?)>")
    clean_single_tags = re.compile(r"<(.*?)>")

    page = re.sub(clean_double_tags, ' ', page)
    page = re.sub(clean_single_tags, ' ', page)

    return page


def remove_brackets(page):
    """Remove brackets tags from a string"""
    clean = re.compile(r"{{[^}{]*}}", flags=re.MULTILINE)
    if page:
        while clean.search(page):
            page = re.sub(clean, ' ', page)
    return page


def get_links(page_text):
    """
    :param page_text: Page text
    :return:
    The list of external link of the page
    """
    import re
    ragex = re.compile(r'\[\[.*?\]\]')
    l = ragex.findall(page_text)
    return [s[2:-2].split("|")[0] for s in l]


def unwiki(wiki):
    """
    Remove wiki markup from the text.
    """
    wiki = re.sub(r'(?i)\{\{IPA(\-[^\|\{\}]+)*?\|([^\|\{\}]+)(\|[^\{\}]+)*?\}\}', lambda m: m.group(2), wiki)
    wiki = re.sub(r'(?i)\{\{Lang(\-[^\|\{\}]+)*?\|([^\|\{\}]+)(\|[^\{\}]+)*?\}\}', lambda m: m.group(2), wiki)
    wiki = re.sub(r'\{\{[^\{\}]+\}\}', '', wiki)
    wiki = re.sub(r'(?m)\{\{[^\{\}]+\}\}', '', wiki)
    wiki = re.sub(r'(?m)\{\|[^\{\}]*?\|\}', '', wiki)
    wiki = re.sub(r'(?i)\[\[Category:[^\[\]]*?\]\]', '', wiki)
    wiki = re.sub(r'(?i)\[\[Image:[^\[\]]*?\]\]', '', wiki)
    wiki = re.sub(r'(?i)\[\[File:[^\[\]]*?\]\]', '', wiki)
    wiki = re.sub(r'\[\[[^\[\]]*?\|([^\[\]]*?)\]\]', lambda m: m.group(1), wiki)
    wiki = re.sub(r'\[\[([^\[\]]+?)\]\]', lambda m: m.group(1), wiki)
    wiki = re.sub(r'\[\[([^\[\]]+?)\]\]', '', wiki)
    wiki = re.sub(r'(?i)File:[^\[\]]*?', '', wiki)
    wiki = re.sub(r'\[[^\[\]]*? ([^\[\]]*?)\]', lambda m: m.group(1), wiki)
    wiki = re.sub(r"''+", '', wiki)
    wiki = re.sub(r'(?m)^\*$', '', wiki)

    return wiki


def unhtml(html):
    """
    Remove HTML from the text.
    """
    html = re.sub(r'(?i)&nbsp;', ' ', html)
    html = re.sub(r'(?i)<br[ \\]*?>', '\n', html)
    html = re.sub(r'(?m)<!--.*?--\s*>', '', html)
    html = re.sub(r'(?i)<ref[^>]*>[^>]*<\/ ?ref>', '', html)
    html = re.sub(r'(?m)<.*?>', '', html)
    html = re.sub(r'(?i)&amp;', '&', html)

    return html


def punctuate(text):
    """
    Convert every text part into well-formed one-space
    separate paragraph.
    """
    text = re.sub(r'\r\n|\n|\r', '\n', text)
    text = re.sub(r'\n\n+', '\n\n', text)

    parts = text.split('\n\n')
    partsParsed = []

    for part in parts:
        part = part.strip()

        if len(part) == 0:
            continue

        partsParsed.append(part)

    return '\n\n'.join(partsParsed)


def wiki_to_paintext(text):
    content = text
    content = unhtml(content)
    content = unwiki(content)
    content = punctuate(content)
    return content


def get_resume(text):
    """
    :param text: text to resume
    :return: first paragraphe in the text
    """
    # regex = re.compile(r"^(.*?)\n")
    # return regex.match(text).group(1)
    return text[:500]


def delete_section_textpage(textpage):
    """
    Parse text to only get main parts of the text ("== Title ==" paragraphs)
    :param textpage:
    :return:
        A clean "string" text
    """
    is_in_subtitle = False
    sub_title_re = "=== Bibliographie ===|== Notes et références ==|== Voir aussi =="
    final_text = ""

    for line in textpage.split("\n"):
        if re.match(sub_title_re, line):
            is_in_subtitle = True
        if re.match("== .*? ==", line) and not is_in_subtitle:
            is_in_subtitle = False
        if not is_in_subtitle:
            final_text += line + "\n"
    return final_text


def get_clean_tokens(textpage_plaintext, remove_section=False):
    """
    :param remove_section:
    :param textpage_plaintext: text to clean in tokens
    :return:
        Apply cleanup and return a list of words
    """
    text = textpage_plaintext

    if remove_section:
        # remove and get only main parts of the text
        text = delete_section_textpage(text)

    # Tokenisation of text
    tokens = nlp(text)

    # whitespace
    whitespace_reg = r'[ \t\n\r\v\f]'
    whitespace = re.compile(whitespace_reg)

    # Punctuation
    punctuation_reg = r"[!\"'#$%&()*+’,./:;-<=>«»?@\[\]^_`{|}~]"
    punctuation_reg2 = r"[\"'’]"
    punctuation = re.compile(punctuation_reg2)

    clean_tokens = []

    for token in tokens:
        if token.lemma_ not in punctuation_reg:
            clean_whitespace = whitespace.sub('', token.lemma_)
            clean_punc = punctuation.sub('', clean_whitespace)

            if clean_punc not in mystopwords and len(clean_punc) >= 1:
                clean_tokens.append(clean_punc)

    # Lemmatization and remove whitespace and punctuation
    # lemm_tokens = [whitespace.sub('', token.lemma_) for token in tokens if token.lemma_ not in punctuation_reg]

    # remove other punctuation
    # lemm_tokens = [punctuation.sub('', token) for token in lemm_tokens]

    # remove mystopwords and empty token
    # lemm_tokens = [token for token in lemm_tokens if token not in mystopwords and len(token) >= 1]

    return clean_tokens
