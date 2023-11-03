from django.db import models
from django.urls import reverse

# Create your models here.
class Planner(models.Model):
    #List of choices for major value in database, human readable name
    name = models.CharField(max_length=200)
    date = models.CharField(max_length = 200)
    description = models.CharField(max_length = 500)
    
    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.name

    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('planner-detail', args=[str(self.id)])
