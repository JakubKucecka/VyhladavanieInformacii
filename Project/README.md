# F14 - Studentsky projekt na predmet Vyhladavanie informacii

Na spustenie projetu je potrebne si vyklonovat tento repozitar a prepnut sa do zlozky Project.
  - **git clone https://github.com/JakubKucecka/VyhladavanieInformacii.git**
  - **cd VyhladavanieInformacii/Project**

Nasledne staci spustit priaz na spustenie scriptu starter.py.
  - **python starter.py** alebo **python3 starter.py** podla vasej verzie Pythonu

Naslendne sa nas to opyta na zopar otazkok, kde je potrebne vzdy zadat "y" ako yes a ak sa nas opyta na mena ta zadat mena.

## Prva implementacia
V prvej implementacii mam v subore Project/tmp/parse/tmp_film.gz ukazkovy zoparriadkovy archiv, z ktoreho budeme citat. Tento subor sa postupne rozbija do suborov Project/tmp/parse/actor.gz a Project/tmp/parse/other.gz. A tieto zasa postupne spojim do vysledneho suboru Project/tmp/parse/final.gz, z ktoreho sa vyhladava.

## Druha implementacia
V druhej implementacii mam v subore Project/tmp/parse/film_dump_from_freebase_rdf.gz archiv o veľosti 1.2G (rucne vytvorený dump udajov s retazcom ".film" z celeho FreeBase suboru), z ktoreho budeme citat. Tento subor sa postupne rozbija do suborov Project/tmp/parse/actor.gz a Project/tmp/parse/other.gz. A tieto zasa postupne spojim do vysledneho suboru Project/tmp/parse/final.gz, z ktoreho sa vyhladava. Dopracoval som dumpovanie vsetkych mien a aliasov osob a mien filmov.

Bohuzial tieto subory nevojdu na git.

Podla zmien pri dumpovani som upravil aj vyhladavanie.

## Tretia implementacia 
V tretej implementacii pracujem uz s celymi datam, ktore som raz presiel a rozdelil do suborov, actor. gz, performance.gz a film.gz. Nasledne som udaje z tychto suborov pospajal do struktur a tie som zapisal do vysledneho final.gz súboru. Tu sa dostavame  najpodstatnejsej zmene. 

