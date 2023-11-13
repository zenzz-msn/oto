from ..db.LibraryDatabase import LibraryDatabase
from ..db.StoreDatabase import StoreDatabase
from ..model.kindle_model import Book

class LibraryService:
    json_db_user = LibraryDatabase('library.json')
    json_db = StoreDatabase('data.json')

    @classmethod
    def add_book(cls, id):
        res = cls.json_db.find_by_id(id)
        if res:
            created = cls.json_db_user.create(res)
            if created:
                return {"msg": "Added to Library Successfully"}, 201
        return {"msg": "Failed to create resource"}, 404

    @classmethod
    def remove_book(cls, id):
        res = cls.json_db_user.delete_by_id(id)
        if res:
            return {"msg": "Removed Successfully"}, 200
        return {"msg": "Book not found or already removed"}, 404

    @classmethod
    def get_last_read_book(cls):
        res = cls.json_db_user.get_last_access_by_lastAccess()
        if res:
            return {"msg": {"data": res.to_dict()}}, 200
        return {"msg": "Book not found"}, 404

    @classmethod
    def get_all_books(cls):
        all_books = cls.json_db_user.find_all()
        res = [book.to_dict() for book in all_books]
        return {"msg": {"data": res}}, 200

    @classmethod
    def update_read_page(cls, id, page):
        res = cls.json_db_user.update_last_read_page_by_id(id, page)
        if res:
            return {"msg": {"data": "Updated read page & latest access"}}, 200
        return {"msg": "Not a valid page or book not found"}, 404

    @classmethod
    def get_last_read_page(cls, id):
        res = cls.json_db_user.get_last_read_page_by_id(id)
        if res:
            return {"msg": {"data": res}}, 200
        return {"msg": "Not started reading this book"}, 404

    @classmethod
    def get_book_metadata(cls, id):
        res = cls.json_db_user.get_metadata_by_id(id)
        if res:
            return {"msg": {"data": res}}, 200
        return {"msg": "Resource not found"}, 404
