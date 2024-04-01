from django.db import models

# modified user model
from django.contrib.auth.models import AbstractUser
class MyUser(AbstractUser):
    email = models.EmailField(blank=True, null=True)  # Make email optional
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="myuser_groups",  # Ensure this is unique and not clashing with 'auth.User.groups'
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="myuser_permissions",  # Ensure this is unique and not clashing with 'auth.User.user_permissions'
        related_query_name="user",
    )

class Key(models.Model):
    uid = models.CharField(max_length=100)
    time_remaining = models.IntegerField(default=365)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        managed = True
class Updated(models.Model):
    url = models.CharField(max_length=1000)
    version = models.IntegerField()
    class Meta:
        managed = True