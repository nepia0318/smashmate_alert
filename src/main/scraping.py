import requests
from bs4 import BeautifulSoup

def getCurrentRateByUserId(userId):
    baseUrl = "https://smashmate.net/user/"

    # ウェブページの内容を取得
    response = requests.get(baseUrl + str(userId))
    response.raise_for_status()  # エラーがあれば例外を発生させる

    # BeautifulSoupでHTMLを解析
    soup = BeautifulSoup(response.text, 'html.parser')

    # 'current-rate'クラスを持つ要素を探す
    elements = soup.select('div.side > div.row.row-center.va-middle > div.col-xs-6')

    results = {}
    if elements:
        results = {
            'current_rate': elements[1].text.strip(),
            'maximum_rate': elements[3].text.strip(),
            'match_result': elements[5].text.strip()
        }
        print(results)
    else:
        print("合致する情報が取得できませんでした")
        raise Exception

    return results
