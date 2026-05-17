from django.contrib import admin
from services.models import Category, Task, SubTask
from services.models import Book, Author, Post

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Task)
admin.site.register(SubTask)
