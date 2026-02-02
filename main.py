from news import get_tamil_news
from ai_writer import generate_tamil_article
from blogger import post_to_blogger
import random

articles = get_tamil_news()
article = random.choice(articles)

content = generate_tamil_article(article)

post_to_blogger(
    article["title"],
    content,
    article["urlToImage"]
)
