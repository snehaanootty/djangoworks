from django.db import models

class Movie(models.Model):
    name=models.CharField(max_length=200)
    year=models.PositiveIntegerField(null=True)
    language=models.CharField(max_length=200)
    genres=models.CharField(max_length=200)
    runtime=models.CharField(max_length=200,null=True)
    posterpic=models.ImageField(upload_to="images",null=True,blank=True)

    def __str__(self):
        return self.name 
