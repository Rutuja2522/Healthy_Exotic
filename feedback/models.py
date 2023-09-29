from django.db import models
class Feedback(models.Model):
    name=models.CharField(max_length=20,unique=True)
    email=models.EmailField(max_length=20)
    subject=models.CharField(max_length=20)
    message=models.TextField(max_length=200)
    class Meta:
        db_table="feedback"
# Create your models here.
