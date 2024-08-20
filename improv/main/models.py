from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    photo = models.ImageField(upload_to="players/")

    def __str__(self):
        return self.name

class Show(models.Model):
    name = models.CharField(max_length=64)
    tagline = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to="shows/")
    location = models.CharField(max_length=128)
    postcode = models.IntegerField(null=True, blank=True)
    time = models.DateTimeField()
    
    def __str__(self):
        return f"{self.name} - {self.time.date()}"