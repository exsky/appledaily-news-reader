from enum import Enum
from libs.news import NewsIngress, Article
from os import makedirs
from os.path import exists as pexists


class Mode(Enum):
    TITLE = 1
    LINK = 2
    QUICK = 3


class Creator:
    #Static variable
    ni = NewsIngress()

    def __init__(self, mode=None):
        if not pexists('news'):
            makedirs('news')
        if not mode:    # 沒值給預設
            self.mode = Mode.TITLE
        elif not isinstance(mode, Mode):  # 有值要檢查是不是合法
            raise TypeError('Mode must be an instance of Mode Enum')
        else:
            self.mode = mode

    @classmethod
    def gen_titles(cls):
        try:
            print('[Title Only]')
            with open('news/news_title.txt', 'w+') as f:
                f.write('\n'.join(cls.ni.get_titles_list()))
        except Exception as e:
            print(e)

    @classmethod
    def gen_title_link(cls):
        try:
            print('[Title and Link]')
            prefix = 'https://tw.appledaily.com'
            with open('news/news_title_link.txt', 'w+') as f:
                for k, v in cls.ni.gen_title_link_dict().items():
                    f.write(k+'\n')
                    f.write('{}{}\n\n'.format(prefix, v))
        except Exception as e:
            print(e)

    @classmethod
    def gen_quick(cls):
        try:
            print('[Quick]')
            prefix = 'https://tw.appledaily.com'
            with open('news/news_quick.txt', 'w+') as f:
                for k, v in cls.ni.gen_title_link_dict().items():
                    article = Article(v)
                    f.write(k+'\n')
                    f.write('{}{}\n'.format(prefix, v))
                    f.write(article.get_content())
                    f.write('\n\n')
        except Exception as e:
            print(e)

    def gen_file(self):
        if self.mode == Mode.TITLE:
            self.gen_titles()
        elif self.mode == Mode.LINK:
            self.gen_title_link()
        elif self.mode == Mode.QUICK:
            self.gen_quick()
