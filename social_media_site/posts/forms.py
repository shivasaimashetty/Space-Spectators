from posts.models import Comment,Post
from django import forms

class CommentForm(forms.ModelForm):

    class Meta():
        model=Comment
        fields=('text',)

class GroupPostForm(forms.ModelForm):
    class Meta():
        model=Post
        fields=('message','photo')
