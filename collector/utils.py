
import re
import httpx as http
from langchain.text_splitter import RecursiveCharacterTextSplitter
from .concurrent_fetch import batch_fetch
from bs4 import BeautifulSoup
import html2text
import markdown

import asyncio


class GithubUser:
    def __init__(self, user: str):
        self.user = user
        self.repos = self._get_repos_url()
        self.repos_readme_url_map = {
            repo: f'https://raw.githubusercontent.com/{self.user}/{repo}/main/README.md' for repo in self.repos}

        self.url_readme_texts_pair = self._get_readme_texts()

    def _get_repos_url(self) -> list[str]:
        url = f'https://api.github.com/users/{self.user}/repos'
        result = http.get(url).json()
        return [repo['name'] for repo in result]

    def _get_readme_texts(self) -> list[str]:
        urls = self.repos_readme_url_map.values()
        return [(url, self._text_spliter(text)) for url, text in asyncio.run(batch_fetch(urls))]

    def _text_spliter(self, text: str) -> list[str]:
        self.extract_text_from_markdown(text)
        return RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=0).split_text(text)

    @staticmethod
    def extract_text_from_markdown(md_content):
        # Convert the Markdown content to HTML
        html_content = markdown.markdown(md_content)

        # Use html2text to convert the HTML content to plain text
        h = html2text.HTML2Text()
        h.ignore_links = True
        h.ignore_images = True
        text = h.handle(html_content)

        # Remove HTML tags and URLs from the extracted text
        html_tag_pattern = re.compile('<.*?>')
        return html_tag_pattern.sub('', text)
