from django.db import models
class Pizza(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
# Create your models here.
class Topping(models.Model):
    pizza=models.ForeignKey(Pizza,
    on_delete=models.CASCADE)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name