from django import forms
from .models import UploadImage

class UserImageForm(forms.ModelForm):
    class Meta:
        model = UploadImage  # Specify the model
        fields = '__all__'  # Include all fields from the model
