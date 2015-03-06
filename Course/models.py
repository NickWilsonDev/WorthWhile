from django.db import models
from django.forms import ModelForm, Form
from django import forms

# Create your models here.

class Course(models.Model):
    #Title
    title = models.CharField("Course Title", max_length=60, \
                             default="Name it something good.")
 
    #Description maybe should be textfield instead
    description = models.CharField("Description", max_length=200)

    #instructor
    instructor = models.CharField("Instructor", max_length=60, \
                                  default="Django Guru")

    #Duration (only values of 2 or 8 weeks)
    duration = models.CharField("Course Duration", max_length=10)

    #Course Art (upload field)
    art = models.ImageField(upload_to='', blank=True, null=True)


class CourseForm(ModelForm, Form):
    CHOICES = (('2', '2 Weeks'), ('8', '8 Weeks'))

    duration = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    art = forms.FileField()
    class Meta:
        model = Course
        widgets = {
            'description' : forms.Textarea(attrs = {'cols' : 60, 'rows' : 10})
        }
        fields = ['title', 'description', 'instructor', 'duration', 'art']
