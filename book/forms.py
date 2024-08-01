from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from book.models import Users, Bookshelf


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    # def clean_password(self):
    #     password = self.cleaned_data.get("password")
    #     if password:
    #         try:
    #             password_validation.validate_password(password, self.instance)
    #         except ValidationError as error:
    #             self.add_error("password", error)
    #     return password

    class Meta:
        model = Users
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "middle_name",
            "avatar",
            "password",
            "confirm_password"
        )

    def clean_username(self):
        username = self.cleaned_data["username"]
        if Users.objects.filter(username=username).exists():
            msg = 'this username already taken please choose another one'
            self.add_error('username', msg)
        return username

    def clean(self):
        if self.cleaned_data["password"] != self.cleaned_data["confirm_password"]:
            msg = "password and confirm_password must be match"
            self.add_error("confirm_password", msg)

        return self.cleaned_data

    def save(self):
        user = Users.objects.create(
            username=self.cleaned_data["username"],
            email=self.cleaned_data["email"],
            middle_name=self.cleaned_data["middle_name"],
            first_name=self.cleaned_data["first_name"],
            last_name=self.cleaned_data["last_name"],
            avatar=self.cleaned_data["avatar"],
        )
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_password(self):
        try:
            user = Users.objects.get(username=self.cleaned_data.get("username"))
            # if not user.check_password(raw_password=value):
            #     user.login_try_count=+1
            # else:
            #     user.login_try_count=0
            # user.save()
            #
        except Users.DoesNotExist:
            return self.cleaned_data.get("password")
        return self.cleaned_data.get("password")


class BookshelfForm(forms.ModelForm):
    class Meta:
        model = Bookshelf
        fields = "__all__"


class UserUpdateForm(ModelForm):
    class Meta:
        model = Users
        fields = ("first_name", "last_name", "middle_name", "email", "avatar", "username",)
