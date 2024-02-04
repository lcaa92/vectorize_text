import requests
import re

from bs4 import BeautifulSoup
import nltk
from gensim.models import Word2Vec


PAGES = [
    "https://en.wikipedia.org/wiki/UEFA_Champions_League",
    "https://en.wikipedia.org/wiki/Copa_Am%C3%A9rica",
    "https://en.wikipedia.org/wiki/UEFA_Nations_League",
    "https://en.wikipedia.org/wiki/UEFA_European_Championship",
    "https://en.wikipedia.org/wiki/FIFA_World_Cup"
]


class ProcessContent():
    page = ""
    page_content = []
    merge_text = ""
    sentences = []
    model = Word2Vec()

    def __init__(self, page="", page_content="") -> None:
        self.page = page
        self.page_content = page_content

    def get_text_data(self):
        """Merge page_content in one string"""

        for content in self.page_content:
            self.merge_text += content.text

        self.merge_text = re.sub(r'\[[0-9]*\]', ' ', self.merge_text)
        self.merge_text = re.sub(r'\s+', ' ', self.merge_text)
        self.merge_text = self.merge_text.lower()
        self.merge_text = re.sub(r'[@#\$%&\*\(\)\<\>\'\":;\]\[-]', ' ', self.merge_text)
        self.merge_text = re.sub(r'\d', ' ', self.merge_text)
        self.merge_text = re.sub(r'\s+', ' ', self.merge_text)

    def tokenize_text(self):
        """Tokenize text"""
        self.sentences = nltk.sent_tokenize(self.merge_text)

        self.sentences = [nltk.word_tokenize(sentence) for sentence in self.sentences]

    def run(self):
        print(f'Running process to page {self.page}')
        self.get_text_data()
        self.tokenize_text()
        self.model = Word2Vec(self.sentences, min_count=1)


if __name__ == '__main__':
    nltk.download('punkt')

    for page in PAGES:
        resp = requests.get(page)
        soup = BeautifulSoup(resp.text, 'html.parser')
        content = soup.find_all('p')

        process = ProcessContent(page=page, page_content=content)
        process.run()
