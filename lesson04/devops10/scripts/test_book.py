from book.models import Publisher, Book


b = Book.objects.all()
print(b)