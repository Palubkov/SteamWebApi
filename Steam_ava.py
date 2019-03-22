import requests
import json
import webbrowser
import os


key = '12DFAEB25ABD07C6DC8BA4E82CCF8204'
steamid = '76561197998462172'


def req_fr_list(s_id):
    data = requests.get(
        'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/'
        '?key=%s&steamid=%s&relationship=friend&format=json' % (key, s_id))
    return data.json()


def req_ava(s_id):
    data = requests.get(
        'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/'
        'v0002/?key=%s&steamids=%s' % (key, s_id))
    return data.json()


def dump_split(to_dump):
    data = json.dumps(to_dump)
    d = data.split(',')
    return d


def id_parser(v):
    res = []
    for i in v:
        if 'steamid' in i:
            res.append(i[-18:-1])
    return res


def ava_parser(v):
    avatars = []
    for i in v:
        for j in dump_split(req_ava(i)):
            if '"avatar"' in j:
                avatars.append(j[12:-1])
    return avatars


def make_html(avas):
    if os.path.isfile('imgtable.html'):
        os.remove("imgtable.html")
    avatab = "<html><table>"
    for i in avas:
        avatab = avatab+'<tr><td><img src="'+i+'"></td></tr>'

    avatab = avatab + "</table></html>"
    hs = open("imgtable.html", 'w')
    hs.write(avatab)
    hs.close()
    return hs.name


#webbrowser.open(make_html(ava_parser(id_parser(dump_split(req_fr_list(steamid))))))