from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Product(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    rasm = models.ImageField(upload_to='Maxsulot/')
    nomi = models.CharField(max_length=25)
    narxi = models.IntegerField()

    def __str__(self):
        return self.nomi

class Savatcha(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)    
    quantity = models.IntegerField()
    vaqti = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.User.first_name + "/" + self.product.nomi

    class Meta:
        verbose_name_plural="Savatcha"


class Tanlangan(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    vaqti = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.User.first_name + "/" + self.product.nomi

    class Meta:
        verbose_name_plural="tanlangan"
