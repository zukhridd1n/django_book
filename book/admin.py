from django.contrib import admin

from book.models import Users, Book, Bookshelf, Genre, Author, BookReview, BlockedUsers


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_filter = ("username",)
    list_display = ("first_name", "last_name", "middle_name", "username")
    list_display_links = ("username",)
    search_fields = ("username", "first_name")
    date_hierarchy = "date_joined"


@admin.register(Bookshelf)
class BookshelfAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    pass

@admin.register(BlockedUsers)
class BlockedUsersAdmin(admin.ModelAdmin):
    pass