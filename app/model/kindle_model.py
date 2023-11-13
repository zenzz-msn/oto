import uuid
from datetime import datetime

class Book:
    '''Model class for Book'''

    def __init__(self, id: uuid, lastAccess:datetime, currentPage:int, author: str, country: str, imageLink: str, language: str, link: str, pages: int, title: str, year: int):
        '''Model Constructor'''
        self.id = id
        self.lastAccess = lastAccess if lastAccess else "2000-11-12 12:59:59.489792"
        self.currentPage = currentPage if currentPage else 0
        self.author = author
        self.country = country
        self.imageLink = imageLink
        self.language = language
        self.link = link
        self.pages = pages
        self.title = title
        self.year = year

    def to_dict(self):
        return {
            'id': self.id,
            'lastAccess': self.lastAccess,
            'currentPage': self.currentPage,
            'author': self.author,
            'country': self.country,
            'imageLink': self.imageLink,
            'language': self.language,
            'link': self.link,
            'pages': self.pages,
            'title': self.title,
            'year': self.year
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['id'],
            data.get('lastAccess'),
            data.get('currentPage'),
            data['author'],
            data['country'],
            data['imageLink'],
            data['language'],
            data['link'],
            data['pages'],
            data['title'],
            data['year']
        )
