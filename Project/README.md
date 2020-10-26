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
  - ak zadame mena **Tricky Sam Nanton** a **Utz Krause** zizstime, ze spolu nemohli hrat pretoze nezili v jednom obdobi
  - ak zadame mena **Bill Moor** a **Utz Krause** zistime, ze spolu nikde nehrali
 
Mena mozeme zadavat roznym sposobom, program nie je zavisli od velosti pismena.
