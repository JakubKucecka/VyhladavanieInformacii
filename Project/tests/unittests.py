import sys
sys.path.insert(1, '../')
from lib import dump
from lib import pars
from lib import pair
from lib import sort
from lib import index
from unittest import mock
import gzip

input_file = 'data/tmp_film.gz'
actors_file = "data/actors.gz"
performances_file = "data/performances.gz"
other_file = "data/other.gz"
final_file = "data/final.gz"
index_dir = "data/index"

"""
zcat returns one line less in the terminal
"""


def test_dump():
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: input_file
    dump.dump(actors_file, performances_file, other_file, 1)
    mock.builtins.input = original_input

    with gzip.open(actors_file, 'rb') as f:
        for i, l in enumerate(f):
            pass
    assert i + 1 == 84

    with gzip.open(performances_file, 'rb') as f:
        for i, l in enumerate(f):
            pass
    assert i + 1 == 89

    with gzip.open(other_file, 'rb') as f:
        for i, l in enumerate(f):
            pass
    assert i + 1 == 120


def test_pars():
    a = {'m.0c1lfgs': {'name': ['Bill Moor'], 'alias': ['William H Moor III'], 'b_date': '1931-07-13',
                       'd_date': '2007-11-27',
                       'films': {'m.0v1h48r': 'NONE', 'm.0w1zn1m': 'NONE', 'm.0yqny5k': 'NONE', 'm.0c1lfgg': 'NONE',
                                 'm.0v4kwzc': 'NONE'}},
         'm.049wzr': {'name': ['Carole Bouquet', 'Карол Буке', 'Кароль Буке'], 'alias': ['Carole Bouquetová'],
                      'b_date': '1957-08-18', 'd_date': '',
                      'films': {'m.0j8w0d1': 'NONE', 'm.04dj223': 'NONE', 'm.0hzvrvq': 'NONE', 'm.0ncf20s': 'NONE',
                                'm.0kbqn77': 'NONE', 'm.04dfbch': 'NONE', 'm.0gvn89_': 'NONE', 'm.0k46s8': 'NONE',
                                'm.0131h9d8': 'NONE', 'm.05v60ym': 'NONE', 'm.04dfbb2': 'NONE', 'm.0csb3yq': 'NONE',
                                'm.0dkfzhk': 'NONE', 'm.04j14g8': 'NONE', 'm.04dfb5w': 'NONE', 'm.0gvz14t': 'NONE',
                                'm.0bgbt7y': 'NONE', 'm.0wc5nh2': 'NONE', 'm.0c1lj1y': 'NONE', 'm.0cg6stf': 'NONE',
                                'm.02vbdb7': 'NONE', 'm.02vc7nk': 'NONE', 'm.0n27_lw': 'NONE', 'm.0wc68wl': 'NONE',
                                'm.03jp9sv': 'NONE', 'm.0k7wpv': 'NONE', 'm.02vc8t9': 'NONE', 'g.11b6_k4cv8': 'NONE',
                                'm.0crsbyq': 'NONE', 'm.04stmnb': 'NONE'}},
         'm.03lv3s': {'name': ['Victor Argo'], 'alias': ['Victor Jimenez', 'Vic Argo', 'Víctor Jiménez'],
                      'b_date': '1934-11-05', 'd_date': '2004-04-07',
                      'films': {'m.0jx7cdv': 'NONE', 'm.0k7__9x': 'NONE', 'm.0bntmn9': 'NONE', 'm.0glhqk2': 'NONE',
                                'm.0vxmlz8': 'NONE', 'm.0vxn7b_': 'NONE', 'm.0cgbx3r': 'NONE', 'm.02vcnyz': 'NONE',
                                'm.0csd099': 'NONE', 'm.0jtz2f': 'NONE', 'm.075q0qf': 'NONE', 'm.0cg6zjh': 'NONE',
                                'm.04j0tzx': 'NONE', 'm.0vsk19x': 'NONE', 'm.09tdyn7': 'NONE', 'm.0gz5hgh': 'NONE',
                                'm.0w24hbm': 'NONE', 'm.04j0_0n': 'NONE', 'm.040g20j': 'NONE', 'm.0cg54p1': 'NONE',
                                'm.07wkxq7': 'NONE', 'm.0cg1j97': 'NONE', 'm.0bvy7y4': 'NONE', 'm.08cqvhf': 'NONE',
                                'm.0vb36x6': 'NONE', 'm.0dgktpj': 'NONE', 'm.0cw0qp0': 'NONE', 'm.09j2x4p': 'NONE',
                                'm.0vnzbq3': 'NONE', 'm.011k09th': 'NONE', 'm.0q_4yzm': 'NONE', 'm.0gkk8q7': 'NONE',
                                'm.0cg0jqc': 'NONE', 'm.0tkct71': 'NONE', 'm.0csm6rl': 'NONE', 'm.04j0hpm': 'NONE',
                                'm.0gz6df2': 'NONE', 'm.0y6r_c9': 'NONE', 'm.0cfzm0h': 'NONE', 'm.011lm293': 'NONE',
                                'm.0cg8fgt': 'NONE', 'm.0c6g_65': 'NONE', 'm.02vddcl': 'NONE', 'm.07lm452': 'NONE',
                                'm.0bzbclb': 'NONE', 'm.0jxgx6': 'NONE', 'm.0cg3m_3': 'NONE'}},
         'm.01vzbw6': {'name': ["Joe 'Tricky Sam' Nanton", 'Tricky Sam Nanton'],
                       'alias': ['Nanton, Joe', 'Joe Nanton', 'Nanton, Tricky Sam', 'Joe Tricky Sam Nanton ',
                                 'J. Nanton', 'Joseph Nanton', 'Josef Nanton'], 'b_date': '1904-02-01',
                       'd_date': '1946-07-20', 'films': {'m.0zkb02w': 'NONE'}},
         'm.0h5v7n1': {'name': ['Utz Krause'], 'alias': [], 'b_date': '1955-04-16', 'd_date': '1998-01-07',
                       'films': {'m.0h5v7mz': 'NONE'}}}
    p = {'m.0h5v7mz': 'm.02chjf', 'm.0gyhxsk': 'm.03wy8t', 'm.0k16w0': 'm.03wy8t', 'm.0yqp0gw': 'm.03wy8t',
         'm.0k16vk': 'm.03wy8t', 'm.0yqnzc3': 'm.03wy8t', 'm.0yqnyjm': 'm.03wy8t', 'm.0cg60gj': 'm.03wy8t',
         'm.0yqnr5x': 'm.03wy8t', 'm.0yqp0s5': 'm.03wy8t', 'm.0zgpfq1': 'm.03wy8t', 'm.0cf_7br': 'm.03wy8t',
         'm.0cg3m_3': 'm.03wy8t', 'm.0yqnyyk': 'm.03wy8t', 'm.0yqnz5w': 'm.03wy8t', 'm.0yqp0wl': 'm.03wy8t',
         'm.0k16vq': 'm.03wy8t', 'm.0yqnw32': 'm.03wy8t', 'm.0yqnwg7': 'm.03wy8t', 'm.0cgn0nn': 'm.03wy8t',
         'm.0yqnxlc': 'm.03wy8t', 'm.0cv_q35': 'm.03wy8t', 'm.0yqp11l': 'm.03wy8t', 'm.0yqp1dj': 'm.03wy8t',
         'm.0k16v2': 'm.03wy8t', 'm.0k16v7': 'm.03wy8t', 'm.0k16vw': 'm.03wy8t', 'm.0yqp12j': 'm.03wy8t',
         'm.0yqnwys': 'm.03wy8t', 'm.0yqp141': 'm.03wy8t', 'm.0yqp08p': 'm.03wy8t', 'm.0yqns9w': 'm.03wy8t',
         'm.0yqnrd3': 'm.03wy8t', 'm.0yqnxr5': 'm.03wy8t', 'm.0yqnrq7': 'm.03wy8t', 'm.0yqnw62': 'm.03wy8t',
         'm.0yqnw5b': 'm.03wy8t', 'm.0yqnxw_': 'm.03wy8t', 'm.0gkcm82': 'm.03wy8t', 'm.0yqnxgf': 'm.03wy8t',
         'm.0crrf8f': 'm.03wy8t', 'm.0cs9q_z': 'm.03wy8t', 'm.0yqnxf0': 'm.03wy8t', 'm.0yqnz6t': 'm.03wy8t',
         'm.0yqnzj2': 'm.03wy8t', 'm.0yqny4g': 'm.03wy8t', 'm.0yqnz59': 'm.03wy8t', 'm.0yqnrtc': 'm.03wy8t',
         'm.0yqnrs4': 'm.03wy8t', 'm.0gdmh4v': 'm.03wy8t', 'm.0yqp1cy': 'm.03wy8t', 'm.0yqn_1r': 'm.03wy8t',
         'm.0k16ty': 'm.03wy8t', 'm.0bhfb87': 'm.03wy8t', 'm.0yqns5s': 'm.03wy8t', 'm.0yqn_dx': 'm.03wy8t',
         'm.0yqp0bl': 'm.03wy8t', 'm.0yqp05g': 'm.03wy8t', 'm.0yqp16m': 'm.03wy8t', 'm.0gbylp_': 'm.03wy8t',
         'm.0yqnwkp': 'm.03wy8t', 'm.0yqnrv6': 'm.03wy8t', 'm.0yqnxvr': 'm.03wy8t', 'm.0yqn_gh': 'm.03wy8t',
         'm.0yqnydr': 'm.03wy8t', 'm.0k16ts': 'm.03wy8t', 'm.0yqnxts': 'm.03wy8t', 'm.0yqnzcv': 'm.03wy8t',
         'm.0yqnzfd': 'm.03wy8t', 'm.0crsbyq': 'm.03wy8t', 'm.0yqny7q': 'm.03wy8t', 'm.0yqnyp2': 'm.03wy8t',
         'm.0k16vd': 'm.03wy8t', 'm.040_z81': 'm.03wy8t', 'm.0k16w5': 'm.03wy8t', 'm.0cg4khy': 'm.03wy8t',
         'm.0yqp0dg': 'm.03wy8t', 'm.0yqnz35': 'm.03wy8t', 'm.0yqnrf5': 'm.03wy8t', 'm.0yqn_p5': 'm.03wy8t',
         'm.0yqny3l': 'm.03wy8t', 'm.0gclj63': 'm.03wy8t', 'm.0yqny65': 'm.03wy8t', 'm.0yqp15t': 'm.03wy8t',
         'm.0k16tm': 'm.03wy8t', 'm.0bhf6ql': 'm.03wy8t', 'm.0yqnxs_': 'm.03wy8t', 'm.0cw06q_': 'm.03wy8t',
         'm.0yqny5k': 'm.03wy8t'}
    f = {'m.03wy8t': ['New York Stories', 'Nowojorskie opowieści', 'Historias de Nueva York', 'New York Üçlemesi',
                      'Нью-йоркские истории', 'Нюйоркски истории', 'Histórias de Nova Iorque', 'Contos de Nova York',
                      'Històries de Nova York', 'New Yorker Geschichten'],
         'm.02chjf': ['Lola rennt', 'Aleargă, Lola, aleargă', 'Lola corre', 'Lola běží o život', 'Run, Lola, Run',
                      'Run, Lola, run', 'Corra Lola, Corra', 'Run Lola Run', 'Biegnij Lola, biegnij', 'A lé meg a Lola',
                      'Bėk, Lola, bėk', 'Беги, Лола, беги', 'Cours, Lola, cours', 'Corre, Lola, corre',
                      'Trči Lola, trči', 'Lola trči', 'Lola', 'Corre, Lola, Corre', 'Spring Lola', 'Corre Lola Corre',
                      'Trči Lola trči', 'Бягай, Лола', 'Koş Lola Koş']}

    [ACTOR, PERF_FILM, FILM_ID_NAME] = pars.pars(actors_file, performances_file, other_file, {}, {}, {})

    assert a == ACTOR
    assert p == PERF_FILM
    assert f == FILM_ID_NAME


