import requests
from bs4 import BeautifulSoup

def scraping(userId):
    baseUrl = "https://smashmate.net/user/" #kamlon: 54285

    try:
        # ウェブページの内容を取得
        response = requests.get(baseUrl + str(userId))
        response.raise_for_status()  # エラーがあれば例外を発生させる

        # BeautifulSoupでHTMLを解析
        soup = BeautifulSoup(response.text, 'html.parser')

        # 'current-rate'クラスを持つ要素を探す
        rate_element = soup.find(class_='rate_text')

        if rate_element:
            current_rate = rate_element.text.strip()
            print(f"現在レート: {current_rate}")
        else:
            print("現在レートの情報が見つかりませんでした。")

    # except requests.RequestException as e:
    #     print(f"リクエストエラー: {e}")
    except Exception as e:
        # print(f"エラーが発生しました: {e}")
        raise

    return current_rate
