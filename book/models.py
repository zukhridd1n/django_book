from django.contrib.auth import password_validation
from django.contrib.auth.models import AbstractUser, User, Group, Permission
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Users(AbstractUser):
    middle_name = models.CharField(max_length=56, null=True, blank=True)
    avatar = models.ImageField(upload_to="avatar/", null=True, blank=True)


class Book(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=128)
    published = models.DateField()
    isbn = models.CharField(max_length=128, unique=True)
    language = models.CharField(max_length=12, blank=True, null=True)
    page = models.IntegerField()
    authors = models.ManyToManyField("Author")
    genres = models.ManyToManyField("Genre", "books")
    cover = models.ImageField(upload_to="book_cover/")

    def __str__(self):
        return self.title


class Bookshelf(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(Users, models.CASCADE, "shelfs")
    books = models.ManyToManyField(Book, "shelfs")


class BookReview(models.Model):
    body = models.TextField()
    book = models.ForeignKey(Book, models.CASCADE, "reviws")
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    owner = models.ForeignKey(Users, models.CASCADE, "reviews")
    like_count = models.IntegerField(default=0)


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    website = models.URLField(max_length=128, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    avatar = models.ImageField(upload_to="author_avatar/", default="avatar.jpg")
    genre = models.ForeignKey("Genre", models.SET_NULL, null=True)


class Genre(models.Model):
    name = models.CharField(max_length=28)


class BlockedUsers(models.Model):
    name = models.CharField(max_length=28)
    address = models.CharField(max_length=28)

    def __str__(self):
        return self.name
