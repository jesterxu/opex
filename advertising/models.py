# -*- coding: windows-1254 -*-
from django.db import models
from django.contrib.auth.models import User
from tagging.fields import TagField
from tagging.models import Tag
from unidecode import unidecode

class Banner(models.Model):
   title    	    = models.CharField(max_length=255, verbose_name="Title", help_text = "Advertising Title")
   chef_title	    = models.CharField(max_length=255, verbose_name="Title Chef", help_text = "Title Chef", blank=True) 
   
   description    	    = models.CharField(max_length=500, verbose_name="Description", help_text = "Advertising Description")
   description_chef	    = models.CharField(max_length=500, verbose_name="Description Chef", help_text = "Description Chef", blank=True)
   
   link				= models.URLField()
   
   picture			= models.ImageField(upload_to="picture/", help_text="260x180 Onerilir")
   
   publication		= models.BooleanField(verbose_name="Does Publicate?", default=True, help_text = "Does Publicate?")
   
   created 	    = models.DateTimeField(auto_now_add=True, verbose_name="Created History")
   ending			= models.DateTimeField(verbose_name="Ending History")

   author			= models.ForeignKey(User, verbose_name="Author")

   def __unicode__(self):
       return self.title
	   
   def _get_url(self):
       self._require_file()
       return self.storage.url(self.name)
   url = property(_get_url)
	   
   def save(self, *args, **kwargs):
       self.chef_title = unidecode(self.title)
       super(Banner, self).save(*args, **kwargs)
	  
       self.description_chef = unidecode(self.description)
       super(Banner, self).save(*args, **kwargs)
	   
   class Meta:
	   verbose_name_plural = "Banners"

class TextLink(models.Model):
   title    	    = models.CharField(max_length=255, verbose_name="Title", help_text = "Advertising Title")
   chef_title	    = models.CharField(max_length=255, verbose_name="Title Chef", help_text = "Title Chef", blank=True) 
   
   description    	    = models.CharField(max_length=500, verbose_name="Description", help_text = "Advertising Description")
   description_chef	    = models.CharField(max_length=500, verbose_name="Description Chef", help_text = "Description Chef", blank=True)
   
   sira				= models.IntegerField()
   
   link				= models.URLField()
   
   publication		= models.BooleanField(verbose_name="Publicate?", default=True, help_text = "Publicate?")
   
   created 	    = models.DateTimeField(auto_now_add=True, verbose_name="Created History")
   ending			= models.DateTimeField(verbose_name="Ending History")

   author			= models.ForeignKey(User, verbose_name="Author")

   def __unicode__(self):
       return self.title
	   
   def save(self, *args, **kwargs):
       self.chef_title = unidecode(self.title)
       super(TextLink, self).save(*args, **kwargs)
	  
       self.description_chef = unidecode(self.description)
       super(TextLink, self).save(*args, **kwargs)
	   
   class Meta:
	   verbose_name_plural = "Text Links"
	   
