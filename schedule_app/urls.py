from django.urls import path
from . import views

urlpatterns = [
    #path function defines a url pattern
    #'' is empty to represent based path to app
    # views.index is the function defined in views.py
    # name='index' parameter is to dynamically create url
    # example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),
    path('planners/', views.PlannerListView.as_view(), name= 'planners'),
    path('planner/<int:pk>', views.PlannerDetailView.as_view(), name='planner-detail'),
    path('planner/create_planner/', views.createPlanner, name='create_planner'),
    path('planner/<int:planner_id>/update_planner/', views.updatePlanner, name='update_planner'),
    path('planner/<int:planner_id>/delete_planner/', views.deletePlanner, name='delete_planner'),
]
