import requests
import re
from bs4 import BeautifulSoup

def getCurrentRateByUserId(userId):
    base_url = "https://smashmate.net/user/"
    print(f'url: {base_url + str(userId)}')

    # Get Webpage content
    response = requests.get(base_url + str(userId))
    response.raise_for_status()  # Throw exception if request failed

    # Parse HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find current-rate class
    elements = soup.select('div.side > div.row.row-center.va-middle > div.col-xs-6')

    results = {}
    if elements:
        current_rate    = re.search(r'\d+', elements[1].text.strip())
        difference_rate = re.search(r'(?<=前日比：)-*\d+', elements[1].text.strip())

        results = {
            'current_rate'   : current_rate.group() if current_rate is not None else 'None' ,
            'difference_rate': difference_rate.group() if difference_rate is not None else 'None',
            'maximum_rate'   : elements[3].text.strip(),
            'match_result'   : elements[5].text.strip()
        }
        print(results)
    else:
        raise Exception("Data not found.")

    return results
