from django import forms

from .models import Person

class PostForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('firstname', 'lastname','nickname','email',)