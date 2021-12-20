from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import phonenumbers
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

from likes.models import Likes


SIGNUP_MODE = (
    ("EMAIL", "EMAIL"),
    ("PHONE", "PHONE")
)


class UserManager(BaseUserManager):
    def create_superuser(self, email, username, first_name, last_name, phone_number, signup_mode, password, date_of_birth, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError("Super user must have is_staff as true")

        if other_fields.get('is_superuser') is not True:
            raise ValueError("Super user must have is_superuser as true")

        return self.create_user(email, username, first_name, last_name, phone_number, signup_mode, password, date_of_birth, **other_fields)

    def create_user(self, email, username, first_name, last_name, phone_number, signup_mode, password, date_of_birth, **other_fields):
        email = self.normalize_email(email)

        if not signup_mode and signup_mode not in ["EMAIL", "PHONE"]:
            raise ValueError(
                "Selected a valid signup either 'EMAIL' or 'PHONE'")

        if signup_mode == "EMAIL" and not email:
            raise ValueError("Email is required for email mode of sign up")

        if signup_mode == "PHONE" and not (len(phone_number) < 10):
            raise ValueError("Phone is required for phone mode of sign up")

        if signup_mode == "PHONE" and not phonenumbers.is_valid_number(phonenumbers.parse(phone_number)):
            raise ValueError("Invalid phone number was provided")

        user = self.model(email=email, username=username,
                          first_name=first_name, last_name=last_name, date_of_birth=date_of_birth, **other_fields)

        user.set_password(password)

        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=True,
                              null=True, max_length=225)
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    username = models.CharField(unique=True, max_length=225,)
    phone_number = PhoneNumberField(blank=True)
    date_of_birth = models.DateField()
    signup_mode = models.CharField(choices=SIGNUP_MODE, max_length=10)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email', 'last_name', 'first_name',
                       'date_of_birth', 'phone_number', 'signup_mode']

    def __str__(self) -> str:
        return self.username


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True, upload_to='profile_pics')
    followers = models.ManyToManyField(User, blank=True, related_name='user_followers')
    followings = models.ManyToManyField(User, blank=True, related_name='user_followings')
    likes = models.ManyToManyField(Likes, blank=True)

    def followers_count(self):
        return self.followers.all().count()

    def followings_count(self):
        return self.followings.all().count()

    def likes_count(self):
        return self.likes.all().count()
