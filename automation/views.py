#!/usr/bin/env python
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, HttpResponse
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



import os
from selenium import selenium
from automation.models import *
from opex.settings import MEDIA_ROOT,  DIZIN

# Create your views here.

files = Files.objects.filter(hidden=False).order_by("-created")
articles = Articles.objects.filter(home_hard=True).order_by("-created")[:5]
categories = Categories.objects.order_by("title")
mcategories = mCategories.objects.order_by("title")
pages = Pages.objects.order_by("title")
announcements = Announcements.objects.order_by("-created")[:5]
demonstrations = Demonstrations.objects.filter(publication=True).order_by("-created")[:5]
textlink = TextLink.objects.filter(publication=True)
banner	= Banner.objects.filter(publication=True)

def seleniumlog(request):
	os.chdir("/home/jester/Documents/swap/robotframework-seleniumlibrary-demo/")
	#os.system('python /home/jester/Documents/swap/robotframework-seleniumlibrary-demo/rundemo.py /home/jester/Documents/swap/robotframework-seleniumlibrary-demo/test_cases/login_tests')
#	os.system('python test.py')	
	return HttpResponse(open('report.html'))

def iselenium2(request,slug):	
	os.chdir("/home/jester/Documents/swap/robotframework-seleniumlibrary-demo/")
	return HttpResponse(open(slug))
    
def seleniums(request):
	ireturn=globals()
    	return render_to_response('automation.html',ireturn)
    
def upload_success(request):
    return render_to_response('fillrelease-success.html')
    
def upload_file(request):	
	if request.method=='POST':
		iform=UploadFileForm(request.POST, request.FILES)
		if iform.is_valid():
			
		    iform.save()
		    newupload=iform.save(commit=False)
		    print newupload.ip+':'+str(newupload.ifile)+':'+newupload.mediatype
		    
		    #if newupload.tasktype.find('Tracker')!=-1:
		    	#iproduct=newupload.tasktype.split('Fill')[1].split('Build')[0].strip()
		    	#print iproduct
		    	#os.system('python '+DIZIN+'automation/fillbuildtracker.py ' + iproduct+ ' '+MEDIA_ROOT+"/"+unicode(newupload.ifile)+' '+newupload.mediatype)
		    #else:
		    os.system('python '+DIZIN+'automation/fillscore.py ' + newupload.ip+ ' '+MEDIA_ROOT+"/"+unicode(newupload.ifile)+' '+newupload.mediatype)
		    os.system('rm '+MEDIA_ROOT+"/"+unicode(newupload.ifile))
		    #return HttpResponseRedirect('/fillrelease/success')
	else:
		iform=UploadFileForm(initial={'ip':request.META['REMOTE_ADDR']})
	
	ireturn=globals()
	ireturn['iform']=iform
	return render_to_response('fillrelease.html',ireturn)
#
#this is the function to handle the SW create media issues. :)
#
def generate_media(request):
	if request.method=='POST':
		iform=generateMediaForm(request.POST,request.FILES)
		iform.save()
		newupload=iform.save(commit=False)
		os.system('python '+DIZIN+'automation/generatemedia.py '+newupload.product+' '+newupload.language+' '+newupload.mediatype)
	else:
		iform=generateMediaForm()

	ireturn=globals()
	ireturn['iform']=iform
	return render_to_response('generatemedia.html',ireturn)

def handle_uploaded_file(f):
    destination=open('test.txt', 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
