from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # fields = '__all__'
        exclude = ('user', )
        # fields = ('title', 'content', )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('user', 'article', )
        # fields = ('content', )


