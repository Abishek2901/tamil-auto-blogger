import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_tamil_article(article):
    prompt = f"""
    நீ ஒரு தமிழ் செய்தி எழுத்தாளர்.
    கீழ்கண்ட செய்தியை 250-300 வார்த்தைகளில்
    முழுக்க தமிழ் மொழியில்
    SEO-friendly ஆக எழுதவும்.

    தலைப்பு: {article['title']}
    செய்தி: {article['description']}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
