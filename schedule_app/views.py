from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Planner
from .forms import PlannerForm
from django.views import generic
from django.shortcuts import redirect
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def index(request):
    # Force users to login
    if not request.user.is_authenticated:
        return redirect('login') 
    else:
        pass
    
    # Render the HTML template index.html with the data in the context variable.
    planners = Planner.objects.all()
    return render( request, 'schedule_app/index.html', {'planners': planners})

# Allow new users to sign up
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form, 'title':'register here'})

class PlannerListView(generic.ListView):
    model = Planner
    
class PlannerDetailView(generic.DetailView):
    model = Planner

# Add an item
def createPlanner(request):
    if request.method == 'POST':
        form = PlannerForm(request.POST)
        
        if form.is_valid():
            planner = form.save()
        
        return redirect("/")
    else:
        form = PlannerForm
        
    context = {'form': form}
    return render(request, 'schedule_app/planner_form.html', context)

# Edit an item
def updatePlanner(request, planner_id):
    item = Planner.objects.get(pk = planner_id)
    form = PlannerForm(instance = item)
    if request.method == 'POST':
        form = PlannerForm(request.POST, instance = item)
        
        if form.is_valid():
            form.save()
        
        return redirect('planner-detail', item.id)
    else:
        form = PlannerForm(instance = item)
    
    context = {'form': form}
    return render(request, 'schedule_app/planner_form.html', context)

# Remove an item
def deletePlanner(request, planner_id):
    item = Planner.objects.get(pk = planner_id)
    if request.method == 'POST':
        item.delete()
        return redirect("/")
    
    context = {'item': item}
    return render(request, 'schedule_app/planner_delete.html', context)

