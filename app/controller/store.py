from flask import Blueprint, request
from ..service.store_service import StoreService

store = Blueprint("store",__name__,url_prefix="/store")

@store.route("/", methods=['GET'])
def get_all_books_route():
    result = StoreService.get_all_books()
    return result

@store.route("/<id>/", methods=['GET'])
def get_a_book_route(id):
    result = StoreService.get_a_book(id)
    return result