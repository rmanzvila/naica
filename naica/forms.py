from django import forms
from naica.models import Poll


class PollForm(forms.ModelForm):
    """Form to render a poll creation"""

    class Meta:
        model = Poll
        fields = '__all__'
