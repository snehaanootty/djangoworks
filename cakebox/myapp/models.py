from django.db import models

class Cake(models.Model):
    name=models.CharField(max_length=200)
    flavour=models.CharField(max_length=200)
    options=(
        ("round","round"),
        ("square","square"),
        ("heart","heart"),
        ("other","other")
    )
    shape=models.CharField(max_length=200,choices=options,default="round",blank=True,null=True)
    layer=models.CharField(max_length=100)
    description=models.CharField(max_length=300,null=True,blank=True)
    weight=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    pic=models.ImageField(upload_to="pictures",null=True,blank=True)

    def __str__(self):
        return self.name

