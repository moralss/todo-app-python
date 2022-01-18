from django import forms


class Todoform(forms.Form):
    topic = forms.CharField(max_length=100)
    descrption = forms.CharField(max_length=100)
