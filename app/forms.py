from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        label="期限",
        widget=forms.NumberInput(attrs={
        'type': 'datetime-local',
        }))

    class Meta:
        model = Post
        exclude = ["user"]

    def __init__(self, user=None, *args, **kwargs):
        for field in self.base_fields.values():
            field.widget.attrs["class"] = "form-control"
        self.user = user
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        post_obj = super().save(commit=False)
        if self.user:
            post_obj.user = self.user
        if commit:
            post_obj.save()
        return post_obj
