from django.db import models

# Create your models here.

class food_diary(models.Model):
    mfg_code = models.CharField(max_length=20)
    food_id = models.IntegerField(primary_key=True)
    food_name = models.CharField(max_length=100)
    description = models.CharField(max_length=700)
    food_type = models.CharField(max_length=105)
    calories = models.IntegerField()
    protein = models.FloatField()
    fats = models.FloatField()
    carbohydrates = models.FloatField()
    link_of_image = models.URLField(max_length=2000)
    link_of_recipie = models.URLField(max_length=800)
    purchasing_link = models.URLField(max_length=800)
    
    def __str__(self):
        return self.food_name

class meal(models.Model): 
    meal_type=models.CharField(max_length=50)
    def __str__(self):
        return self.meal_type

class Transaction_det(models.Model):
    email_id = models.EmailField()
    date = models.DateField()
    food_name = models.CharField(max_length=30)
    calories = models.IntegerField()
    quantity = models.IntegerField()
    meal_type = models.CharField(max_length=25)
    

class Temporary(models.Model):
    food_name = models.CharField(max_length=30, primary_key=True)
    calories = models.IntegerField()
    quantity = models.IntegerField()
    meal_type = models.CharField(max_length=25)

class Unsaved(models.Model):
    email_id = models.EmailField()
    date = models.DateField()
    food_name = models.CharField(max_length=30)
    calories = models.IntegerField()
    quantity = models.IntegerField()
    meal_type = models.CharField(max_length=25)

class Purchase_det(models.Model):
    email_id = models.EmailField()
    date = models.DateField()
    mfg_code = models.CharField(max_length=20)
    food_id = models.IntegerField(primary_key=True)
    food_name = models.CharField(max_length=30)
    calories = models.IntegerField()
    protein = models.FloatField()
    fats = models.FloatField()
    carbohydrates = models.FloatField()
    quantity = models.IntegerField()

class Temporary_purchase(models.Model):
    mfg_code = models.CharField(max_length=20)
    food_id = models.IntegerField(primary_key=True)
    food_name = models.CharField(max_length=30)
    calories = models.IntegerField()
    protein = models.FloatField()
    fats = models.FloatField()
    carbohydrates = models.FloatField()
    quantity = models.IntegerField()

class Unsaved_purchase(models.Model):
    email_id = models.EmailField()
    date = models.DateField()
    mfg_code = models.CharField(max_length=20)
    food_id = models.IntegerField(primary_key=True)
    food_name = models.CharField(max_length=30)
    calories = models.IntegerField()
    protein = models.FloatField()
    fats = models.FloatField()
    carbohydrates = models.FloatField()
    quantity = models.IntegerField()