def test_pair():
    a = {'m.0c1lfgs': {'name': ['Bill Moor'], 'alias': ['William H Moor III'], 'b_date': '1931-07-13',
                       'd_date': '2007-11-27',
                       'films': {'m.0yqny5k': 'NONE'}},
         'm.03lv3s': {'name': ['Victor Argo'], 'alias': ['Victor Jimenez', 'Vic Argo', 'Víctor Jiménez'],
                      'b_date': '1934-11-05', 'd_date': '2004-04-07',
                      'films': {'m.0cg3m_3': 'NONE'}}}
    p = {'m.0cg3m_3': 'm.03wy8t', 'm.0yqny5k': 'm.03wy8t'}
    f = {'m.03wy8t': ['New York Stories', 'Nowojorskie opowieści', 'Historias de Nueva York', 'New York Üçlemesi',
                      'Нью-йоркские истории', 'Нюйоркски истории', 'Histórias de Nova Iorque', 'Contos de Nova York',
                      'Històries de Nova York', 'New Yorker Geschichten']}

    output = {'m.0c1lfgs': {'name': ['Bill Moor'], 'alias': ['William H Moor III'], 'b_date': '1931-07-13',
                            'd_date': '2007-11-27', 'films': {
            'm.0yqny5k': ['m.03wy8t', 'New York Stories', 'Nowojorskie opowieści', 'Historias de Nueva York',
                          'New York Üçlemesi', 'Нью-йоркские истории', 'Нюйоркски истории', 'Histórias de Nova Iorque',
                          'Contos de Nova York', 'Històries de Nova York', 'New Yorker Geschichten']}},
              'm.03lv3s': {'name': ['Victor Argo'], 'alias': ['Victor Jimenez', 'Vic Argo', 'Víctor Jiménez'],
                           'b_date': '1934-11-05', 'd_date': '2004-04-07', 'films': {
                      'm.0cg3m_3': ['m.03wy8t', 'New York Stories', 'Nowojorskie opowieści', 'Historias de Nueva York',
                                    'New York Üçlemesi', 'Нью-йоркские истории', 'Нюйоркски истории',
                                    'Histórias de Nova Iorque', 'Contos de Nova York', 'Històries de Nova York',
                                    'New Yorker Geschichten']}}}

    a = pair.pair(a, p, f)
    assert a == output


