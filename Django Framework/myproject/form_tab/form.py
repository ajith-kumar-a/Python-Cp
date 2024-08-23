from django import forms
from .models import Review
 
# class Feedbackform(forms.Form):
#     user_name = forms.CharField(label='Enter the name',max_length=20,
#     error_messages={
#         'required':'It is Empty Value',
#         'max_length':'Please enter a shorter name'
#     })
#     text = forms.CharField(label='Enter the Feedback',widget=forms.Textarea)
#     rating = forms.IntegerField(label='Enter the Rating',min_value=1,max_value=5)

# class Feedbackform(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = '__all__' #['user_name',rating]
#         #exclude = []

#         labels = {
#             'user_name': 'Your Name',  # Custom label for user_name field
#             'rating': 'Your Rating',   # Example of adding another custom label
#         }

#         widgets = {
#             'user_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
#             'rating': forms.NumberInput(attrs={'class': 'form-control'}),
#             # Add other fields as needed
#         }

#         error_messages = {
#             'user_name': {
#                 'required': 'Please provide your name.',
#                 'max_length': 'This name is too long.',
#             }
#         }


class Feedbackform(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            'user_name': 'Your Name',
        }
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'text':forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            # Add other fields as needed
        }