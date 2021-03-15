import io
import re
import time
from utils import hms_string, print_percentage
from paths import path_corpus_plaintext
import xml.etree.ElementTree as ET


class Wiki2Plain:
    def __init__(self, wiki):
        self.wiki = wiki

        self.text = wiki
        self.text = self.unhtml(self.text)
        self.text = self.unwiki(self.text)
        self.text = self.punctuate(self.text)

    def __str__(self):
        return self.text

    def unwiki(self, wiki):
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

    def unhtml(self, html):
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

    def punctuate(self, text):
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


def wiki_to_plaintext_pagelist(file_name):
    """
    :param file_name:
        XML file containing pages data
    :return:
        List of tuple containing (id, title, content) for each page in plaintext
    """
    start_time = time.time()
    pagelist_plaintext = []
    total_pages_count = 0

    id = None
    title = None
    content = None

    with io.open(path_corpus_plaintext, 'w') as corpusPT:

        for event, elem in ET.iterparse(file_name, events=('start', 'end')):
            tname = elem.tag

            if event == 'start':

                if tname == 'page':
                    title = ''
                    id = -1
                    content = ''
            else:
                if tname == 'title':
                    title = elem.text

                elif tname == 'id':
                    id = int(elem.text)

                elif tname == 'text':
                    content = Wiki2Plain(elem.text).text

                elif tname == 'page':
                    total_pages_count += 1

                    page_elem = ET.Element('page')
                    page_elem.text = "\n\t"
                    page_elem.tail = "\n"

                    title_elem = ET.SubElement(page_elem, 'title')
                    title_elem.text = title
                    title_elem.tail = "\n\t"

                    id_elem = ET.SubElement(page_elem, 'id')
                    id_elem.text = str(id)
                    id_elem.tail = "\n\t"

                    text_elem = ET.SubElement(page_elem, 'text')
                    text_elem.text = content + "\t"
                    text_elem.tail = "\n"

                    corpusPT.write(ET.tostring(page_elem, encoding='unicode'))

                    pagelist_plaintext.append((id, title, content))

                    print_percentage(total_pages_count, 252374)

                elem.clear()

    print("     ** Finish wiki_to_plaintext_pagelist()")
    elapsed_time = time.time() - start_time
    print("     Elapsed time wiki_to_plaintext_pagelist() : {}".format(hms_string(elapsed_time)))
    return pagelist_plaintext


