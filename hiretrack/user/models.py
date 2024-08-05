# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager,AbstractBaseUser,PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings




class BaseModel(models.Model):
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='%(class)s_createdby')
   updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='%(class)s_modifiedby', null=True, blank=True)

   class Meta:
       abstract = True

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin,BaseModel):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(unique=True, null=True, blank=True)
    password = models.CharField(max_length=128)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

class UserDetail(BaseModel):
    CANDIDATE = 'candidate'
    INTERVIEWER = 'interviewer'

    ROLE_CHOICES = [
        (CANDIDATE, 'Candidate'),
        (INTERVIEWER, 'Interviewer'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user_detail')
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=CANDIDATE)
    gender = models.CharField(max_length=10)
    profile_picture = models.CharField(max_length=255)
    address = models.TextField()
    
    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    

