from django import forms


class TodoForm(forms.Form):
    topic = forms.CharField(max_length=100)
    descrption = forms.CharField(max_length=100)
