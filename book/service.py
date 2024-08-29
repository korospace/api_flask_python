# import utils
from utils.helpers import generate_response

# Get Book
# ============================
def get_book(request):
    # some logic here
    # ......

    books = [
        {
            "id": 1,
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "published_year": 1960,
            "isbn": "978-0-06-112008-4"
        },
        {
            "id": 2,
            "title": "1984",
            "author": "George Orwell",
            "published_year": 1949,
            "isbn": "978-0-452-28423-4"
        },
        {
            "id": 3,
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "published_year": 1925,
            "isbn": "978-0-7432-7356-5"
        }
    ]

    return generate_response(status=200, message=f"service get_book",data=books)
    