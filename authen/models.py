from django.db import models

# Create your models here.

class users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    admission_year = models.DateField()
    phone_number = models.CharField(max_length=20)
    self_introduce = models.TextField(null=True)


