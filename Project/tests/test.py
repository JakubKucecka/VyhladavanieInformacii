from lib import search
from lib import index
from nose.tools import *
from unittest import mock

input_file = '../../VI_data/freebase-rdf-latest.gz'
actors_file = "../etc/parse/actors.gz"
performances_file = "../etc/parse/performances.gz"
other_file = "../etc/parse/other.gz"
final_file = "../etc/parse/final.gz"
index_dir = "../etc/index"


def test_new_york_stories():
    test = sorted(
        ['Adele French', 'Alexandra Becker', 'Andrew MacMillan', 'Briz', 'Celia Nestell', 'Diane Lin Cosman',
         "Dylan O'Sullivan Farrow", 'Elana Cooper', 'Ernst Muller', 'George Schindler', 'Gina Scianni',
         'Gregorij von Leitis', 'Herschel Rosen', 'Jackie Enfield', 'JoJo Starbuck', 'Joan Bud', 'Lola André',
         'Lynda Lenet', 'Michael Rizzo', 'Phil Harper', 'Richard Grund', 'Robin Wood-Chappelle', 'Sarah Spiegel',
         'Selim Tlili', 'Selma Hirsch', 'Victor Trull', 'Annie Joe Edwards', 'George Rafferty', 'Jenny Nichols',
         'Lou Ruggiero', 'Thelma Carpenter', 'Jessie Keosian', 'Michael Powell', 'Bridgit Ryan', 'Amber Barretto',
         'Paul Geier', 'Rawleigh Moreland', 'Martin Rosenblatt', 'Marvin Chatinover', 'Gia Coppola', 'Ed Koch',
         'Peter Gabriel', 'Julia Campanelli', 'Molly Regan', 'F.X. Vitolo', 'David Cryer', 'Lo Nardo',
         'Nancy Giles', 'Paul Mougey', 'Richard Price', 'Brigitte Bako', 'Matthew T. Gitkin', 'Larry David',
         'Bill Moor', 'Kenneth McGregor', 'Carmine Coppola', 'Ira Wheeler', 'Jesse Borrego', 'Tom Mardirosian',
         'Heather McComb', 'Holly Marie Combs', 'Jodi Long', 'Don Novello', 'Helen Hanft', 'Debbie Harry',
         'Carole Bouquet', 'Michael Higgins', "Patrick O'Neal", 'Chris Elliott', 'Mae Questel', 'Джеймс Кин',
         'Julie Kavner', 'Talia Shire', 'Paul Herman', 'Illeana Douglas', 'Victor Argo', 'Martin Scorsese',
         'Mark Boone Junior', 'Adrien Brody', 'Rosanna Arquette', 'Woody Allen', 'Mia Farrow', 'Giancarlo Giannini',
         'Kirsten Dunst', 'Майк Старр', 'Nick Nolte', 'Steve Buscemi'])
    assert sorted(index.search_film(index_dir, "New York Stories")) == test


def test_lawless():
    test = sorted(['Haley Bennett', 'Rooney Mara', 'Michael Fassbender', 'Ryan Gosling', 'Benicio del Toro',
                   'Natalie Portman', 'Christian Bale', 'Val Kilmer', 'Cate Blanchett'])
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "2"
    output = sorted(index.search_film(index_dir, "Lawless"))
    assert output == test
    mock.builtins.input = original_input


def test_film_exit():
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "e"
    output = index.search_film(index_dir, "Lawless")
    assert output == -2
    mock.builtins.input = original_input


def test_input_not_find():
    output = index.search_film(index_dir, "Name not found, I think, This is bad name of film")
    assert output == -1


def test_correction_1():
    output1 = index.search_actor(index_dir, "Christian Bale")
    output2 = index.search_actor(index_dir, "christian bale")
    assert output1 == output2


def test_correction_2():
    output1 = index.search_actor(index_dir, "Christian Bale")
    output2 = index.search_actor(index_dir, "ChRisTiAn bALe")
    assert output1 == output2


def test_correction_2():
    output1 = index.search_actor(index_dir, "Christian Bale")
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "1"
    output2 = index.search_actor(index_dir, "Christiam Balee")
    assert output1['films'] == output2['films']
    mock.builtins.input = original_input


def test_actor_exit():
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "e"
    output = index.search_actor(index_dir, "Gary oldmanee")
    assert output == -2
    mock.builtins.input = original_input


"""
test actors with count from https://freebase-easy.cs.uni-freiburg.de/browse/#

example:
    https://freebase-easy.cs.uni-freiburg.de/browse/#triples=$1%20equals%20:e:Tom_Hardy;$1%20:r:Film_performance%20$2&active=3&additionalInfo=2%20null%20null
"""


def test_count_tom_hardy():
    output = index.search_actor(index_dir, "Tom Hardy")
    assert len(output['films'].split('@')) == 40


def test_count_christian_bale():
    output = index.search_actor(index_dir, "Christian Bale")
    assert len(output['films'].split('@')) == 49


"""
test movies with count from https://freebase-easy.cs.uni-freiburg.de/browse/#

example:
    https://freebase-easy.cs.uni-freiburg.de/browse/#triples=$1%20equals%20:e:New_York_Stories
"""


def test_count_new_york_stories():
    assert len(index.search_film(index_dir, "New York Stories")) == 87


def test_count_the_dark_knight_rises():
    assert len(index.search_film(index_dir, "The Dark Knight Rises")) == 284


def test_count_lawless_1():
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "1"
    assert len(index.search_film(index_dir, "Lawless")) == 46
    mock.builtins.input = original_input


def test_count_lawless_2():
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "2"
    assert len(index.search_film(index_dir, "Lawless")) == 9
    mock.builtins.input = original_input