class Demonstrations(models.Model):
   PICTURE = (
	('icon-glass','icon-glass'),
	('icon-music','icon-music'),
	('icon-search','icon-search'),
	('icon-envelope','icon-envelope'),
	('icon-heart','icon-heart'),
	('icon-star','icon-star'),
	('icon-star-empty','icon-star-empty'),
	('icon-user','icon-user'),
	('icon-film','icon-film'),
	('icon-th-large','icon-th-large'),
	('icon-th','icon-th'),
	('icon-th-list','icon-th-list'),
	('icon-ok','icon-ok'),
	('icon-remove','icon-remove'),
	('icon-zoom-in','icon-zoom-in'),
	('icon-zoom-out','icon-zoom-out'),
	('icon-off','icon-off'),
	('icon-signal','icon-signal'),
	('icon-cog','icon-cog'),
	('icon-trash','icon-trash'),
	('icon-home','icon-home'),
	('icon-file','icon-file'),
	('icon-time','icon-time'),
	('icon-road','icon-road'),
	('icon-download-alt','icon-download-alt'),
	('icon-download','icon-download'),
	('icon-upload','icon-upload'),
	('icon-inbox','icon-inbox'),
	('icon-play-circle','icon-play-circle'),
	('icon-repeat','icon-repeat'),
	('icon-refresh','icon-refresh'),
	('icon-list-alt','icon-list-alt'),
	('icon-lock','icon-lock'),
	('icon-flag','icon-flag'),
	('icon-headphones','icon-headphones'),
	('icon-volume-off','icon-volume-off'),
	('icon-volume-down','icon-volume-down'),
	('icon-volume-up','icon-volume-up'),
	('icon-qrcode','icon-qrcode'),
	('icon-barcode','icon-barcode'),
	('icon-tag','icon-tag'),
	('icon-tags','icon-tags'),
	('icon-book','icon-book'),
	('icon-bookmark','icon-bookmark'),
	('icon-print','icon-print'),
	('icon-camera','icon-camera'),
	('icon-font','icon-font'),
	('icon-bold','icon-bold'),
	('icon-italic','icon-italic'),
	('icon-text-height','icon-text-height'),
	('icon-text-width','icon-text-width'),
	('icon-align-left','icon-align-left'),
	('icon-align-center','icon-align-center'),
	('icon-align-right','icon-align-right'),
	('icon-align-justify','icon-align-justify'),
	('icon-list','icon-list'),
	('icon-indent-left','icon-indent-left'),
	('icon-indent-right','icon-indent-right'),
	('icon-facetime-video','icon-facetime-video'),
	('icon-picture','icon-picture'),
	('icon-pencil','icon-pencil'),
	('icon-map-marker','icon-map-marker'),
	('icon-adjust','icon-adjust'),
	('icon-tint','icon-tint'),
	('icon-edit','icon-edit'),
	('icon-share','icon-share'),
	('icon-check','icon-check'),
	('icon-move','icon-move'),
	('icon-step-backward','icon-step-backward'),
	('icon-fast-backward','icon-fast-backward'),
	('icon-backward','icon-backward'),
	('icon-play','icon-play'),
	('icon-pause','icon-pause'),
	('icon-stop','icon-stop'),
	('icon-forward','icon-forward'),
	('icon-fast-forward','icon-fast-forward'),
	('icon-step-forward','icon-step-forward'),
	('icon-eject','icon-eject'),
	('icon-chevron-left','icon-chevron-left'),
	('icon-chevron-right','icon-chevron-right'),
	('icon-plus-sign','icon-plus-sign'),
	('icon-minus-sign','icon-minus-sign'),
	('icon-remove-sign','icon-remove-sign'),
	('icon-ok-sign','icon-ok-sign'),
	('icon-question-sign','icon-question-sign'),
	('icon-info-sign','icon-info-sign'),
	('icon-screenshot','icon-screenshot'),
	('icon-remove-circle','icon-remove-circle'),
	('icon-ok-circle','icon-ok-circle'),
	('icon-ban-circle','icon-ban-circle'),
	('icon-arrow-left','icon-arrow-left'),
	('icon-arrow-right','icon-arrow-right'),
	('icon-arrow-up','icon-arrow-up'),
	('icon-arrow-down','icon-arrow-down'),
	('icon-share-alt','icon-share-alt'),
	('icon-resize-full','icon-resize-full'),
	('icon-resize-small','icon-resize-small'),
	('icon-plus','icon-plus'),
	('icon-minus','icon-minus'),
	('icon-asterisk','icon-asterisk'),
	('icon-exclamation-sign','icon-exclamation-sign'),
	('icon-gift','icon-gift'),
	('icon-leaf','icon-leaf'),
	('icon-fire','icon-fire'),
	('icon-eye-open','icon-eye-open'),
	('icon-eye-close','icon-eye-close'),
	('icon-warning-sign','icon-warning-sign'),
	('icon-plane','icon-plane'),
	('icon-calendar','icon-calendar'),
	('icon-random','icon-random'),
	('icon-comment','icon-comment'),
	('icon-magnet','icon-magnet'),
	('icon-chevron-up','icon-chevron-up'),
	('icon-chevron-down','icon-chevron-down'),
	('icon-retweet','icon-retweet'),
	('icon-shopping-cart','icon-shopping-cart'),
	('icon-folder-close','icon-folder-close'),
	('icon-folder-open','icon-folder-open'),
	('icon-resize-vertical','icon-resize-vertical'),
	('icon-resize-horizontal','icon-resize-horizontal'),
	('icon-hdd','icon-hdd'),
	('icon-bullhorn','icon-bullhorn'),
	('icon-bell','icon-bell'),
	('icon-certificate','icon-certificate'),
	('icon-thumbs-up','icon-thumbs-up'),
	('icon-thumbs-down','icon-thumbs-down'),
	('icon-hand-right','icon-hand-right'),
	('icon-hand-left','icon-hand-left'),
	('icon-hand-up','icon-hand-up'),
	('icon-hand-down','icon-hand-down'),
	('icon-circle-arrow-right','icon-circle-arrow-right'),
	('icon-circle-arrow-left','icon-circle-arrow-left'),
	('icon-circle-arrow-up','icon-circle-arrow-up'),
	('icon-circle-arrow-down','icon-circle-arrow-down'),
	('icon-globe','icon-globe'),
	('icon-wrench','icon-wrench'),
	('icon-tasks','icon-tasks'),
	('icon-filter','icon-filter'),
	('icon-briefcase','icon-briefcase'),
	('icon-fullscreen','icon-fullscreen'),
   )
   
   title    	    = models.CharField(max_length=255, verbose_name="Title", help_text = "Advertising Title")
   chef_title	    = models.CharField(max_length=255, verbose_name="Title Chef", help_text = "Title Chef", blank=True) 
   slug      	    = models.SlugField(max_length=255, verbose_name="Slug")
   
   description    	    = models.CharField(max_length=500, verbose_name="Description", help_text = "Advertising Description")
   description_chef	    = models.CharField(max_length=500, verbose_name="Description Chef", help_text = "Description Chef", blank=True)
   
   picture			= models.CharField(max_length=50, verbose_name="Advertising Picture", help_text = "Advertising Picture", choices=PICTURE)
  
   content       	= models.TextField(verbose_name="All Content", help_text = "All Content", blank=True)
   
   publication		= models.BooleanField(verbose_name="Publicate?", default=True, help_text = "Publicate?")
   
   created 	    = models.DateTimeField(auto_now_add=True, verbose_name="Created History")
   modified		= models.DateTimeField(auto_now=True, verbose_name="Modified History")

   author			= models.ForeignKey(User, verbose_name="Author")

   def __unicode__(self):
       return self.title
	   
   def save(self, *args, **kwargs):
       self.chef_title = unidecode(self.title)
       super(Demonstrations, self).save(*args, **kwargs)
	  
       self.description_chef = unidecode(self.description)
       super(Demonstrations, self).save(*args, **kwargs)
	   
   class Meta:
	   verbose_name_plural = "Demonstration Texts"
	   
   def get_absolute_url(self):
	   return "/demonstration/%s/" %self.slug
