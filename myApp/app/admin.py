from django.contrib import admin

from myApp.app.models import Book, Author

admin.site.register(Book)
admin.site.register(Author)