from django.db import models


class Baza_func(models.Model):
    doctor_name = models.CharField(max_length=250)
    specialist = models.CharField(max_length=250)
    experience = models.TextField()
    caste = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    telegram_url = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)


    def __str__(self):
        return self.doctor_name

class Medic_programs(models.Model):
    service_name = models.CharField(max_length=50)
    service_price = models.CharField(max_length=50)
    first_service = models.CharField(max_length=50)
    second_service = models.CharField(max_length=50)
    third_service = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.service_name