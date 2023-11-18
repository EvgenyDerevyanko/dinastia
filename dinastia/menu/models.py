from django.db import models as m


# Create your models here.
class Category(m.Model):
    name = m.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name



class Product(m.Model):
    name = m.CharField(unique=True, max_length=100)
    price = m.DecimalField(max_digits=10, decimal_places=2)
    discription = m.TextField(max_length=2000) 
    category = m.ForeignKey(to='Category',
                            related_name='products', 
                            on_delete=m.SET_NULL,
                            null=True)
    image = m.ImageField(upload_to='product', blank=True)

    class Meta:
        ordering = ['price']
        indexes = [m.Index(fields=['id', 'name'])]

    def __str__(self):
        return self.name
