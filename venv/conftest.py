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