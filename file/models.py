from django.db import models
from unidecode import unidecode
from django.contrib.sitemaps import ping_google

class Files(models.Model):
   FILE_PICTURE = (
	('c','C'),
	('cplus','C++'),
	('eklenti','Eklenti'),
	('exe','Exe'),
	('gif','Gif'),
	('header','Header'),
	('html','Html'),
	('java','Java'),
	('jpeg','Jpeg'),
	('js','Js'),
	('mp3','Mp3'),
	('pdf','Pdf'),
	('php','Php'),
	('plain','Plain'),
	('png','Png'),
	('python','Python'),
	('script','Bash Script'),
	('sifreli','Sifreli'),
	('text','Text'),
	('widget','Widget'),
	('xml','Xml'),
	('zip','Zip/Rar'),	
   )
   
   title    	    = models.CharField(max_length=255, verbose_name="Title", help_text = "File Title")
   chef_title	    = models.CharField(max_length=255, verbose_name="Title Chef", help_text = "Title Chef", blank=True) 
   slug      	    = models.SlugField(max_length=255, verbose_name="Slug")
   
   description    	    = models.TextField(max_length=500, verbose_name="Description", help_text = "File Description")
   description_chef	    = models.TextField(max_length=500, verbose_name="Description Chef", help_text = "Description Chef", blank=True)
   
   ifile			= models.FileField(upload_to="upload/", blank=True)
   file_tour 	    = models.CharField(max_length=10, verbose_name="File Tour", help_text = "File Tour", blank=True)
   file_picture	    = models.CharField(max_length=255, verbose_name="File Picture", help_text = "File Picture", choices=FILE_PICTURE) 
   
   file_source		= models.CharField(max_length=255, verbose_name="File Source", help_text = "File Source", blank=True)
   
   hidden			= models.BooleanField(verbose_name="Will File Hidden?", default=False, help_text = "Will File Hidden?")
   
   created 	    = models.DateTimeField(auto_now_add=True, verbose_name="Created History")
   modified		= models.DateTimeField(auto_now=True, verbose_name="Modified History")

   def __unicode__(self):
       return self.title
	   
   def save(self, *args, **kwargs):
       self.chef_title = unidecode(self.title)
       super(Files, self).save(*args, **kwargs)
	   
       self.description_chef = unidecode(self.description)
       super(Files, self).save(*args, **kwargs)	  

       try:
           ping_google()
       except Exception:
           pass	   
	   
   class Meta:
	   verbose_name_plural = "Files"
	   
   def get_absolute_url(self):
	   return "/file/%s/" %self.slug
