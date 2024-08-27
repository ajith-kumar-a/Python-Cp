from django import forms
from .models import Comment

class Comments(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        labels = {
            'user_name': 'Name',
            'user_email': 'Mail ',
            'comment': 'Comment'

        }
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'user_email':forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.NumberInput(attrs={'class': 'form-control'}),
            # Add other fields as needed
        }