import requests

def get_intelligence_hero(list_name):

    iq_list = []

    for name in list_name:
        url = "https://superheroapi.com/api/2619421814940190/search/" + f'{name}'
        resp = requests.get(url)

        for value in resp.json()['results']:
            if value['name'] == name:
                IQ_hero = int(value['powerstats']['intelligence'])
                iq_list.append(IQ_hero)

    res_tuple = list(zip(list_name, iq_list))
    sort_res = sorted(res_tuple)
    print(f'Самый умный супергерой - {sort_res[-1][0]}, его IQ равен {sort_res[-1][1]}')