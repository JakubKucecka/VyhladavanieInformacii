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

## Priklady
Mam pripravene tri pkrilady:
  - ak zadame mena **Bill Moor**, **Carole Bouquet** alebo **Victor Argo** program vypise v akom filme spolu hrali
```python
Enter first name: Bill Moor
Enter second name: Victor argo
Actors: 
	Bill Moor -> Bill Moor, William H Moor III
	Victor argo -> Victor Argo, Victor Jimenez, Vic Argo, Víctor Jiménez
played together in films:
	Hanky Panky czyli ważna sprawa -> Hanky Panky czyli ważna sprawa, Hanky Panky, Ki kém, ki nem kém, Hokus Pokus czyli ważna sprawa, Masum Sanık, La Folie aux trousses
	New York Stories -> New York Stories, Nowojorskie opowieści, Historias de Nueva York, New York Üçlemesi, Histórias de Nova Iorque, Contos de Nova York, Històries de Nova York, New Yorker Geschichten
	...
	Enter first name: Bill Moor
Enter second name: Carole Bouquet
Actors: 
	Bill Moor -> Bill Moor, William H Moor III
	Carole Bouquet -> Carole Bouquet, Карол Буке, Кароль Буке, Carole Bouquetová
played together in films:
	New York Stories -> New York Stories, Nowojorskie opowieści, Historias de Nueva York, New York Üçlemesi, Histórias de Nova Iorque, Contos de Nova York, Històries de Nova York, New Yorker Geschichten
```
  - ak zadame mena **Tricky Sam Nanton** a **Utz Krause** zizstime, ze spolu nemohli hrat pretoze nezili v jednom obdobi
```python
Enter first name: Utz Krause
Enter second name: Tricky Sam Nanton
Actors:
	Utz Krause -> 1955-04-16-1998-01-07
	J. Nanton -> 1904-02-01-1946-07-20
Actors could not play together because they did not live at the same time
```
  - ak zadame mena **Bill Moor** a **Utz Krause** zistime, ze spolu nikde nehrali
 ```python
Enter first name: Bill Moor
Enter second name: Utz Krause
Actors Bill Moor and Utz Krause did not play together
```

Mena mozeme zadavat roznym sposobom, program nie je zavisli od velosti pismena.
