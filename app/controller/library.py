from flask import Blueprint, request
from ..service.library_service import LibraryService
import uuid

library = Blueprint("library",__name__,url_prefix="/library")


@library.route("/", methods=['GET'])
def get_all_books_route():
    return LibraryService.get_all_books()


@library.route("/<uuid:id>/", methods=['GET'])
def read_page_or_get_book_metadata(id):
    page = request.args.get('page', type=int)
    if page is not None:
        return LibraryService.update_read_page(id, page)
    else:
        return LibraryService.get_book_metadata(id)

@library.route("/<uuid:id>/", methods=['POST', 'DELETE'])
def remove_book_or_get_book_metadata_route(id):
    if request.method == "POST":
        return LibraryService.add_book(id)
    elif request.method == "DELETE":
        return LibraryService.remove_book(id)


@library.route("/last_read/", methods=['GET'])
def get_last_read_book_route():
    return LibraryService.get_last_read_book()


@library.route("/<uuid:id>/last_read_page/", methods=['GET'])
def get_last_read_page_route(id):
    return LibraryService.get_last_read_page(id)

