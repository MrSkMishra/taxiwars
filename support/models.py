from django.db import models
from django.contrib.auth.models import User




class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    country_code=   models.CharField(max_length=10,blank=True, null=True)
    phone_number =  models.CharField(max_length=13, unique=True)
    otp =           models.CharField(max_length=6,blank=True, null=True)

    def __str__(self):
        # return self.phone_number      
        return f'{str(self.phone_number)}  :  id :{self.id}'



class DriverDetails(models.Model):
    details =   models.ForeignKey(Driver, on_delete=models.SET_NULL,null=True, blank=True)
    first_name =   models.CharField(max_length=40,null=True,blank=True) 
    last_name =   models.CharField(max_length=40,null=True,blank=True)
    email = models.EmailField(blank=True,null=True)
    street_address_1 =   models.CharField(max_length=40,null=True,blank=True)
    street_address_2 =   models.CharField(max_length=40,null=True,blank=True)
    city =   models.CharField(max_length=40,null=True,blank=True)
    state =   models.CharField(max_length=40,null=True,blank=True)
    driving_lisence = models.ImageField(upload_to= 'media/driving_lisence')
    aadhar_card = models.ImageField(null=True,blank=True,upload_to='media/aadhar_card')
    driver_photo = models.ImageField(null=True, blank=True,upload_to='media/driver_photo')
    driver_lat = models.CharField(max_length=50,default="")
    driver_lng =  models.CharField(max_length=50,default="")
    verified = models.BooleanField(default=False)
    

    def __str__(self):
        return f'{self.first_name}  :  id : {self.details}  :   verification :{self.verified}'

class DriverFields(models.Model):
    name = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)


    def __str__(self):
        return f'{str(self.name)} : verification :{self.verified}'


class DriverVerificationDetails(models.Model):
    details =   models.ForeignKey(Driver, on_delete=models.SET_NULL,null=True, blank=True)
    first_name =   models.CharField(max_length=40,null=True,blank=True)
    last_name =   models.CharField(max_length=40,null=True,blank=True)
    email = models.EmailField(blank=True,null=True)
    street_address_1 =   models.CharField(max_length=40,null=True,blank=True)
    street_address_2 =   models.CharField(max_length=40,null=True,blank=True)
    city =   models.CharField(max_length=40,null=True,blank=True)
    state =   models.CharField(max_length=40,null=True,blank=True)
    driving_lisence = models.ImageField()
    aadhar_card = models.ImageField(null=True,blank=True)
    driver_photo = models.ImageField(null=True, blank=True)
    driver_lat = models.CharField(max_length=50,default="")
    driver_lng =  models.CharField(max_length=50,default="")
    driver_available = models.BooleanField(default=True)
    driver_verified  = models.BooleanField(default=False)