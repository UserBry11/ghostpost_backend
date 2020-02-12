from django import forms


class CreateForm(forms.Form):
    title = forms.CharField(max_length=30)
    boolean = forms.BooleanField()
    content = forms.CharField(widget=forms.Textarea)
    upvotes = forms.IntegerField()
    downvotes = forms.IntegerField()
