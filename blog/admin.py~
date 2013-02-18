from django.contrib import admin
from django import forms
from blog.models import Blogs, Categories
from article.models import Articles, mCategories
from pages.models import Pages
from file.models import Files
from link.models import Link
from announcement.models import Announcements
from advertising.models import Banner, TextLink, Demonstrations
from django.db import models

class CategoriesAdmin(admin.ModelAdmin):
	list_display = ('title','description','category_picture')
	prepopulated_fields = {"slug": ("title",)}

class BlogAdmin(admin.ModelAdmin):
   list_display = ('title','author','category','description','created','modified')
   prepopulated_fields = {"slug": ("title",)}
   formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }
   class Media:
		js = ('ckeditor/ckeditor.js',)

class mCategoryAdmin(admin.ModelAdmin):
	list_display = ('title','description','category_picture')
	prepopulated_fields = {"slug": ("title",)}
	
class ArticlesAdmin(admin.ModelAdmin):
   list_display = ('title','author','category','description','created','modified')
   prepopulated_fields = {"slug": ("title",)} 
   formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }
   class Media:
		js = ('ckeditor/ckeditor.js',)  

class PagesAdmin(admin.ModelAdmin):
   list_display = ('title','author','description','created','modified')
   prepopulated_fields = {"slug": ("title",)}
   formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }
   class Media:
		js = ('ckeditor/ckeditor.js',)		

class FileAdmin(admin.ModelAdmin):
	list_display = ('title','description','file_source')
	prepopulated_fields = {"slug": ("title",)}
	
class LinkAdmin(admin.ModelAdmin):
	list_display = ('link','hits','get_short_id')
	
class AnnouncementsAdmin(admin.ModelAdmin):
   list_display = ('title','author','description','created','modified')
   prepopulated_fields = {"slug": ("title",)} 
   formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }
   class Media:
		js = ('ckeditor/ckeditor.js',)

class DemonstrationsAdmin(admin.ModelAdmin):
   list_display = ('title','author','description','created','modified')
   prepopulated_fields = {"slug": ("title",)} 
   formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }
   class Media:
		js = ('ckeditor/ckeditor.js',) 

class TextLinkAdmin(admin.ModelAdmin):
	list_display = ('title','description','ending') 
	
class BannerAdmin(admin.ModelAdmin):
	list_display = ('title','description','ending') 		
	
admin.site.register(Blogs, BlogAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Articles, ArticlesAdmin)
admin.site.register(mCategories, mCategoryAdmin)
admin.site.register(Pages, PagesAdmin)
admin.site.register(Files, FileAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Announcements, AnnouncementsAdmin)
admin.site.register(Demonstrations,DemonstrationsAdmin)
admin.site.register(TextLink, TextLinkAdmin)
admin.site.register(Banner, BannerAdmin)
