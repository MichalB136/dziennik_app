from django import forms

from classes.models import Mark

class MarkCreateForm(forms.ModelForm):

    class Meta:
        model = Mark
        fields = ['student', 'subject',
                  'value', 'weight', 'note']