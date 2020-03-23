from django import forms
from ghostpost.models import BoastRoast


class CreateForm(forms.ModelForm):
    class Meta:
        model = BoastRoast
        fields = [
            'title',
            'boolean',
            'content',
            'upvotes',
            'downvotes',
            'post_date'
        ]
    # title = forms.CharField(max_length=30)
    # boolean = forms.BooleanField(required=False)
    # content = forms.CharField(widget=forms.Textarea)
    # upvotes = forms.IntegerField()
    # downvotes = forms.IntegerField()
