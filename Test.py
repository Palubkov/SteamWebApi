import pytest
import Steam_ava
import os

def test_check_type_fr(friends):
    return type(friends[0]) == str


def test_check_count_fr(friends):
    return len(friends) > 0


def test_check_type_ava(avatars):
    return type(avatars[0]) == str


def test_check_count_ava(avatars):
    return len(avatars) > 0


def test_file_creation():
    Steam_ava.make_html(['1', '2', '3'])
    assert os.path.isfile('imgtable.html')


