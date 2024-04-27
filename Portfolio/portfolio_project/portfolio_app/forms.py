from django import forms
from .models import Achievement, Skill, Resume, Experience, Education

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['title', 'description', 'image']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['title', 'skills']  


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'file']



class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['companyname', 'position', 'start_date', 'end_date', 'current', 'description']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


from django import forms
from .models import Education

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institution', 'degree', 'specialization', 'start_year', 'end_year']
