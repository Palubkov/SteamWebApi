import pytest
import Steam_ava
import os

steamid = '76561197998462172'
key = '12DFAEB25ABD07C6DC8BA4E82CCF8204'


@pytest.fixture
def friends():
    data = Steam_ava.id_parser(
        Steam_ava.dump_split(Steam_ava.req_fr_list(steamid)))
    return data


@pytest.fixture
def avatars():
    data = Steam_ava.ava_parser(
        Steam_ava.dump_split(Steam_ava.req_ava(steamid)))
    return data


def test_check_type_fr(friends):
    return type(friends[1]) == str


def test_check_count_fr(friends):
    return len(friends) > 0


def test_check_type_ava(avatars):
    return type(avatars[1]) == str


def test_check_count_ava(avatars):
    return len(avatars) > 0


def test_file_creation():
    Steam_ava.make_html(['1', '2', '3'])
    assert os.path.isfile('imgtable.html')


