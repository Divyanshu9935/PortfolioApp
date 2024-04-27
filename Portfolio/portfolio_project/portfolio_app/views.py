from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseBadRequest
from .models import Achievement, Skill, Resume, Experience, Education
from .forms import AchievementForm, SkillForm, ResumeForm, ExperienceForm, EducationForm


def index(request):
    achievements = Achievement.objects.all()
    skills = Skill.objects.all()
    resumes = Resume.objects.all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()

    return render(request, 'index.html', {'achievements': achievements, 'skills': skills, 'resumes': resumes, 'experiences': experiences, 'educations': educations})

def achievement_detail(request, achievement_id):
    achievement = get_object_or_404(Achievement, pk=achievement_id)
    skills = Skill.objects.filter(achievement=achievement)
    return render(request, 'achievement_detail.html', {'achievement': achievement, 'skills': skills})
    
def add_achievement(request):
    if request.method == 'POST':
        form = AchievementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AchievementForm()
    return render(request, 'add_achievement.html', {'form': form})


def add_skills(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Replace 'index' with the name of your desired redirect URL
    else:
        form = SkillForm()
    return render(request, 'add_skills.html', {'form': form})

def delete_achievement_by_name(request):
    if request.method == 'POST':
        achievement_title = request.POST.get('achievement_title')
        achievements = Achievement.objects.filter(title=achievement_title)
        if not achievements.exists():
            return HttpResponseBadRequest("No achievement found with the given title.")
        
        # Delete all matching achievements
        achievements.delete()
        return redirect('index')  # Redirect to index page after deletion

    return render(request, 'delete_achievement_by_name.html')



def delete_skill_by_title(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        try:
            skill = Skill.objects.get(title=title)
            skill.delete()
            return redirect('index')  # Redirect to index page or any other desired page
        except Skill.DoesNotExist:
            # Handle the case where the skill with the provided title does not exist
            # You can render an error message or redirect to a different page
            pass  # For now, we'll just ignore it
    return render(request, 'delete_skill_by_title.html')  # Render the delete form template


def add_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ResumeForm()
    return render(request, 'add_resume.html', {'form': form})

def delete_resume(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        resume = get_object_or_404(Resume, title=title)
        resume.delete()
        return redirect('index')  # Redirect to index after deleting resume
    return render(request, 'delete_resume.html')


def delete_achievement(request):

    return render(request, 'delete_achievement.html')

def add_qualifications(request):

    return render(request, 'add_qualifications.html')



def add_workexperience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Replace 'index' with the name of your desired redirect URL
    else:
        form = ExperienceForm()
    return render(request, 'add_workexperience.html', {'form': form})

def delete_workexperiences(request):
    if request.method == 'POST':
        companyname = request.POST.get('companyname')
        try:
            workexperiences = Experience.objects.get(companyname=companyname)
            workexperiences.delete()
            return redirect('index')  # Redirect to index page or any other desired page
        except Experience.DoesNotExist:
            # Handle the case where the skill with the provided title does not exist
            # You can render an error message or redirect to a different page
            pass  # For now, we'll just ignore it
    return render(request, 'delete_workexperience.html')  # Render the delete form template



def add_education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to a success page, change 'index' to your desired URL
    else:
        form = EducationForm()
    return render(request, 'add_education.html', {'form': form})


def delete_education(request):
    if request.method == 'POST':
        degree = request.POST.get('degree')
        education = get_object_or_404(Education, degree=degree)
        education.delete()
        return redirect('index')  # Redirect to a success page, change 'index' to your desired URL
    # Handle GET request if needed
    return render(request, 'delete_education.html')

