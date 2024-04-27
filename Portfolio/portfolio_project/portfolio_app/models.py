from django.db import models

class Achievement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='achievements/')
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=100)
    skills = models.CharField(max_length=12, choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advance', 'Advance')
    ])

    def __str__(self):
        return self.title

class Resume(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.title
    
class Experience(models.Model):
    companyname = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    current = models.CharField(max_length=12, choices=[
        ('Working', 'Working'),
        ('Finished', 'Finished')])
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.companyname


class Education(models.Model):
    DEGREE_CHOICES = (
        ('Bachelor', 'Bachelor'),
        ('Master', 'Master'),
        ('PhD', 'PhD'),
        ('Diploma', 'Diploma'),
        ('Certificate', 'Certificate'),
        ('Intermediate', 'Intermediate'),
        ('HighSchool', 'HighSchool'),
    )

    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=20, choices=DEGREE_CHOICES)
    specialization = models.CharField(max_length=100)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.degree} in {self.specialization} from {self.institution}"
