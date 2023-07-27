from django.db import models

# Create your models here.
class Item(models.Model):
    name=models.CharField(("name"), max_length=50)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=
                          (('IT','IT'),
                           ('Non It', 'Non It')))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    
class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=50,choices=(("Manager","Manager"),("SDE","SDE")))
    company=models.ForeignKey(Company,on_delete=models.CASCADE)