if __name__ == '__main__':
    wiki_page = """
   {{Infobox Biographie2|charte=linguiste
|nom                     = Antoine Meillet
|nationalité             = {{France}}
|date de naissance       = {{Date de naissance|11|novembre|1866}} 
|lieu de naissance       = [[Moulins (Allier)|Moulins]] ([[Allier (département)|Allier]]) 
|date de décès           = {{Date de décès|21|septembre|1936|11|novembre|1866}}
|lieu de décès           = [[Châteaumeillant]]
|région                  = Linguiste occidental
|époque                  = {{s|XX}}
|image                   = Meillet Antoine.jpg
|légende                 = 
|domaine  = [[Linguistique comparée]]
|principaux intérêts     = 
|influencé par           = 
|influence de            = 
|idées remarquables      = [[épithète homérique]]
|œuvres principales      = ''Introduction à l'étude comparative des langues indo-européennes'' ([[1903]])<br />
''Aperçu d'une histoire de la langue grecque'' ([[1913]])<br />
''Dictionnaire étymologique de la langue latine'' ([[1932]])
|adjectifs dérivés       = 
}}

'''Paul Jules Antoine Meillet''', né le {{Date de naissance|11|novembre|1866}} à [[Moulins (Allier)|Moulins]] ([[Allier (département)|Allier]]) et mort le {{Date de décès|21|septembre|1936}} à [[Châteaumeillant]] ([[Cher (département)|Cher]]), est le principal [[liste de linguistes|linguiste]] français des premières décennies du {{XXe siècle}}. Il est aussi [[philologue]].

== Biographie ==
D'origine bourbonnaise, fils d'un notaire de [[Châteaumeillant]] ([[Cher (département)|Cher]]), Antoine Meillet fait ses études secondaires au [[lycée Théodore-de-Banville|lycée]] de [[Moulins (Allier)|Moulins]].

Étudiant à la [[faculté des lettres de Paris]] à partir de [[1885]] où il suit notamment les cours de [[Louis Havet]], il assiste également à ceux de [[Michel Bréal]] au [[Collège de France]] et de [[Ferdinand de Saussure]] à l'[[École pratique des hautes études]].

En 1889, il est major de l'[[agrégation de grammaire]]<ref>http://rhe.ish-lyon.cnrs.fr/?q=agregsecondaire_laureats&amp;nom=&amp;annee_op=%3D&amp;annee%5Bvalue%5D=1889&amp;annee%5Bmin%5D=&amp;annee%5Bmax%5D=&amp;periode=All&amp;concours=7&amp;items_per_page=10.</ref>{{référence insuffisante|date=juillet 2020}}.

Il assure à la suite de Saussure le cours de [[grammaire comparée]], qu'il complète à partir de 1894 par une conférence sur l'[[Peuples iraniens|iranien]].

En 1897, il soutient sa thèse pour le [[doctorat]] ès lettres ''(Recherches sur l'emploi du génitif-accusatif en vieux-slave)''. En 1905, il occupe la chaire de grammaire comparée au [[Collège de France]], où il consacre ses cours à l'histoire et à la structure des [[langues indo-européennes]]. Il succéda au linguiste [[Auguste Carrière]] à la tête de la chaire d'[[arménien]] à l'[[Institut national des langues et civilisations orientales|École des langues orientales]]<ref>[http://www.inalco.fr/ina_gabarit_rubrique.php3?ctx=langue&amp;id_rubrique=47&amp;id_departement=8&amp;ina_rubrique_departement=1193&amp;id_langue=8&amp;ina_rubrique_langue=918&amp;ina_rubrique_2=1699 Institut National des Langues et Civilisations Orientales]</ref>{{référence insuffisante|date=juillet 2020}}.

Secrétaire de la [[Société de linguistique de Paris]], il est élu à l'[[Académie des inscriptions et belles-lettres]] en 1924. Il préside également l'Institut d'Etudes Slaves de 1921 à sa mort<ref>http://institut-etudes-slaves.fr/liste-des-presidents-de-lies/</ref>{{référence insuffisante|date=juillet 2020}}.

Il a formé toute une génération de linguistes français, parmi lesquels [[Émile Benveniste]], [[Marcel Cohen]], [[Georges Dumézil]], [[André Martinet]], [[Aurélien Sauvageot]], [[Lucien Tesnière]], [[Joseph Vendryes]], ainsi que le japonisant [[Charles Haguenauer]]. Antoine Meillet devait diriger la thèse de [[Jean Paulhan]] sur la sémantique du proverbe et c'est lui qui découvrit [[Gustave Guillaume]].

Il a influencé aussi un certain nombre de linguistes étrangers. Il a également été le premier à identifier le phénomène de la [[grammaticalisation]].

selon le [[Linguistique|linguiste]] allemand [[Walter Porzig]], Meillet est un « grand précurseur »<ref>{{article|langue=fr|auteur=Maurice Leroy|titre=Walter Porzig, Die Gliederung des indogermanischen Sprachgebiets|année=1955|numéro=1|volume=24|périodique=[[L'Antiquité classique]]|url=https://www.persee.fr/doc/antiq_0770-2817_1955_num_24_1_3260_t1_0216_0000_1|site=www.persee.fr|format=pdf|passage=216-217|consulté le=1 juillet 2020}}.</ref>. Il montre, par exemple, que, dans les dialectes indo-européens, les groupes indo-européens sont le résultat historique d'une [[Variation linguistique|variation diatopique]].

L’acte de naissance de la sociolinguistique est signé par Antoine Meillet fondateur de la sociolinguistique qui s’est opposé au Cours de linguistique générale de [[Ferdinand de Saussure]] dès son apparition en 1916 en le critiquant sur plusieurs plans.

== Études arméniennes ==
* [[1890]], une mission de trois mois dans le [[Caucase]] lui permet d'apprendre l'[[arménien]] moderne.
* [[1902]], il obtient la [[chaire d'arménien de l'École des langues orientales]].
* [[1903]], nouvelle mission en Arménie russe, il publie son ''Esquisse d'une grammaire comparée de l'arménien classique'', qui demeure une référence en linguistique arménienne et indo-européenne jusqu'à ce jour. L'un de ses étudiants, [[Hratchia Adjarian]], devient le fondateur de la dialectologie arménienne. C'est également sous les encouragements de Meillet qu'Émile Benveniste étudie la langue arménienne.
* [[1919]], il est cofondateur de la Société des études arméniennes avec Victor Bérard, Charles Diehl, André-Ferdinand Hérold, H. Lacroix, Frédéric Macler, Gabriel Millet, Gustave Schlumberger.
* [[1920]], le {{date-|19 janvier}}, il crée la ''[[Revue des études arméniennes]]'' avec [[Frédéric Macler]].

== Études homériques ==
À la Sorbonne, Meillet supervise le travail de [[Milman Parry]]. Meillet offre à son étudiant l'opinion, nouvelle à cette époque, que la structure formulaïque de ''[[l'Iliade]]'' serait une conséquence directe de sa transmission orale. Ainsi, il le dirige vers l'étude de l'oralité dans son cadre natif et lui suggère d'observer les mécanismes d'une tradition orale vivante à côté du texte classique (''[[l'Iliade]]'') qui est censé résulter d'une telle tradition. En conséquence, Meillet présente Parry à [[Matija Murko]], savant originaire de [[Slovénie]] qui avait longuement écrit sur la tradition héroïque épique dans les [[Balkans]], surtout en [[Bosnie-Herzégovine]]<ref>[[Mathias Murko]], ''La poésie populaire épique en Yougoslavie au début du {{s-|XX}}'' (Paris: Champion, 1929); Albert Lord, ''The singer of tales'' (Cambridge, Mass.: Harvard University Press, 1960), {{p.|11-12}}; Andrew Dalby, ''Rediscovering Homer'' (New York, London: Norton, 2006. {{ISBN|0-393-05788-7}}), {{p.|186-187}}.</ref>. Par leurs recherches, dont les résultats sont à présent hébergés par l'université de Harvard, Parry et son élève, [[Albert Lord]], ont profondément renouvelé les études homériques.

== Principaux ouvrages ==
* ''Esquisse d'une grammaire comparée de l'arménien classique'', [[1903]].
* ''Introduction à l'étude comparative des langues indo-européennes'', [[1903]] ({{1re}} éd.), Hachette, Paris, [[1912]] ({{3e}} éd.)<ref>Cet ouvrage, ainsi que l{{'}}''Aperçu d'une histoire de la langue grecque'' ont fait l'objet d'une critique par [[Lucien Febvre]], ''Antoine Meillet et l'histoire, La Grèce ancienne à travers l'histoire'', Revue de synthèse historique, 1913, {{p.|4-93}}, rééditée dans Lucien Febvre, ''Vivre l'histoire'', coll. Bouquins, Robert Laffont/Armand Colin, Paris, 2009, {{p.|136-145}}.</ref>.
* ''Les dialectes indo-européens'', [[1908]].
* ''Aperçu d'une histoire de la langue grecque'', [[1913]].
* ''Altarmenisches Elementarbuch'', [[1913]]. Heidelberg (en français : Manuel élémentaire d'Arménien classique, traduction de Gabriel Képéklian, Limoges, Lambert-Lucas, 2017 {{ISBN|978-2-35935-094-4}})
* ''Linguistique historique et linguistique générale'', [[1921]] (le tome II est paru en 1936 ; les deux tomes ont été réunis chez Lambert-Lucas, Limoges, 2015).
* ''Les origines indo-européennes des mètres grecs'', [[1923]].
* ''Traité de grammaire comparée des langues classiques'', [[1924]] (avec Joseph Vendryés).
* ''La méthode comparative en linguistique historique'', [[1925]], Oslo, Instituttet for Sammenlignende Kulturforskning (réimpr. Paris, Champion, 1954).
* {{Ouvrage|langue=fr|titre=Esquisse d'une histoire de la langue latine|lieu=Paris|éditeur=Klincksieck|année=1977|isbn=978-2-252-01871-2|isbn10=2-252-01871-2|bnf=345861423}}.
* ''Dictionnaire étymologique de la langue latine'', [[1932]] (en collab. Avec [[Alfred Ernout]] (1879-1973), éd. augmentée, par Jacques André (1910-1994), Paris : Klincksieck, 2001, {{ISBN|2-252-03359-2}} {{BNF|37707942}}
* ''Meillet en Arménie, 1891, 1903'', Journaux et lettres publiés par Francis Gandon, Limoges, Lambert-Lucas, 2014, {{ISBN|978-2-35935-071-5}}.

== Notes et références ==
<references />

== Voir aussi ==
{{Autres projets
|wikisource = Antoine Meillet
|commons = Category:Antoine Meillet
}}
=== Bibliographie ===
*[[Marc Décimo]], ''Sciences et pataphysique'', t. 2 : ''Comment la linguistique vint à Paris ?'', ''De Michel Bréal à Ferdinand de Saussure'', Dijon, [[Les presses du réel|Les Presses du réel]], coll. Les Hétéroclites, 2014 {{ISBN|978-2-84066-599-1}}.
*{{Article|langue=fr|prénom1=Anne-Marguerite|nom1=Fryba|titre=[[Maurice Grammont]], Antoine Meillet et l'institutionnalisation de la linguistique en France|périodique=Revue des langues romanes|numéro=105|année=2001|pages=503-517}}
* {{Chapitre|langue=fr|prénom1=Charles|nom1=de Lamberterie|lien auteur1=Charles de Lamberterie|titre chapitre=Milman Parry et Antoine Meillet|auteurs ouvrage=Françoise Létoublon (éd.)|titre ouvrage=Hommage à [[Milman Parry]]. Le style formulaire de l’épopée homérique et la théorie de l’oralité poétique|lieu=Amsterdam|éditeur=Gieben|année=1997}}
* {{Ouvrage|langue=fr|prénom1=Gabriel|nom1=Bergounioux|prénom2=Charles|nom2=de Lamberterie|titre=Meillet aujourd'hui|lieu=Louvain-Paris|éditeur=Peeters|année=2006|pages totales=356|isbn=978-90-429-1743-9}}

=== Articles connexes ===
* [[Franz Bopp]]
* [[Johann Kaspar Zeuss]]

=== Liens externes ===
* {{Autorité}}
* {{Dictionnaires}}
* {{Bases recherche}}

{{Portail|linguistique}}

{{DEFAULTSORT:Meillet, Antoine}}
[[Catégorie:Académie des inscriptions et belles-lettres]]
[[Catégorie:Agrégé de grammaire]]
[[Catégorie:Linguiste français]]
[[Catégorie:Philologue français]]
[[Catégorie:Slaviste]]
[[Catégorie:Naissance en novembre 1866]]
[[Catégorie:Naissance à Moulins (Allier)]]
[[Catégorie:Décès en septembre 1936]]
[[Catégorie:Décès dans le Cher]]
[[Catégorie:Décès à 69 ans]]
[[Catégorie:Institut national des langues et civilisations orientales]]
[[Catégorie:Arménologue français]]
[[Catégorie:Indo-européaniste]]
[[Catégorie:Étudiant de l'université de Paris]]
[[Catégorie:Personnalité inhumée à Moulins]]
[[Catégorie:Commandeur de la Légion d'honneur]]
   """

    wiki2plain = Wiki2Plain(wiki_page)
    content_text = wiki2plain.text

    print('---')
    print(content_text)
    print('---')
