from django.contrib import admin
from .models import Article,Comment
# Register your models here.

admin.site.register(Comment)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    
    list_display = ["title","author","created_date"]  # title ve author bilgisi görülücek
    list_display_links = ["title","created_date"]
    search_fields = ["title"]  # arama alanı oluşturduk
    list_filter = ["created_date"] #oluşturma tarihine göre süzgeç
    class Meta:  #Meta yazmamız lazım
        model = Article
