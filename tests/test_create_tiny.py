import requests

def test_create_short_url():
    url = 'https://sberdevices.ru/shop/category/tv/filter/'


    response = requests.post(
        'https://gotiny.cc/api',
        headers={"Content-Type": "application/json"},
        json={"input" : url})
    assert response.status_code == 200