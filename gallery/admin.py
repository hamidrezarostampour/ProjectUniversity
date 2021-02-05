from django.contrib import admin
from .models import Book, Comment, Category, Star

# Register your models here.

admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Star)