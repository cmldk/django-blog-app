from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):  #ototmatik form oluşturcak
    class Meta:
        model = Article
        fields = ["title","content","article_image"]