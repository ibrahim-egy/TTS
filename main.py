import webbrowser
import requests
import fitz
import os

with fitz.open("Hello.pdf") as doc:
    text = ""
    for page in doc:
        text += page.get_text()

API_KEY = os.environ["API_KEY"]

params = {
    "key": API_KEY,
    "src": text,
    "hl": "en-us",
}

response = requests.get("http://api.voicerss.org", params=params)
response.raise_for_status()

url = response.url
webbrowser.open(url)
