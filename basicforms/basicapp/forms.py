from django import forms
#from django.core import validators

from basicapp.models import MyModel

# def check_for_z(value):
#     if value[0] != 'z':
#         raise forms.ValidationError('Needs to start with Z')

# class FormName(forms.Form):
#     name = forms.CharField(validators=[check_for_z])
#     email = forms.EmailField()
#     verify_email = forms.EmailField(label='Enter your email again:')
#     text = forms.CharField(widget=forms.Textarea)
#     botcatcher = forms.CharField(required=False,
#                                  widget=forms.HiddenInput,
#                                  validators=[validators.MaxLengthValidator(0)])
    
#     def clean(self):
#         all_clean = super().clean()
#         email = all_clean['email']
#         vmail = all_clean['verify_email']

#         if email != vmail:
#             raise forms.ValidationError('Match doesnt match')