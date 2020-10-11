# F14 - Studentsky projekt na predmet Vyhladavanie informacii

Na spustenie projetu je potrebne si vyklonovat tento repozitar a prepnut sa do zlozky Project.
  - **git clone https://github.com/JakubKucecka/VyhladavanieInformacii.git**
  - **cd VyhladavanieInformacii/Project**

Nasledne staci spustit priaz na spustenie scriptu starter.py.
  - **python starter.py** alebo **python3 starter.py** podla vasej verzie Pythonu

Naslendne sa nas to opyta na zopar otazkok, kde je potrebne vzdy zadat "y" ako yes a ak sa nas opyta na mena ta zadat mena.

## Prva implementacia
V prvej implementacii mam v subore Project/tmp/tmp_film.gz ukazkovy zoparriadkovy archiv, z ktoreho budeme citat.

Mam pripravene tri pkrilady:
  - ak zadame mena **Bill Moor**, **Carole Bouquet** alebo **Victor Argo** program vypise v akom filme spolu hrali
  - ak zadame mena **Tricky Sam Nanton** a **Utz Krause** zizstime, ze spolu nemohli hrat pretoze nezili v jednom obdobi
  - ak zadame mena **Bill Moor** a **Utz Krause** zistime, ze spolu nikde nehrali
 
Mena mozeme zadavat roznym sposobom, program nie je zavisli od velosti pismena.
