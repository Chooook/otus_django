from django import forms
from django.core.exceptions import ValidationError

from .models import Category, Equipment


class CategoryForm(forms.ModelForm):

    name = forms.CharField(label='Category name')

    class Meta:
        model = Category
        fields = ('name', )


class EquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = ('name', 'category', 'img')

    name = forms.CharField(label='',
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Equipment name'}
                           ))
    category = forms.CheckboxInput()
    img = forms.ImageField(label='Image')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise ValidationError('Name must be longer than 3 symbols')
        return name
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if name == 'xyi':
            raise ValidationError('Too strange name, sorry')


# Form View example
class ContactForm(forms.Form):

    name = forms.CharField(label='Your name',
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',}
                           ))
