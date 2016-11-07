from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Recipe(models.Model):
    name=models.CharField(max_length=250)

    description=models.CharField(max_length=250)



    owner = models.CharField(max_length=250)



class RecipeDetails(models.Model):
    recipedescription = models.TextField(null=True)

    number = models.IntegerField()

    owner = models.CharField(max_length=250)

    recipe=models.ForeignKey(Recipe,null=True,on_delete=models.CASCADE)