Zapracoval som indexy pomocou kniznice Whoosh. Mam teda jeden index, ktory ma polia "names", "data" a "films". v "names" su indexovane mena a aliasy, v "data" su uložene datumy, ktore neindexujem a vo "films" su ulozene nazvy aliasy a id filmu, toto sa tiez indexuje. Polia, ktore sa indexuju su typu Text a pouzivam SimpleAnalyzer, ktory za frazu berie vsetko z pola *[\w,.\"\\\-:\'_ ]*. 

Nasledne som zapracoval vyhladavanie aj pomocou pola "names" aj pola "films". Co sa da vyhladat najdeme v prikladoch. Mam tiez zapracovany autocorrect na max dve chyby.

Vymazal som znaky ine ake su v latinke a azbuke.

## Priklady
Mam pripravene tri pkrilady:

  - ak zadame mena **Carole Bouquet** alebo **Victor Argo** program vypise v akom filme spolu hrali
```python
Enter first name: carole bouquet

Enter second name: victor argo

Actors: 
	carole bouquet -> Carole Bouquet, Карол Буке, Кароль Буке, Carole Bouquetová
	victor argo -> Victor Argo, Victor Jimenez, Vic Argo, Víctor Jiménez
played together in films:
	New York Stories -> Nowojorskie opowieści, Historias de Nueva York, New York Üçlemesi, Нью-йоркские истории, Нюйоркски истории, Histórias de Nova Iorque, Contos de Nova York, Històries de Nova York, New Yorker Geschichten
```

  - ak zadame mena **Tricky Sam Nanton** a **Utz Krause** zizstime, ze spolu nemohli hrat pretoze nezili v jednom obdobi
```python
Enter first name: tricky sam nanton

Enter second name: utz krause

Actors:
	tricky sam nanton -> born: 1904-02-01 died: 1946-07-20
	utz krause -> born: 1955-04-16 died: 1998-01-07
Actors could not play together because they did not live at the same time
```

  - ak zadame mena **Victor Argo** a **Utz Krause** zistime, ze spolu nikde nehrali
```python
Enter first name: victor argo

Enter second name: utz krause

Actors played in:
	victor argo -> Tagebuch einer Verführung, Smoke - Raucher unter sich, Caminho sem volta, После работы, Geç Kalan Sevgi, Angyali szemek, Jej alibi, Bad Lieutenant, The Last Temptation of Christ, Next Stop Wonderland, Beautiful But Deadly, A Family Matter, Coyote Ugly, Hanky Panky czyli ważna sprawa, King of New York, The Rose, Fast Food, Fast Women, Standard Time, Os Cavaleiros do Asfalto, Blue in the Face, Pohřeb, El tren de Bertha, Il nostro Natale, Coming Soon, Em Fuga, Lulu on the Bridge, Неприятности с обезьянкой, Sirovi ugovor, Dangerous Game, Sound of Silence, Coyote Ugly, Schatten und Nebel, Um Anjo de Mulher, Ghost Dog : La Voie du samouraï, Le Prix du silence, Taksista, Double Whammy, New York Stories
	utz krause -> Lola rennt
Actors did not play together
```

  - ak zadame meno **Bill Moor**, najdeme dvoch a preto sa nas system opyta toreho Billa chceme
```python
Enter first name: bill moor
I find more then one bill moor, didn't you mean?
	[1] bill moor -> Bill Moor -> born: 0001-01-01 died: NOW
	[2] bill moor -> Bill Moor, William H Moor III -> born: 1931-07-13 died: 2007-11-27
Enter num of actor or 'e' for end: 2
```

  - ak zadame **zle meno**, opravy ho a opyta sa nas, ktore podla ponuy chceme
```python
Enter first name: utz rause
I didn't find utz rause, didn't you mean?
	[1] utz rause -> Utz Krause -> born: 1955-04-16 died: 1998-01-07
Enter num of actor or 'e' for end: 1
```

  - ak zadame **nazov filmu*** vypise sa zoznam hercov
```python
Enter name of movie: new york stories

In film new york stories played:
    ...
	Paul Mougey
	Rawleigh Moreland
	Richard Price
	Brigitte Bako
	Matthew T. Gitkin
	Paul Geier
	Larry David
	Bill Moor
    ...
	Carole Bouquet
    ...
	Victor Argo
	...
```

  - ak sa stane, ze **dva alebo viacero filmov sa vola rovnako**, opyta sa nas aky film chceme
```python
Enter name of movie: lawless
I find more then one lawless, didn't you mean?
	[1] lawless -> Des hommes sans loi, Lawless, Země bez zákona, Bezakonje, The Wettest County, Gangster, În afara legii, In afara legii, Без закона, Wettest County, Laittomat, Dos Homens Sem Lei, The Wettest County in the World, Zem bez zákona, Virš įstatymo, The Promised Land, Bez zakona, Os Infratores, Fékezhetetlen, Kanunsuzlar, Laglöst land, Самый пьяный округ в мире
	[2] lawless -> Lawless, Weightless, Untitled Terrence Malick project, Cím nélküli Terrence Malick terv, Untitled Terrence Malick Project
Enter num of movie or 'e' for end:
```

  - ak zadame nazov filmu, ktory **nenasiel**, opravi ho a opyta sa, ci sme mysleli tento
```python
Enter name of movie: new yor stories
I didn't find 'new yor stories', didn't you mean 'new york stories'? [y|n]:
```

Mena mozeme zadavat roznym sposobom, program nie je zavisli od velosti pismena ale nevieme vyhladavat iba **cast nazvu**.

## Vyhodnotenie
Vyhodnotenie budem robit pomocou [stranky](https://freebase-easy.cs.uni-freiburg.de/browse/#triples=$1%20is-a%20:e:Award_Winner;$2%20:r:Artist%20$1&additionalInfo=2%20null%20null&nofhits=24). Kde vyberiem nahodnu vzoru mien a preliam, ci sa zonamy rovnaju.
