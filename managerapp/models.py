from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class UserLoginDetails(models.Model):
    # - A password field to store the password for the corresponding site.
    # - I used a charfield because django automatically hashes the password field
    password = models.CharField(max_length=150)
    url = models.URLField()
    username = models.CharField(max_length=150)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('credential_detail', args=[self.id])
