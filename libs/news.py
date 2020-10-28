import requests
from bs4 import BeautifulSoup


class NewsIngress:

    def __init__(self, url=None):
        if not url:
            url = 'https://tw.appledaily.com/realtime/recommend/'
        self.resp = requests.get(url)
        self.status = self.resp.status_code
        self.soup = BeautifulSoup(self.resp.text, 'html.parser')

    def get_titles_list(self):
        if self.status != 200:
            return

        titles = []
        for sp in self.soup.find_all('span'):
            news_title = sp.find('a')
            if news_title:
                # \u3000 是全形空白
                titles.append(news_title.string.replace(u'\u3000', u' '))
        return titles

    def gen_title_link_dict(self):
        if self.status != 200:
            return

        title_link = {}
        for a_tag in self.soup.find_all('a', class_='text_brownish-grey'):
            news_title = a_tag.string.replace(u'\u3000', u' ')
            title_link[news_title] = a_tag.get('href')
        return title_link


class Article:

    def __init__(self, uri=None):
        if not uri:
            uri = '/gadget/20201021/W66WFUGHSZF3JGQYHVX7MYSZCY/'
        url = 'https://tw.appledaily.com' + uri
        self.resp = requests.get(url)
        self.status = self.resp.status_code
        self.soup = BeautifulSoup(self.resp.text, 'html.parser')

    def get_title(self):    # TODO: turn to staticmethod
        title = self.soup.find(id='article-header').find_all('span')[0].string
        title = title.replace(u'\u3000', u' ')
        return title

    def get_content(self):  # TODO: turn to staticmethod
        if self.status != 200:
            return
        sections = self.soup.find_all('p', class_='text--desktop')
        content = ''
        for section in sections:
            if section.string:
                content += str(section.string)
        return content
