from pprint import pprint

from datetime import date, timedelta

import requests


def get_questions():

    today = date.today()
    day_before_yesterday = today - timedelta(days=2)

    url = f'https://api.stackexchange.com/2.3/questions?fromdate={day_before_yesterday}' \
          f'&todate={today}&order=desc&sort=activity&tagged=Python&site=stackoverflow'
    response = requests.get(url)

    pprint(response.json())