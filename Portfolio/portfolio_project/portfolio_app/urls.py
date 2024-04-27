from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_achievement, name='add_achievement'),
    path('achievement/delete/', views.delete_achievement_by_name, name='delete_achievement_by_name'),
    path('add_skills/', views.add_skills, name='add_skills'),
    path('skill/delete/', views.delete_skill_by_title, name='delete_skill_by_title'),
    path('add_resume/', views.add_resume, name='add_resume'),
    path('delete/', views.delete_resume, name='delete_resume'),
    path('delete_achievement/', views.delete_achievement, name='delete_achievement'),
    path('add_qualifications/', views.add_qualifications, name='add_qualifications'),
    path('add_workexperience/', views.add_workexperience, name='add_workexperience'),
    path('delete_workexperience/', views.delete_workexperiences, name='delete_workexperiences'),
    path('add_education/', views.add_education, name='add_education'),
     path('delete_education/', views.delete_education, name='delete_education'),
    # Add other URL patterns as needed
]



