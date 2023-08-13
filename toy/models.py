from django.db import models

class Customer(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    message=models.CharField(max_length=250)
    date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['id']
class Table(models.Model):
    course=models.TextField()
    duration=models.CharField(max_length=20)
    class Meta:
        ordering=['id']