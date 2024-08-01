from django.urls import path

from book.views import RegisterView, LoginView, MyBookView, BookshelfCreateView, LogoutView, UserProfileView, \
    UserUpdateProfileView

app_name = "book"
urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("edit-profile/", UserUpdateProfileView.as_view(), name="update-profile"),
    path("my_book/", MyBookView.as_view(), name="my-book"),
    path("new-bookshelf/", BookshelfCreateView.as_view(), name="new-bookshelf"),
]
