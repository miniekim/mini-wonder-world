from django.contrib import admin
from .models import Article, Comment

# Register your models here.
@admin.register (Article)
class PollsAdmin(admin.ModelAdmin):
    pass
