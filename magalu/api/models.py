from django.db import models

class Product(models.Model):
    title = models.CharField('Título', max_length=50, unique=True, null=False, blank=True)
    price = models.DecimalField('Preço', max_digits=6,decimal_places=2, null=False,help_text='Favor, incluir até 6 dígitos, com 2 casas decimais'
    )
    image = models.ImageField(upload_to='product', max_length=200, null=False)
    brand = models.CharField('Marca', max_length=50, null=False)
    reviewScore = models.DecimalField('Pontuação do produto', max_digits=3, decimal_places=1, null=True, help_text='Favor, incluir até 3 dígitos, com 1 casa decimal'
    )
    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=150, null=False, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    favorite = models.ManyToManyField(Product,verbose_name='Produtos favoritos')

    def __str__(self):  
        return self.name