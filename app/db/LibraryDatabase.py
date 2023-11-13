import json
from datetime import datetime
from ..model.kindle_model import Book

class LibraryDatabase:
    _instance = None

    def __new__(cls, file_path):
        if not cls._instance:
            cls._instance = super(LibraryDatabase, cls).__new__(cls)
            cls._instance.file_path = file_path
            cls._instance.data = cls._instance.load_data()
        return cls._instance

    def load_data(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_data(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=2)

    def create(self, book):
        book_id = book.id
        # Check if an entry with the same ID already exists
        existing_entry = next((entry for entry in self.data if entry.get('id') == str(book_id)), None)

        if existing_entry is None:
            # If entry doesn't exist, create it
            self.data.append(book.to_dict())
            self.save_data()
            return True
        else:
            return False

    def delete_by_id(self, book_id):
        for book_data in self.data:
            if 'id' in book_data and book_data['id'] == str(book_id):
                self.data.remove(book_data)
                self.save_data()
                return True
        return False 

    def find_all(self):
        return [Book.from_dict(book_data) for book_data in self.data]
    
    def find_by_id(self, book_id):
        for book_data in self.data:
            if 'id' in book_data and book_data['id'] == str(book_id):
                return Book.from_dict(book_data)
        return None

    def get_last_access_by_lastAccess(self):
        if not self.data:
            return None  
        
        valid_entries = [entry for entry in self.data if entry.get('lastAccess') is not None]
        if not valid_entries:
            return None  

        sorted_data = sorted(
            valid_entries,
            key=lambda x: datetime.strptime(x['lastAccess'], '%Y-%m-%d %H:%M:%S.%f'),
            reverse=True 
        )
        last_read_book = sorted_data[0]
        return Book.from_dict(last_read_book)

    def update_last_read_page_by_id(self, book_id, page):
        for book_data in self.data:
            if 'id' in book_data and book_data['id'] == str(book_id):
                book_data['lastAccess'] = str(datetime.now())
                total_pages = book_data['pages']
                
                if 1 <= page <= total_pages:
                    book_data['currentPage'] = page
                    self.save_data()
                    return True
        return False
    def get_last_read_page_by_id(self, book_id):
        for book_data in self.data:
            if 'id' in book_data and book_data['id'] == str(book_id):
                return book_data['currentPage']
        return None

    def get_metadata_by_id(self, book_id):
        for book_data in self.data:
            if 'id' in book_data and book_data['id'] == str(book_id):
                metadata = {
                    'title': book_data.get('title'),
                    'author': book_data.get('author'),
                    'year': book_data.get('year'),
                    'language': book_data.get('language'),
                    'read_percentage': round((book_data.get('currentPage')/book_data.get('pages'))*100,2),
                    'currentPage': book_data.get('currentPage')
                }
                return metadata
        return None