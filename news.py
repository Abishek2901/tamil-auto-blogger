import requests
import os

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def get_tamil_news():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "in",
        "language": "ta",
        "pageSize": 5,
        "apiKey": NEWS_API_KEY
    }

    r = requests.get(url, params=params)
    return r.json()["articles"]
