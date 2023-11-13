from ..db.StoreDatabase import StoreDatabase
from ..model.kindle_model import Book

class StoreService:
    json_db = StoreDatabase('data.json')

    @classmethod
    def get_all_books(cls):
        all_books = cls.json_db.find_all()
        res = [book.to_dict() for book in all_books]
        return {"msg": {"data": res}}, 200

    @classmethod
    def get_a_book(cls,id):
        res = cls.json_db.find_by_id(id)
        return res.to_dict()
