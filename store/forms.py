from django import forms
from .models import Store
from .models import Store2
from .models import Store3

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['title', 'writer', 'body', 'body2','image']


class StoreForm2(forms.ModelForm):
    class Meta:
        model = Store2
        fields = ['title', 'writer', 'body', 'body2','image']

class StoreForm3(forms.ModelForm):
    class Meta:
        model = Store3
        fields = ['title', 'writer', 'body', 'body2','image']