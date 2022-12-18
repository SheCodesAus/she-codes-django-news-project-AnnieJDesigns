from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content','image_field']
        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'),
            attrs={'class':'form-control', 
            'placeholder':'Select a date','type':'date'}),
            }
        labels = {
            'title': 'Title',
            'content': 'Content',
            'image': 'Image URL',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter title up to 10 words'}),
            
           
        }
    
ORDER_CHOICE = {
    ('','newest first'), 
    ('oldest first')
}
        