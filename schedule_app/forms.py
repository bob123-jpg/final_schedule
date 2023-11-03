from django.forms import ModelForm
from .models import Planner

#create class for project form
class PlannerForm(ModelForm):
    class Meta:
        model = Planner
        fields =('name', 'date', 'description')

