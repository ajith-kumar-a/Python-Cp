from django import forms
 
class Feedbackform(forms.Form):
    user_name = forms.CharField(label='Enter the name')