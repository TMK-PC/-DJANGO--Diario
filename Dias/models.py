from django.db import models

# Create your models here.

class Dias(models.Model):

    id = models.AutoField(primary_key=True)
    data = models.CharField(max_length=10)
    topicos = models.CharField(max_length=1000000000, blank=True, null=True)
    descricao = models.CharField(max_length=1000000000000000000)


    def __str__(self):
        return f"{self.data}"