def test_sort_and_index():
    actors = {'m.0c1lfgs': {'name': ['Bill Moor'], 'alias': ['William H Moor III'], 'b_date': '1931-07-13',
                            'd_date': '2007-11-27', 'films': {'m.0v1h48r': 'NONE', 'm.0w1zn1m': 'NONE',
                                                              'm.0yqny5k': ['m.03wy8t', 'New York Stories',
                                                                            'Nowojorskie opowieści',
                                                                            'Historias de Nueva York',
                                                                            'New York Üçlemesi', 'Нью-йоркские истории',
                                                                            'Нюйоркски истории',
                                                                            'Histórias de Nova Iorque',
                                                                            'Contos de Nova York',
                                                                            'Històries de Nova York',
                                                                            'New Yorker Geschichten'],
                                                              'm.0c1lfgg': 'NONE', 'm.0v4kwzc': 'NONE'}},
              'm.049wzr': {'name': ['Carole Bouquet', 'Карол Буке', 'Кароль Буке'], 'alias': ['Carole Bouquetová'],
                           'b_date': '1957-08-18', 'd_date': '',
                           'films': {'m.0j8w0d1': 'NONE', 'm.04dj223': 'NONE', 'm.0hzvrvq': 'NONE', 'm.0ncf20s': 'NONE',
                                     'm.0kbqn77': 'NONE', 'm.04dfbch': 'NONE', 'm.0gvn89_': 'NONE', 'm.0k46s8': 'NONE',
                                     'm.0131h9d8': 'NONE', 'm.05v60ym': 'NONE', 'm.04dfbb2': 'NONE',
                                     'm.0csb3yq': 'NONE', 'm.0dkfzhk': 'NONE', 'm.04j14g8': 'NONE', 'm.04dfb5w': 'NONE',
                                     'm.0gvz14t': 'NONE', 'm.0bgbt7y': 'NONE', 'm.0wc5nh2': 'NONE', 'm.0c1lj1y': 'NONE',
                                     'm.0cg6stf': 'NONE', 'm.02vbdb7': 'NONE', 'm.02vc7nk': 'NONE', 'm.0n27_lw': 'NONE',
                                     'm.0wc68wl': 'NONE', 'm.03jp9sv': 'NONE', 'm.0k7wpv': 'NONE', 'm.02vc8t9': 'NONE',
                                     'g.11b6_k4cv8': 'NONE',
                                     'm.0crsbyq': ['m.03wy8t', 'New York Stories', 'Nowojorskie opowieści',
                                                   'Historias de Nueva York', 'New York Üçlemesi',
                                                   'Нью-йоркские истории', 'Нюйоркски истории',
                                                   'Histórias de Nova Iorque', 'Contos de Nova York',
                                                   'Històries de Nova York', 'New Yorker Geschichten'],
                                     'm.04stmnb': 'NONE'}},
              'm.03lv3s': {'name': ['Victor Argo'], 'alias': ['Victor Jimenez', 'Vic Argo', 'Víctor Jiménez'],
                           'b_date': '1934-11-05', 'd_date': '2004-04-07',
                           'films': {'m.0jx7cdv': 'NONE', 'm.0k7__9x': 'NONE', 'm.0bntmn9': 'NONE', 'm.0glhqk2': 'NONE',
                                     'm.0vxmlz8': 'NONE', 'm.0vxn7b_': 'NONE', 'm.0cgbx3r': 'NONE', 'm.02vcnyz': 'NONE',
                                     'm.0csd099': 'NONE', 'm.0jtz2f': 'NONE', 'm.075q0qf': 'NONE', 'm.0cg6zjh': 'NONE',
                                     'm.04j0tzx': 'NONE', 'm.0vsk19x': 'NONE', 'm.09tdyn7': 'NONE', 'm.0gz5hgh': 'NONE',
                                     'm.0w24hbm': 'NONE', 'm.04j0_0n': 'NONE', 'm.040g20j': 'NONE', 'm.0cg54p1': 'NONE',
                                     'm.07wkxq7': 'NONE', 'm.0cg1j97': 'NONE', 'm.0bvy7y4': 'NONE', 'm.08cqvhf': 'NONE',
                                     'm.0vb36x6': 'NONE', 'm.0dgktpj': 'NONE', 'm.0cw0qp0': 'NONE', 'm.09j2x4p': 'NONE',
                                     'm.0vnzbq3': 'NONE', 'm.011k09th': 'NONE', 'm.0q_4yzm': 'NONE',
                                     'm.0gkk8q7': 'NONE', 'm.0cg0jqc': 'NONE', 'm.0tkct71': 'NONE', 'm.0csm6rl': 'NONE',
                                     'm.04j0hpm': 'NONE', 'm.0gz6df2': 'NONE', 'm.0y6r_c9': 'NONE', 'm.0cfzm0h': 'NONE',
                                     'm.011lm293': 'NONE', 'm.0cg8fgt': 'NONE', 'm.0c6g_65': 'NONE',
                                     'm.02vddcl': 'NONE', 'm.07lm452': 'NONE', 'm.0bzbclb': 'NONE', 'm.0jxgx6': 'NONE',
                                     'm.0cg3m_3': ['m.03wy8t', 'New York Stories', 'Nowojorskie opowieści',
                                                   'Historias de Nueva York', 'New York Üçlemesi',
                                                   'Нью-йоркские истории', 'Нюйоркски истории',
                                                   'Histórias de Nova Iorque', 'Contos de Nova York',
                                                   'Històries de Nova York', 'New Yorker Geschichten']}},
              'm.01vzbw6': {'name': ["Joe 'Tricky Sam' Nanton", 'Tricky Sam Nanton'],
                            'alias': ['Nanton, Joe', 'Joe Nanton', 'Nanton, Tricky Sam', 'Joe Tricky Sam Nanton ',
                                      'J. Nanton', 'Joseph Nanton', 'Josef Nanton'], 'b_date': '1904-02-01',
                            'd_date': '1946-07-20', 'films': {'m.0zkb02w': 'NONE'}},
              'm.0h5v7n1': {'name': ['Utz Krause'], 'alias': [], 'b_date': '1955-04-16', 'd_date': '1998-01-07',
                            'films': {'m.0h5v7mz': ['m.02chjf', 'Lola rennt', 'Aleargă, Lola, aleargă', 'Lola corre',
                                                    'Lola běží o život', 'Run, Lola, Run', 'Run, Lola, run',
                                                    'Corra Lola, Corra', 'Run Lola Run', 'Biegnij Lola, biegnij',
                                                    'A lé meg a Lola', 'Bėk, Lola, bėk', 'Беги, Лола, беги',
                                                    'Cours, Lola, cours', 'Corre, Lola, corre', 'Trči Lola, trči',
                                                    'Lola trči', 'Lola', 'Corre, Lola, Corre', 'Spring Lola',
                                                    'Corre Lola Corre', 'Trči Lola trči', 'Бягай, Лола',
                                                    'Koş Lola Koş']}}}

    sort.sort(actors, final_file)

    with gzip.open(final_file, 'rb') as f:
        for i, l in enumerate(f):
            pass
    assert len(actors) == i + 1

    index.index(index_dir, final_file)

    with gzip.open(final_file, 'rb') as f:
        for i, l in enumerate(f):
            pass
    assert len(actors) == i + 1


def test_new_york_stories():
    test = sorted(
        ['Bill Moor', 'Carole Bouquet', 'Victor Argo'])
    assert sorted(index.search_film(index_dir, "New York Stories")) == test


def test_film_correction_and_exit():
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "e"
    output = index.search_film(index_dir, "new york storieZ")
    assert output == -2
    mock.builtins.input = original_input


def test_input_not_find():
    output = index.search_film(index_dir, "Name not found, I think, This is bad name of film")
    assert output == -1


def test_not_case_sensitive_1():
    output1 = index.search_actor(index_dir, "Victor Argo")
    output2 = index.search_actor(index_dir, "victor argo")
    assert output1 == output2


def test_not_case_sensitive_2():
    output1 = index.search_actor(index_dir, "Victor Argo")
    output2 = index.search_actor(index_dir, "ViCtOr aRgO")
    assert output1 == output2


def test_correction():
    output1 = index.search_actor(index_dir, "Victor Argo")
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "1"
    output2 = index.search_actor(index_dir, "viKtor arKo")
    assert output1['films'] == output2['films']
    mock.builtins.input = original_input


def test_actor_exit():
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "e"
    output = index.search_actor(index_dir, "viKtor arKo")
    assert output == -2
    mock.builtins.input = original_input
