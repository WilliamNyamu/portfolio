from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser
# Create your models here.

class CustomUserManager(UserManager):
    """Custom user manager that uses email as the primary identifier"""
    def create_user(self, email, password = None, **extra_fields):
        # Ensure the email is not empty
        if not email:
            raise ValueError("Email field cannot be empty")
        # sanitize the email
        email = self.normalize_email(email)
        # create the user
        user = self.model(email = email, **extra_fields)
        # for password hashing
        user.set_password(user)
        # save the user in the db
        user.save(using = self.db)
        return user
    
    def create_superuser(self, username, email, password, **extra_fields):
        # stamp the superuser file
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # validation checks
        if extra_fields.get('is_admin') is not True:
            raise ValueError("is_admin should be true")
        if extra_fields.get('is_staff') is not True:
            raise ValueError("is staff should be true")
        
        return self.create_user(email, password, **extra_fields)
    
class CustomUser(AbstractUser):
    """Create a custom user with email as the primary identifier"""
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_picture', blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

