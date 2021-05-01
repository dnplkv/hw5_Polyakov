from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from main.models import Post
import requests


class Command(BaseCommand):
    page_url = 'https://doroshenkoaa.ru/med/'

    def handle(self, *args, **options):
        response = requests.get(self.page_url)
        soup_page = BeautifulSoup(response.content, 'html.parser')
        article_links = []
        h2s = soup_page.find_all("h2")
        for h2 in h2s:
            article_links.append(h2.a['href'])
        for link in article_links:
            r = requests.get(link)
            soup = BeautifulSoup(r.content, "html.parser")
            for soup_title in soup.findAll("h1", {"itemprop": "headline"}):
                article_title = soup_title.text.strip()
            for soup_content in soup.findAll("div", {"itemprop": "articleBody"}):
                article_content = soup_content.text
            Post.objects.create(title=article_title, content=article_content)
