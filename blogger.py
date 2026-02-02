from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
import os

BLOG_ID = os.getenv("BLOG_ID")

def post_to_blogger(title, content, image):
    creds = Credentials.from_service_account_info(
        eval(os.getenv("GOOGLE_CREDS")),
        scopes=["https://www.googleapis.com/auth/blogger"]
    )

    service = build("blogger", "v3", credentials=creds)

    body = {
        "title": title,
        "content": f'<img src="{image}"/><p>{content}</p>'
    }

    service.posts().insert(blogId=BLOG_ID, body=body).execute()

