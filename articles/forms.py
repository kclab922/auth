from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    # title = forms.CharField(
    #     label='제목',
    #     widget=forms.TextInput(
    #         attrs={'class': 'form-control'}
    #     )
    # )

    # content = forms.CharField(
    #     label='내용',
    #     widget=forms.Textarea(
    #         attrs={'class': 'form-control'}
    #     )
    # )
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


