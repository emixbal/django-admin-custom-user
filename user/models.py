from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class ProfileRole(models.Model):
    name = models.CharField(max_length=20)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_role = models.ForeignKey(ProfileRole, on_delete=models.SET_NULL, null=True)
