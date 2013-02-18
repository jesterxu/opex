from django.shortcuts import HttpResponse, redirect
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from blog.models import *
from article.models import *
from pages.models import *
from ifile.models import *
from announcement.models import *
from advertising.models import *
from django.contrib.sites.models import Site
from django.db.models import Q
from tagging.models import Tag, TaggedItem
from opex.settings import MEDIA_ROOT


# Create your views here.

def download(request, file_source):

	idownloadfile=get_object_or_404(Files, file_source=file_source)
	
	f=open(MEDIA_ROOT + "/" + file_source)
	data=f.read()
	f.close()
	

	response=HttpResponse(data,mimetype="application/octet-stream")
	response['Content-Disposition']='attachment; filename=%s' % idownloadfile.file_source

	return response

def download2(request, slug, file_source1,file_source):

	return redirect('/files/' + file_source1 + '/' + file_source)
