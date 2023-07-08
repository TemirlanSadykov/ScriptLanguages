from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    PRIVILEGE_CHOICES = (
        ('admin', 'Admin'),
        ('customer', 'Customer'),
    )
    email = models.EmailField(unique=True)
    privilege = models.CharField(max_length=10, choices=PRIVILEGE_CHOICES)
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True)

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images')
    description = models.TextField()
    file = models.FileField(upload_to='product_files')

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)