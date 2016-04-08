from django.db import models

# Create your models here.
class Order(models.Model):
   customer_name = models.CharField(max_length=200)
   contact_number = models.CharField(max_length=10)
   address = models.CharField(max_length=100)
   type = models.CharField(max_length=20)
   created_time = models.DateTimeField(auto_now_add=True, blank=True)
   date = models.CharField(max_length=200)
   time = models.CharField(max_length=200)


   def __str__(self):
       return str(self.contact_number)
