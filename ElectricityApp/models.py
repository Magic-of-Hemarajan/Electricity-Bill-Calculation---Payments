from django.db import models
from django.contrib.auth.models import User
    
class payments(models.Model):
    username = models.ForeignKey(User,on_delete = models.CASCADE)
    number =models.IntegerField()     
    name=models.CharField(max_length=30)       
    unit=models.IntegerField(null=True,blank=True)            
    price=models.CharField(max_length=30)
    receipt=models.IntegerField()
    date=models.DateField()
    

    def __str__ (self):

        return self.receipt