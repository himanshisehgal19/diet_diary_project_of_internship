from django.db import models

# Create your models here.
class Main_page(models.Model):
    Food_id=models.AutoField(primary_key=True)
    Food_type=models.CharField(max_length=200)
    Description=models.TextField()
    slug=models.CharField(max_length=130)
    Link_of_image=models.URLField()
    

    def __str__(self):
        return self.Food_Type

