from utils import wiki_to_paintext, get_clean_tokens, deserialize, serialize
from paths import path_cli, path_pagelist_links, path_pagelist_clean_tokens, path_new_pagelist_clean_tokens

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

    page2 = """
    Lherméneutique (du grec hermeneutikè, ἑρμηνευτική τέχνη, art d'interpréter, hermeneuein signifie d'abord « parler », « s'exprimer » et du nom du dieu grec Hermès, messager des dieux et interprète de leurs ordres) est la théorie de la lecture, de l'explication et de l'interprétation des textes.

L'herméneutique ancienne est formée de deux approches complètement différentes : la logique d'origine aristotélicienne (à partir du Peri hermeneia ou De l'interprétation d'Aristote) d'une part, l'interprétation des textes religieux (orphisme ou exégèse biblique par exemple) et l'hermétisme d'autre part.

L'herméneutique moderne se décline en sous-disciplines :
* « littéraire » (interprétation des textes littéraires et poétiques),
* « juridique » (interprétation des sources de la loi),
* « théologique » (interprétation des textes sacrés; on parle aussi d'exégèse),
*« anthropologique » (interpréter la culture comme un texte; autrement appelée l'anthropologie interprétative)
* « historique » (interprétation des témoignages et des discours sur l'histoire) et
* « philosophique » (analyse des fondements de l'interprétation en général, et interprétation des textes proprement philosophiques).

== Définition générale ==
=== Champs de l'herméneutique ===
On parle d'« herméneutique » pour l'interprétation des textes en général.

L'interprétation des Écritures saintes, qu'il s'agisse de la Bible ou du Coran, est un sujet qui demeure délicat. L'interprétation des symboles religieux et des mythes s'appelle l'herméneutique sacrée (ou herméneutique biblique lorsqu'elle se limite à la Bible, c'est-à-dire aux textes du judaïsme et du christianisme). Elle se révèle nécessaire pour le philosophe et théologien Xavier Tilliette, selon lequel « la Bible est un ouvrage complexe et même scellé. Le Livre des livres est un livre de livres. Il est donc susceptible d'interprétation, il ne va pas sans une herméneutique. […] Il n'y a pas d'acheminement direct à la Bible, il faut toujours une médiation au moins implicite ».

L'interprétation de symboles divinatoires fait également appel à des herméneutes, comme en Chine et au Japon, lors de séances de scapulomancie, de plastromancie, d'achilléomancie ou autres formes d'arts divinatoires.

L'étude, la traduction et l'interprétation des textes classiques (antiques) naît à la Renaissance : c'est la philologie.

On désigne aussi par « herméneutique » la réflexion philosophique interprétative, inventée par Friedrich Schleiermacher, développée par Wilhelm Dilthey et rénovée par Martin Heidegger et Hans-Georg Gadamer.

L'herméneutique trouve des applications dans la critique littéraire ou historique, dans le droit, dans la sociologie, en musique, en informatique, en théologie (domaine d'origine), ou même dans le cadre de la psychanalyse. Cette dernière discipline fait néanmoins problème. Ainsi le psychanalyste Jean Laplanche n'admet-il pas que la psychanalyse se trouve « enrôlée » dans l'herméneutique comme .

=== Questions de méthodologie ===
La méthodologie du dévoilement ou de la restitution d'un texte pose deux questions :
* Quel statut donner aux scripteurs (car le terme d’auteur pose lui aussi des problèmes) du texte biblique ? Inspiration, diction (inerrance) ?
* Dans quelle mesure l’interprétation du lecteur doit-elle être prise en compte et est-elle valide (par rapport à la tradition religieuse et à une lecture collective représentative du groupe porteur de cette tradition) ?

== Histoire de l'herméneutique ==
=== L'« herméneutique » ancienne ===
L'herméneutique est aussi ancienne que le sont les religions, les spiritualités et la philosophie. Cependant, le terme d'herméneutique n'est apparu qu'à l'époque moderne sous la plume de Friedrich Schleiermacher et Wilhelm Dilthey.

==== D'Aristote à la science contemporaine ====
Dans son traité De l'interprétation (Organon II), Aristote ( av. J.-C) avait défini des règles essentiellement logiques d'interprétation des textes. Il y développe notamment sa théorie du jugement affirmatif et négatif, de la contradiction et de la contrariété. Son point de départ est l'analyse des éléments sémantiques :la lettre, le nom, le verbe, la proposition. Il aboutit à une métaphysique qui hiérarchise les degrés d'être, après avoir exposé la théorie des , laquelle influence les débats médiévaux sur le problème théologique de la prédestination.
Ce traité est abondamment commenté par les philosophes médiévaux Averroès, Thomas d'Aquin, Jean Duns Scot, Guillaume d'Ockham), et fixera pour longtemps la norme de lecture des textes.

Les herméneutes contemporains tels que Umberto Eco ou Paul Ricœur se réclament également de la philosophie aristotélicienne, mais davantage de la Poétique et de la Rhétorique que de lOrganon à proprement parler, ce dernier étant plutôt vu comme un prélude à l'élaboration du discours scientifique, que comme un ensemble de traités sur l'interprétation concrète des textes en général.

On peut mesurer ainsi le changement de paradigme de l'époque médiévale à l'époque contemporaine : la logique, c'est-à-dire l'ancienne herméneutique de lOrganon, est devenue la logique symbolique, tandis qu'une nouvelle herméneutique a émergé. Cette dernière explore des champs d'interprétation comme la poétique, la rhétorique, la littérature, mais aussi la sociologie, la psychologie, l'histoire, l'anthropologie. L'une des causes principales de ce changement est la naissance des sciences humaines qui livrent une autre approche du monde que celle des sciences naturelles et de la métaphysique traditionnelle.

Néanmoins, certains auteurs de la deuxième moitié du , comme Paul Feyerabend, soutiennent que le discours scientifique est lui aussi une interprétation du monde et que son mode de production ne diffère pas de celui des autres discours, littéraires, mythologiques.

En ce sens, aucun champ n'échapperait à l'herméneutique, pas même la science dite univoque, c'est-à-dire non sujette aux querelles d'interprétation, et rigoureuse, non affectée par la contingence des images humaines.

==== Stoïcisme ====
Les stoïciens développent un naturalisme herméneutique qui assimile les dieux comme représentations à des forces physiques.
: (Cicéron, De la nature des dieux, II, XXV-XXVI).

==== Judaïsme ====
La tradition du judaïsme rabbinique connaissait depuis longtemps des règles d'interprétation de la Torah. Hillel Hazaken ( AEC) avait défini sept règles d'interprétation. Rabbi Ishmaël, développant les sept règles d'Hillel, exposa treize principes.

D'autre part, le judaïsme rabbinique connaissait quatre sens (Pardes) pour interpréter la Bible hébraïque : peshat (évident, littéral), remez (allusif), drash (interprétatif), et sod (secret/mystique). Par exemple, le sens littéral (peshat) s'avérait souvent insuffisant pour comprendre en profondeur le sens des textes sacrés.

La kabbale, dès Eléazar de Worms et Abraham Aboulafia (vers 1290), a développé la science des lettres (hokhmat ha-zeruf) et ses trois procédés pour déchiffrer la Torah.

# La gematria dévoile la valeur numérique d'un mot ou d'une phrase pour révéler les équivalences avec les mots ou les phrases d'égale valeur. Selon J. Gikatella (mort en 1325), Echad (Un) vaut 13 (1 + 8 + 4) et, comme tel, il équivaut à Ahabah (Amour) (1 + 5 + 2 + 5).
# Le notarikon permet, à partir des lettres d'un mot (initiales, médianes, terminales), de construire des phrases consistant en des mots dont les initiales, mises bout à bout, reconstituent le mot d'origine, et donc en révèlent les significations secrètes. Ainsi, le nom Adam, formé des lettres alef, dalet, mem, renvoie à Adam, David, Messiah (Messie) pour dire qu'Adam engendrera David et de la lignée de David viendra le Messie.
# La temura consiste à substituer chaque lettre d'un mot ou d'un groupe de mots à une autre lettre conformément à un système de substitution. Par exemple, Bavel, "Babylone" devient Shéshak dans Jérémie XXV, 26, si la lettre tav (la dernière de l'alphabet) remplace sin (l'avant-dernière) et ainsi de suite.

Dans le judaïsme, la période médiévale a vu le développement de beaucoup de nouvelles catégories d'interprétation rabbinique et d'explication de la Torah, incluant l'émergence de la Kabbale et des écrits de Maïmonide. Les commentaires bibliques et les commentaires du Talmud s'inscrivent dans cette tradition.

==== Christianisme ====

La tradition chrétienne reprit la doctrine des quatre sens de l'Écriture en l'adaptant au christianisme. Origène au  l'appliqua à la prière (Lectio divina), puis Jean Cassien (dont s'inspire la fameuse règle de saint Benoît) la théorisa en l'introduisant dans les monastères.

La doctrine des quatre sens de l'Ecriture eut un succès important pendant tout le Moyen Âge : le sens allégorique, à la suite de Prudence, inspira une grande partie de la littérature médiévale profane. Elle joua un rôle important à la naissance de la scolastique. Hugues de Saint-Victor la connaissait (De Scripturis).

Pour le philosophe et théologien catholique Xavier Tilliette, « la Bible est un ouvrage complexe et même scellé. Le Livre des livres est un livre de livres. Il est donc susceptible d'interprétation, il ne va pas sans une herméneutique. La Parole de Dieu […] s'est faite parole humaine, astreinte à la compréhension. Il n'y a pas d'acheminement direct à la Bible, il faut toujours une médiation au moins implicite : traduction, exégèse, histoire, genres littéraires, étude des styles, typologie, connaissance de la Tradition, lectio divina »…

=== Renaissance ===
==== Retour à la littéralité ====

L'étude et l'interprétation des textes classiques (antiques) naît à la Renaissance : c'est la philologie. Les savants apprennent le grec et le latin, et développent des méthodes pour prouver l'authenticité ou l'inauthenticité d'un texte, et pour établir des éditions critiques des œuvres. C'est le retour aux sources et à la littéralité des textes. L'un des éminents représentants de cette nouvelle tendance est Guillaume Budé, illustre humaniste. L'une des victoires les plus éclatantes de la nouvelle philologie est la démonstration par Lorenzo Valla de la fausseté de la Donation de Constantin. Cet acte porte également une charge politique, car il démonte les fondements de l'autorité papale, qui s'appuyait sur ce fameux texte.

Sous la plume de Martin Luther et Jean Calvin, la Réforme protestante appelle à relire les textes religieux littéralement par-delà les interprétations canoniques de l'Église catholique romaine. Il s'agit de détruire les couches sédimentées de conciles et de doctrines (la tradition), surajoutées aux textes, pour retrouver le texte biblique en sa pureté. Auparavant, la majorité du peuple n'avait pas accès au texte biblique mais seulement aux interprétations qu'en donnaient les autorités religieuses. Avec les mouvements intellectuels de la Réforme et de l'Humanisme, conjoints à l'invention de l'imprimerie et au développement de l'éducation (qui fera reculer l'illettrisme), le texte biblique deviendra de plus en plus accessible et l'autorité religieuse de plus en plus remise en cause quant à la lecture des textes sacrés.

Paradoxalement, cette affirmation selon laquelle la Bible serait claire par elle-même, et donc à lire de manière littérale, amène le lecteur à réinterpréter lui-même le texte sacré sans qu'on ne lui impose des normes interprétatives rigides et incontestables. Le retour à l'« autorité » du texte littéral annonce la multiplicité « anarchique » des interprétations qui ne peuvent plus être unifiées par une autorité normative. L'herméneutique moderne naît de la destruction de la norme : s'il n'y a plus de norme de lecture extérieure au texte, il faut apprendre à déceler soi-même le mécanisme interne d'un texte donné qui produit lui-même son propre sens afin d'éviter la multiplication à l'infini des significations du texte en question, jusqu'à l'absurdité.

Ce retour à la littéralité sera illustré lors du procès de Galilée (1633) au cours duquel les théologiens privilégièrent le sens littéral de la Bible en l'absence de preuves du mouvement de la Terre. Il aura des conséquences considérables dans l'Histoire.

==== Astrologie et alchimie ====
Depuis le  au moins, le recours à la pensée magique est connu, mais il est vrai qu’il connaît une nouvelle mode au  quand Marsile Ficin édite le Corpus hermeticum, ensemble de textes anonymes du   et que l’on attribue à Hermès Trismégiste, fondateur légendaire de la religion égyptienne, contemporain de Pythagore et de Moïse. Dans cette pensée, le monde animé comme l'inanimé forme un tout continu qui possède une âme : il y a donc des correspondances entre l’Univers et l’Homme qui en est le centre et le reflet en même temps. On raisonne d’ailleurs par analogie : les plantes sont les cheveux du monde, par exemple. L'herméneutique joue ainsi un rôle important dans la médecine de la Renaissance, à la fois dans la pharmacopée (une plante correspondant à un organe) que dans les prescriptions, puisque souvent la consultation et surtout l'administration des médecines sont associées à l'horoscope du patient, les différentes parties du corps trouvant leur correspondance dans les signes zodiacaux.

On est persuadé de la vertu de certains minéraux ou éléments chimiques et notamment du mercure, du soufre. On est ainsi persuadé depuis le  qu’il existe un lien entre la pierre philosophale, qui peut transformer tout métal en or, et les calculs rénaux.
Le personnage le plus connu est Paracelse (1493-1541), fils de médecin, à la fois chimiste (travaillant dans les mines) et alchimiste, qui s’intéresse aux correspondances entre les minéraux et l’homme. Il est professeur de médecine à Bâle en 1526. Il a laissé de nombreuses recettes qui emploient l’opium mais aussi des composés minéraux.
Cette démarche explique également l’intérêt pour les traitements par les eaux thermales de Michel Savonarole (1385-1468) : De omnibus mundi balneis éditée en 1493 à Bologne. Plus tard, l’université de Padoue confie à trois de ses médecins de faire revivre les bains d’Abano, utilisés dans l’Antiquité ; le célèbre anatomiste Fallope qui enseigne à Padoue est chargé en 1556 d'un enseignement à thermalisme acquis.

=== Les précurseurs de l'herméneutique contemporaine ===
==== Schleiermacher ====
C'est Friedrich Schleiermacher (1768 – 1834) qui posa les bases de l'herméneutique contemporaine. Schleiermacher mit également en évidence le cercle herméneutique (l'expression est de Dilthey). Pour comprendre un texte, il faut avoir compris l'œuvre, mais pour comprendre l'œuvre, il faut avoir compris les textes.

==== Dilthey ====
Wilhelm Dilthey (1833 – 1911) voit dans l'herméneutique la possibilité d'une fondation pour les sciences humaines. Les sciences de la nature ne cherchent qu'à « expliquer » (Erklären) leur objet, tandis que les sciences de l'homme, et l'histoire en particulier, demandent également à « comprendre » (Verstehen) de l'intérieur et donc à prendre en considération le vécu.

===  ===

==== Naissance de l'herméneutique philosophique ====
L'herméneutique philosophique contemporaine se conçoit comme une théorie de l'interprétation, et de la réception de l'œuvre (littéraire ou artistique). Elle questionne la textualité en elle-même, et son rapport à l'auteur (processus d'explication) et au lecteur (processus de compréhension).

L'herméneutique philosophique cherche à analyser ce qui se manifeste, ce qui se présente de soi dans l'œuvre d'art (perspective phénoménologique). Elle pose donc de manière originale le problème de la représentation et de la phénoménalisation, s'inspirant en cela des travaux novateurs de Husserl (lequel avait livré une théorie très élaborée de l'imagination, notamment dans les Ideen I, à défaut d'esthétique à proprement parler).

Le langage de l'art représente pour les herméneutes le lieu où la vérité de l'Être se déploie, au-delà de la description scientifique des étants particuliers. L'herméneutique se fonde ainsi sur une nouvelle interrogation du verbe « être », à la fois grammaticale, ontologique et esthétique, à partir des importants travaux de Martin Heidegger dans Être et Temps (et dans ses œuvres ultérieures, dont la tentation hermétiste sera critiquée).

L'herméneutique philosophique utilise comme paradigme majeur la poésie, notamment la poésie romantique, symboliste, surréaliste ou d'inspiration hermétiste, c'est-à-dire la poésie qui ne se comprend pas à la première lecture, mais qui nécessite un effort pour être décryptée. Les philosophes herméneutes analysent par exemple les textes et l'esprit de Hölderlin, Mallarmé, Valéry, Rilke, Artaud ou encore Ponge.

Le deuxième grand paradigme de l'herméneutique est le roman, notamment les œuvres subversives qui remettent en cause les normes traditionnelles d'écriture. Ainsi, on croisera sous la plume des grands herméneutes Rabelais, le Marquis de Sade, Joyce, Kafka, Bataille, ou encore d'autres grands écrivains comme Goethe ou Borges.

==== Heidegger ====

Martin Heidegger étend la conception de Dilthey et conçoit à un certain moment l'herméneutique comme la tâche même de la philosophie si l'existence – objet de la philosophie – demande à être interprétée et si elle n'est autre qu'un processus d'interprétation, une compréhension de soi. L'herméneutique est en ce sens un dépassement de la phénoménologie car elle s'applique à ce qui ne se montre pas, à détruire plutôt un rapport de conscience qui dissimule un rapport authentique à l'être. L'herméneutique constitue ainsi l'ontologie.

==== Gadamer ====
L'élève de Heidegger, Hans-Georg Gadamer publia en 1960 l'ouvrage qui passe encore pour son livre le plus important : Vérité et Méthode.

Cette œuvre affirme, en contestation de la fausse objectivité souvent présente dans les sciences humaines, que « la méthode ne suffit pas ». Une œuvre ne peut pas être expliquée uniquement selon notre propre horizon d'attente. La lecture est faite dans la tension existant entre le texte du passé et l'horizon d'attente actuel.

De plus, Gadamer affirme que « tout texte est réponse à une question. » Si le texte parle encore aux lecteurs présents, c'est qu'il répond encore à une question. Le travail de l'historien est de trouver à quelle question le texte répondait dans le passé et à laquelle il répond aujourd'hui.

==== Ricœur ====
Paul Ricœur entreprend une herméneutique du soi, herméneutique dans la mesure où le moi ne se connaît pas par simple introspection, mais par un ensemble de symboles. Il s'agit de déchiffrer le sens caché dans le sens apparent.

Pour Ricoeur, la psychanalyse est une forme d'herméneutique (interprétation des symptômes du malade).

==== Jauss ====
Hans Robert Jauss, appartenant à l'École de Constance, dans Pour une esthétique de la réception (1972), reprenant les enseignements de Gadamer, affinera la théorie herméneutique. Il proposera l'usage d'une « triade » herméneutique pour l'étude des œuvres.

La triade herméneutique de Jauss :
# Linterprétation du texte où il faut réfléchir, rétrospectivement et trouver les significations.
# La reconstruction historique, où l'on cherche à comprendre l'altérité portée par le texte.
# La compréhension immédiate du texte, de sa valeur esthétique et de l'effet que sa lecture produit sur soi-même.

L'herméneute qui utilise ce modèle s'implique donc énormément dans l'étude et tente de comprendre la valeur novatrice de l'œuvre.

==== Foucault ====
En 1982, Michel Foucault intitule son cours au Collège de France : « herméneutique du sujet ». Il est question en réalité d’une « herméneutique de soi » au sens d’une forme de connaissance de soi. La notion fondamentale est la pensée grecque de lepimeleia heautou (le souci de soi). Cette question est en même temps esthétique : une « esthétique de l’existence » entendue comme une éthique, soit la production de normes qui ne soient pas cryptées, mais que le sujet fonde ou découvre, et par lesquelles il se découvre également.

Foucault considère que la « généalogie » nietzschéenne, qui interprète les jugements de valeur (vrai/faux, bien/mal, beau/laid) à partir de l'histoire et de la physiologie (état de santé du corps), est une herméneutique.

== Applications de l'herméneutique ==
=== Traductologie ===
L'herméneutique est en traductologie une approche de la traduction à part entière ayant comme figure de proue le linguiste allemand Friedrich Schleiermacher (1767-1834). Schleiermacher conçoit l’herméneutique traductionnelle comme un acte d'immersion du traducteur dans la psyché de l'auteur. Il s'agit d'une méthode de traduction empathique, qui insiste sur l'importance de ressentir le texte à traduire. Prétendant proposer une alternative à l'approche linguistique de la discipline, l'approche herméneutique décompose l'acte de traduction en quatre stades et non trois : "un élan de confiance", "l'incursion, l'agression, l'extraction", "l'incorporation au sens fort du terme" et "une réciprocité qui recréée l'équilibre".

=== Sociologie ===
La sociologie herméneutique consiste en la recherche de la compréhension des phénomènes dans leur singularité. Elle est l'art de retranscrire un discours afin d'en extraire les besoins des individus, une sorte de traduction des discours.

=== Anthropologie ===
Pour l'anthropologie interprétative, découlant de l'herméneutique, les faits étudiés sont le produit des réflexions des personnes qui leur sont rattachées. Pour Gagnon, l'anthropologue adoptant une approche herméneutique cherche alors « les connaissances, les représentations, les règles et les attentes que la culture met à la disposition des individus pour leur permettre de donner sens à leurs actions, pour décrire et expliquer le monde (dimension sémantique) mais aussi pour agir, produire quelque chose, résoudre un problème (dimension pragmatique)». Pour être valides socialement, les significations doivent être partagées, à la manière d'un texte public, et la société les garde pour les retransmettre de génération en génération en les adaptant plus ou moins au contexte. Le rôle de l'anthropologue est alors de lire la culture et de l'interpréter à la manière de ce qu'une lectrice ou un lecteur ferait, notamment en rendant clair ce qui est sous-entendu ou présupposé, comme ce que propose Taylor puisque les discours et dialogues contiennent une certaine quantité d'informations tenues pour acquises. Cette méthodologie n'est toutefois pas neutre. Gagnon souligne quelques limites, comme le fait que l'anthropologue est en soi interprète et doit tenir compte de ses propres préjugés culturels et de ses préconceptions issus de sa culture d'origine.

=== Droit ===

=== Informatique ===
Les chercheurs en informatique, particulièrement ceux qui traitent de linguistique informatique, d'ingénierie des connaissances, d'intelligence économique, et de protocoles d'analyse, n'ont pas manqué de remarquer la communauté d'intérêt qu'ils partagent avec les chercheurs en herméneutique, par rapport au caractère des agents d'interprétation et à la conduite des activités d'interprétation. Par exemple, dans leur résumé de mémoire en intelligence artificielle en 1986, Mallery, Hurwitz, et Duffy ont déclaré ce qui suit :

« L'herméneutique, qui est une branche de la philosophie continentale européenne traitant de la compréhension et de l'interprétation humaine de textes écrits, offre une puissance de discernement qui peut contribuer à la compréhension de la signification, à la traduction, aux architectures pour la compréhension du langage naturel, et même aux méthodes qui conviennent pour la recherche scientifique en intelligence artificielle. » (Mallery, Hurwitz, Duffy, 1986).

=== Relations internationales ===
L'herméneutique en relations internationales a connu un regain d'attention avec la fin de la guerre froide. Ceci s'explique par la multiplicité des théories déployées et leur incapacité, par la pensée rationnelle, à expliquer dans leur globalité les rapports internationaux. Dans un esprit de synthèse, certains auteurs redécouvrent la pensée de Gadamer, tel Richard Rorty, pour l'appliquer à la philosophie politique.

Cette philosophie « se débarrasse de la théorie classique de l'homme-connaisseur-des-essences », c'est-à-dire de la vérité par correspondance et met l'accent sur le contexte spatio-temporel de toute théorie et sur l'intentionnalité des auteurs. L'acte de comprendre se décompose alors en trois étapes qui forment le cercle herméneutique : la compréhension stricto sensu, l'interprétation et l'application (confrontation avec le réel par cohérence). Cette dernière étape participe à la notion de réflexivité en science sociale.

Rorty insiste sur le holisme du cercle herméneutique qui fait que tout penseur doit envisager un système dans sa totalité pour en comprendre les parties, et inversement, comprendre toutes les parties pour saisir le fonctionnement du Tout.

Appliqué aux relations internationales, la constructiviste Martha Finnemore voit dans l'herméneutique une invitation à la confrontation paradigmatique, pour approcher au plus près la réalité. De plus, la vérité étant nécessairement établie par cohérence, il y aura toujours un décalage entre l'environnement représenté des acteurs et l'environnement réel. Question qui renvoie à la théorie de Robert Jervis sur les fausses perceptions. Enfin, la compréhension du monde, compris comme un complexe "Tout-unités", amène nécessairement à concilier holisme et individualisme méthodologique.

=== Religion et théologie ===
* S'agissant de l'herméneutique de la vie facticielle appliquée à la religion voir

* Dans le domaine des sciences bibliques, on appelle herméneutique le discours de la méthode de l'exégèse biblique : comment il est possible d'interpréter les textes anciens qui composent la Bible. Dans l'Église catholique, la Commission biblique pontificale a publié en 1993 un document présentant les règles de cette herméneutique.

Mircea Eliade, comme un historien des religions et un herméneute, comprend la religion comme « l'expérience du sacré », et interprète le sacré par rapport au profane. Le savant roumain souligne que la relation entre le sacré et le profane n'est pas d'opposition, mais de complémentarité, ayant interprété le profane comme une hiérophanie. L'herméneutique du mythe est une partie de l'herméneutique de la religion. Le mythe ne doit pas être interprété comme une illusion ou un mensonge, parce qu'il y a une vérité dans le mythe à redécouvrir. Le mythe est interprété par Mircea Eliade comme « une histoire sacrée ». Il a introduit le concept de « l’herméneutique totale ».

====  : résurrection des quatre sens ====
En matière d'herméneutique biblique, et à la suite des travaux du cardinal Henri de Lubac, s.j., sur l'exégèse médiévale, la théorie des quatre sens de l'Écriture semble renaître chez les théologiens contemporains. Le cardinal Urs von Balthasar écrivait à ce sujet en 1970 :
: « Les quatre sens de l’Écriture célèbrent leur résurrection cachée dans la théologie d'aujourd'hui : en effet le sens littéral apparaît comme celui qu'il faut faire émerger en tant qu'historico-critique ; le sens spirituel en tant que kérygmatique, le sens tropologique en tant qu'essentiel et le sens anagogique en tant qu'eschatologique ».

== Notes et références ==

== Voir aussi ==
=== Bibliographie ===

* Aristote, De l'interprétation (Catégories. De l'interprétation : Organon I et II, éd. Vrin, trad. Tricot, 2000 )
* Raymond Aron, Dimension de la conscience historique, Éditions Plon, Paris, 1961, (Réédition : Agora, Paris, 1998, 
* Rudolf Bultmann, Origine et sens de la typologie considérée comme méthode herméneutique, Trad. par Marc B. de Launay. in: Philosophie, 1994 (11), 42, .
* (éd.) Larisa Cercel, Übersetzung und Hermeneutik / Traduction et herméneutique, Bucarest, Zeta Books, 2009, .
*  Wilhelm Dilthey, Das Wesen der Philosophie, Préface d'Otto Pöggeler, Hambourg, Meiner, 1984.
* Gilbert Durand, L'imagination symbolique, 132 p., Presses Universitaires de France, Collection Quadrige Grands textes, Paris, 2003, 
* Carsten Dutt, Herméneutique - Esthétique - Philosophie pratique, Dialogue avec Hans-Georg Gadamer, traduit de l'allemand par Donald Ipperciel, Fides, Québec, 1995
* Michel Foucault, L'herméneutique du sujet, Paris, Seuil, 2001.
* Michel Foucault, Histoire de la sexualité 3: Le souci de soi, Paris, Gallimard, 1984.
* P. Fruchon, « Herméneutique, langage et ontologie », Archives de philosophie, 36, 1973, 
* Hans-Georg Gadamer, Le problème de la conscience historique, P.U.L., Louvain, 1936 (Réédition : Le Seuil, Collection Trâces écrites, 96p., Paris, 1998, 
* Hans-Georg Gadamer, L'art de comprendre. Herméneutique et tradition philosophique, traduction par Marianna Simon, 295 p., Aubier Montaigne, Paris, 1982
* Hans-Georg Gadamer, Vérité et méthode, Édition intégrale rev. et complétée, 533 p., Éditions Le Seuil, Paris, 1996, 
* Hans-Georg Gadamer, Rhétorique, herméneutique et Critique de l'idéologie. Commentaires métacritiques de Wahrheit und Method, Article dans Archives de philosophie, 34, avril - juin 1971, .
* Hans-Georg Gadamer, Le défi herméneutique, Article dans Revue Internationale de Philosophie, 151, 1984, 
* Jean Grondin, L'universalité de l'herméneutique, 272 , Epiméthée, P.U.F., Paris, 1993
* Jean Grondin, L'herméneutique, PUF, "Que sais-je ?", 2006.
* Georges Gusdorf, Les origines de l’herméneutique, Collection : Les Sciences humaines et la pensée occidentale, 1988.
* Martin Heidegger, Ontologie. Hermeneutik der Faktizität (Cours de 1923), GA 23, 1988.
* Hans Robert Jauss, Pour une esthétique de la réception, 305 p., Gallimard, Collection Tel, Paris, 1990, 
* Hans Robert Jauss, Pour une herméneutique littéraire, 457 p., Gallimard, Collection Bibliothèque des idées, Paris, 1988, 
* Jacques Lacan, Écrits, Seuil, Champ freudien, 1966.
* Jean Laplanche, « La psychanalyse comme anti-herméneutique », dans Entre séduction et inspiration: l'homme, Paris, Quadrige/PUF, 1999 
* Pascal Michon, Poétique d'une anti-anthropologie. L'herméneutique de Gadamer, Paris, Vrin, 2000.
* Friedrich Nietzsche, La généalogie de la morale, Gallimard, Folio essais, 1985.
* Guillaume Paugam, La Philosophie et le problème du langage. Linguistique, Rhétorique, Herméneutique, Hermann, Philosophie, 2011.
*  Otto Pöggeler, Schritte zu einer hermeneutischen Philosophie, Alber, 1994.
* Otto Pöggeler et François Gauvin, Que peut encore l'herméneutique pour la philosophie. Entretien avec Otto Pöggeler, Laval théologique et philosophique, 1997, vol. 53, 1, [http://cat.inist.fr/?aModele=afficheN&amp;cpsidt=2864225].
* Paul Ricœur, De l'interprétation. Essai sur Freud, 536 p., Éditions Le Seuil, Collection L'Ordre philosophique, Paris, 1965, 
* Paul Ricœur, Le conflit des interprétations, 500 p., Éditions Le Seuil, Collection Esprit, Paris, 1969, 
* Friedrich Schleiermacher, Herméneutique, éd. Le Cerf, 1989.
* Gunter Scholtz, La philosophie herméneutique de Gadamer et les sciences humaines, traduction de J.-C. Gens, dans L’Héritage de H.-G. Gadamer, numéro spécial dirigé par G. Deniau et J-C. Gens, Éditions du Cercle herméneutique, Collection Phéno, Paris, 2003, .
* André Stanguennec, La réception du structuralisme dans l'herméneutique de P. Ricœur, Bulletin du Centre d'études hégéliennes et dialectiques, CEHD, Neuchâtel, Suisse, mai 1992
* André Stanguennec, L'appropriation de l'histoire chez H-G Gadamer, dans L’Héritage de H.-G. Gadamer, numéro spécial dirigé par G. Deniau et J-C. Gens, Éditions du Cercle herméneutique, Collection Phéno, Paris, 2003
* Revue Le Cercle Herméneutique 
* Gagnon Éric (2018) "Interprétation", in Anthropen.org, Paris, Éditions des archives contemporaines.

=== Articles connexes ===
==== Origines ====
* Sept principes d'Hillel
* Treize principes de Rabbi Ishmaël
* Midrash
* De l'interprétation (second livre de l'Organon d'Aristote)
* Quatre sens de l'Écriture

==== Thèmes en relation ====
* Pragmatique
* Sens | Signe | Symbole
* Interprétation
* Imaginaire
* Anagogie
* Théories de la réception et de la lecture selon l'école de Constance
* Heidegger et l'herméneutique
* Philosophie du langage

==== Applications ====
* Linguistique informatique (logiciels informatiques)
* Réception critique (littérature et théâtre)

=== Liens externes ===
* 
* « Paul Ricoeur, Cinq études herméneutiques », recension par Benjamin Fabre, Archives de sciences sociales des religions, n° 176, octobre-décembre 2016.
*  Larisa Cercel, Auf den Spuren einer verschütteten Evidenz: Übersetzung und Hermeneutik, dans: Larisa Cercel (éd.), Übersetzung und Hermeneutik / Traduction et herméneutique, Bucarest, Zeta Books, 2009, .
*  Définition de l'Encyclopédie Universalis.

Catégorie:Branche de la philosophie
Catégorie:Concept philosophique
Catégorie:Courant philosophique
Catégorie:Analyse littéraire
Catégorie:Analyse artistique
Catégorie:Méthode d'analyse
    """

    # text = wiki_to_paintext(wiki_page)

    # print('####################################')
    # print(text)
    # print('####################################')

    # clean = get_clean_tokens("Alfred de Musset", False)
    # print('####################################')
    # print(clean)
    # print('####################################')
    # print(" * Start deserialize CLI")
    # (C, L, I) = deserialize(path_cli)
    # print(" * Start deserialize links pagelist")
    # pagelist_links = deserialize(path_pagelist_links)
    # print("break")

    print("Start deserialize clean tokens pagelist")
    pagelist_clean_tokens = deserialize(path_pagelist_clean_tokens)

    print("Start deserialize new clean tokens pagelist")
    new_pagelist_clean_tokens = deserialize(path_new_pagelist_clean_tokens)

    print("break")
