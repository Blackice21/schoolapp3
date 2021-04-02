from django.db import models

# Create your models here.
class Principle(models.Model):
    first_name= models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    image = models.ImageField(default='nobody.jpg')

def defaultprinciple():
   return Principle.objects.get_or_create(first_name='nobody', last_name='nobody_.jpg', image='nobody.jpg')[0]

class School(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    image = models.ImageField()
    phone_number = models.CharField(max_length=7)
    principle = models.ForeignKey(Principle, default=defaultprinciple().id, null=True, on_delete=models.SET_NULL)