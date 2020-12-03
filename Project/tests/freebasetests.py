import sys
sys.path.insert(1, '../')
from lib import index
from unittest import mock

index_dir = "../etc/index"


"""
test actors with count from https://freebase-easy.cs.uni-freiburg.de/browse/#

example:
    https://freebase-easy.cs.uni-freiburg.de/browse/#triples=$1%20equals%20:e:Tom_Hardy;$1%20:r:Film_performance%20$2&active=3&additionalInfo=2%20null%20null
"""


def test_count_actor_1():
    output = index.search_actor(index_dir, "Tom Hardy")
    assert len(output['films'].split('@')) == 40


def test_count_actor_2():
    output = index.search_actor(index_dir, "Christian Bale")
    assert len(output['films'].split('@')) == 49


def test_count_actor_3():
    output = index.search_actor(index_dir, "Ashton Kutcher")
    assert len(output['films'].split('@')) == 28


def test_count_actor_4():
    output = index.search_actor(index_dir, "Robert Downey Jr.")
    assert len(output['films'].split('@')) == 72


def test_count_actor_5():
    output = index.search_actor(index_dir, "Johnny Depp")
    assert len(output['films'].split('@')) == 66


def test_count_actor_6():
    output = index.search_actor(index_dir, "Brad Pitt")
    assert len(output['films'].split('@')) == 63


def test_count_actor_7():
    output = index.search_actor(index_dir, "Robert De Niro")
    assert len(output['films'].split('@')) == 105


def test_count_actor_8():
    output = index.search_actor(index_dir, "Charlie Sheen")
    assert len(output['films'].split('@')) == 68


def test_count_actor_9():
    output = index.search_actor(index_dir, "Chuck Norris")
    assert len(output['films'].split('@')) == 40


def test_count_actor_10():
    output = index.search_actor(index_dir, "Sarah Jessica Parker")
    assert len(output['films'].split('@')) == 42


def test_count_actor_11():
    output = index.search_actor(index_dir, "Zac Efron")
    assert len(output['films'].split('@')) == 26


def test_count_actor_12():
    output = index.search_actor(index_dir, "Cameron Diaz")
    assert len(output['films'].split('@')) == 51


def test_count_actor_13():
    output = index.search_actor(index_dir, "Demi Moore")
    assert len(output['films'].split('@')) == 44


def test_count_actor_14():
    output = index.search_actor(index_dir, "Eddie Murphy")
    assert len(output['films'].split('@')) == 50


def test_count_actor_15():
    output = index.search_actor(index_dir, "Uma Thurman")
    assert len(output['films'].split('@')) == 54


def test_count_actor_16():
    output = index.search_actor(index_dir, "Jackie Chan")
    assert len(output['films'].split('@')) == 131


def test_count_actor_17():
    output = index.search_actor(index_dir, "Bradley Cooper")
    assert len(output['films'].split('@')) == 37


def test_count_actor_18():
    output = index.search_actor(index_dir, "Katie Holmes")
    assert len(output['films'].split('@')) == 27


def test_count_actor_19():
    output = index.search_actor(index_dir, "Megan Fox")
    assert len(output['films'].split('@')) == 18


def test_count_actor_20():
    output = index.search_actor(index_dir, "Scarlett Johansson")
    assert len(output['films'].split('@')) == 43


"""
test movies with count from https://freebase-easy.cs.uni-freiburg.de/browse/#

example:
    https://freebase-easy.cs.uni-freiburg.de/browse/#triples=$1%20equals%20:e:New_York_Stories
"""


def test_count_movie_1():
    assert len(index.search_film(index_dir, "New York Stories")) == 87


def test_count_movie_2():
    assert len(index.search_film(index_dir, "The Dark Knight Rises")) == 284


def test_count_movie_3():
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "1"
    assert len(index.search_film(index_dir, "Lawless")) == 46
    mock.builtins.input = original_input


def test_count_movie_4():
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "2"
    assert len(index.search_film(index_dir, "Lawless")) == 9
    mock.builtins.input = original_input


def test_count_movie_5():
    assert len(index.search_film(index_dir, "The Dark Knight")) == 197


def test_count_movie_6():
    assert len(index.search_film(index_dir, "Step Up Revolution")) == 160


def test_count_movie_7():
    assert len(index.search_film(index_dir, "Eagle Eye")) == 202


def test_count_movie_8():
    assert len(index.search_film(index_dir, "Pearl Harbor")) == 167


def test_count_movie_9():
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "2"
    assert len(index.search_film(index_dir, "Road Trip")) == 15
    mock.builtins.input = original_input


def test_count_movie_10():
    assert len(index.search_film(index_dir, "Pirates of the Caribbean: at World's End")) == 130


def test_count_movie_11():
    assert len(index.search_film(index_dir, "Pirates of the Caribbean: Dead Man's Chest")) == 119


def test_count_movie_12():
    assert len(index.search_film(index_dir, "Pirates of the Caribbean: The Curse of the Black Pearl")) == 76


def test_count_movie_13():
    assert len(index.search_film(index_dir, "Pirates of the Caribbean: On Stranger Tides")) == 73


def test_count_movie_14():
    assert len(index.search_film(index_dir, "Pirates of the Caribbean: Dead Men Tell No Tales")) == 6


def test_count_movie_15():
    assert len(index.search_film(index_dir, "Zoolander")) == 137


def test_count_movie_16():
    assert len(index.search_film(index_dir, "Into the Wild")) == 55


def test_count_movie_17():
    assert len(index.search_film(index_dir, "Abraham Lincoln, Vampire Hunter")) == 114


def test_count_movie_18():
    assert len(index.search_film(index_dir, "Harry Potter and the Prisoner of Azkaban")) == 60


def test_count_movie_19():
    assert len(index.search_film(index_dir, "Bojová loď")) == 186


def test_count_movie_20():
    assert len(index.search_film(index_dir, "Vykoupení z věznice Shawshank")) == 62
