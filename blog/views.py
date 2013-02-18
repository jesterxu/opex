from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from blog.models import *
from article.models import *
from pages.models import *
from file.models import *
from announcement.models import *
from advertising.models import *
from django.contrib.sites.models import Site
from django.db.models import Q
from tagging.models import Tag, TaggedItem

from selenium import selenium
import os

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

def home(request):
	blogs = Blogs.objects.order_by("-created")[:5]
	
	site = Site.objects.get_current()	
	return render_to_response('home.html', locals())

def category(request, slug):
	category = get_object_or_404(Categories, slug=slug)
	files = Files.objects.filter(hidden=False).order_by("-created")[:5]
	blogs = Blogs.objects.filter(category=category.id).filter(home_hard=True).order_by("-created")	
	categories = Categories.objects.order_by("title")
	mcategories = mCategories.objects.order_by("title")
	articles = Articles.objects.filter(home_hard=True).order_by("-created")[:5]
	pages = Pages.objects.order_by("title")
	announcements = Announcements.objects.order_by("-created")[:5]
	demonstration = Demonstrations.objects.filter(publication=True).order_by("-created")[:5]
	textlink = TextLink.objects.filter(publication=True)
	banner	= Banner.objects.filter(publication=True)
	
	site = Site.objects.get_current()	
	return render_to_response('category.html', locals())		
	
def blog(request):

	files = Files.objects.filter(hidden=False).order_by("-created")
	articles = Articles.objects.filter(home_hard=True).order_by("-created")[:5]
	categories = Categories.objects.order_by("title")
	mcategories = mCategories.objects.order_by("title")
	pages = Pages.objects.order_by("title")
	announcements = Announcements.objects.order_by("-created")[:5]
	demonstrations = Demonstrations.objects.filter(publication=True).order_by("-created")[:5]
	textlink = TextLink.objects.filter(publication=True)
	banner	= Banner.objects.filter(publication=True)
	
	
	blogs = Blogs.objects.filter(home_hard=True).order_by("-created")

	site = Site.objects.get_current()
	return render_to_response('blog.html', locals())

def post(request, slug):

	files = Files.objects.filter(hidden=False).order_by("-created")
	articles = Articles.objects.filter(home_hard=True).order_by("-created")[:5]
	categories = Categories.objects.order_by("title")
	mcategories = mCategories.objects.order_by("title")
	pages = Pages.objects.order_by("title")
	announcements = Announcements.objects.order_by("-created")[:5]
	demonstrations = Demonstrations.objects.filter(publication=True).order_by("-created")[:5]
	textlink = TextLink.objects.filter(publication=True)
	banner	= Banner.objects.filter(publication=True)
	
	blog = get_object_or_404(Blogs, slug=slug)
	
	site = Site.objects.get_current()
	return render_to_response('post.html', locals())

def label(request, tag_name):
	tag = get_object_or_404(Tag, name=tag_name)
	blogs = TaggedItem.objects.get_by_model(Blogs, tag).filter(home_hard=True)
	categories = Categories.objects.order_by("title")
	mcategories = mCategories.objects.order_by("title")
	articles = Articles.objects.filter(home_hard=True).order_by("-created")[:5]	
	files = Files.objects.filter(hidden=False).order_by("-created")[:5]
	pages = Pages.objects.order_by("title")
	announcements = Announcements.objects.order_by("-created")[:5]
	demonstrations = Demonstrations.objects.filter(publication=True).order_by("-created")[:5]
	textlink = TextLink.objects.filter(publication=True)
	banner	= Banner.objects.filter(publication=True)
	
	site = Site.objects.get_current()
	return render_to_response('label.html', locals())

def article(request, slug, kat_slug):
	article = get_object_or_404(Articles, slug=slug)
	mcategories = mCategories.objects.order_by("title")
	bcategories = Categories.objects.order_by("title")
	listarticle = Articles.objects.order_by("-created")
	files =Files.objects.filter(hidden=False).order_by("-created")[:5]
	pages = Pages.objects.order_by("title")
	announcements = Announcements.objects.order_by("-created")[:5]
	demonstrations = Demonstrations.objects.filter(publication=True).order_by("-created")[:5]
	textlink = TextLink.objects.filter(publication=True)
	banner	= Banner.objects.filter(publication=True)
	
	site = Site.objects.get_current()
	return render_to_response('article.html', locals())
	
def articles(request):
	articles = Articles.objects.filter(home_hard=True).order_by("-created")
	categories = Categories.objects.order_by("title")
	mcategories = mCategories.objects.order_by("title")
	files = Files.objects.filter(hidden=False).order_by("-created")[:5]
	listarticle = Articles.objects.order_by("-created")[:5]
	pages = Pages.objects.order_by("title")
	announcements = Announcements.objects.order_by("-created")[:5]
	demonstrations = Demonstrations.objects.filter(publication=True).order_by("-created")[:5]
	textlink = TextLink.objects.filter(publication=True)
	banner	= Banner.objects.filter(publication=True)
	
	site = Site.objects.get_current()
	return render_to_response('articles.html', locals())	
	
def mcategory(request, kat_slug):
	category = get_object_or_404(mCategories, slug=kat_slug)	
	articles = Articles.objects.filter(category=category.id).filter(home_hard=True).order_by("-created")	
	articlelist	= Articles.objects.filter(home_hard=True).order_by("-created")	
	categories = mCategories.objects.order_by("title")
	bcategories = Categories.objects.order_by("title")
	files = Files.objects.filter(hidden=False).order_by("-created")[:5]	
	pages = Pages.objects.order_by("title")
	announcements = Announcements.objects.order_by("-created")[:5]
	demonstrations = Demonstrations.objects.filter(publication=True).order_by("-created")[:5]
	textlink = TextLink.objects.filter(publication=True)
	banner	= Banner.objects.filter(publication=True)
	
	site = Site.objects.get_current()	
	return render_to_response('mcategory.html', locals())	
	
def mlabel(request, tag_name):
	tag = get_object_or_404(Tag, name=tag_name)
	categories = TaggedItem.objects.get_by_model(Categories, tag).filter(home_hard=True)
	articlelist = Articles.objects.filter(anasayfa_sabit=True).order_by("-created")
	files = Files.objects.filter(hidden=False).order_by("-created")[:5]
	mcategories = mCategories.objects.order_by("title")
	categories = Categories.objects.order_by("title")
	page = Pages.objects.order_by("title")
	announcements = Announcements.objects.order_by("-created")[:5]
	demonstrations = Demonstrations.objects.filter(publication=True).order_by("-created")[:5]
	textlink = TextLink.objects.filter(publication=True)
	banner	= Banner.objects.filter(publication=True)
	
	site = Site.objects.get_current()
	return render_to_response('mlabel.html', locals())	

def pages(request, slug):
	page = get_object_or_404(Pages, slug=slug)
	categories = Categories.objects.order_by("title")
	mcategories = mCategories.objects.order_by("title")
	articles = Articles.objects.filter(home_hard=True).order_by("-created")[:5]	
	files = Files.objects.filter(hidden=False).order_by("-created")[:5]
	pages = Pages.objects.order_by("title")
	announcements = Announcements.objects.order_by("-created")[:5]
	demonstrations = Demonstrations.objects.filter(publication=True).order_by("-created")[:5]
	textlink = TextLink.objects.filter(publication=True)
	banner	= Banner.objects.filter(publication=True)
	
	site = Site.objects.get_current()	
	return render_to_response('page.html', locals())
		

def ifile(request, slug):
	files = Files.objects.filter(hidden=False).order_by("-created")
	articles = Articles.objects.filter(home_hard=True).order_by("-created")[:5]
	categories = Categories.objects.order_by("title")
	mcategories = mCategories.objects.order_by("title")
	pages = Pages.objects.order_by("title")
	announcements = Announcements.objects.order_by("-created")[:5]
	demonstrations = Demonstrations.objects.filter(publication=True).order_by("-created")[:5]
	textlink = TextLink.objects.filter(publication=True)
	banner	= Banner.objects.filter(publication=True)
	
	ifile = get_object_or_404(Files, slug=slug)
	
	site = Site.objects.get_current()	
	return render_to_response('file.html', locals())		
	
def files(request):

	files = Files.objects.filter(hidden=False).order_by("-created")
	articles = Articles.objects.filter(home_hard=True).order_by("-created")[:5]
	categories = Categories.objects.order_by("title")
	mcategories = mCategories.objects.order_by("title")
	pages = Pages.objects.order_by("title")
	announcements = Announcements.objects.order_by("-created")[:5]
	demonstrations = Demonstrations.objects.filter(publication=True).order_by("-created")[:5]
	textlink = TextLink.objects.filter(publication=True)
	banner	= Banner.objects.filter(publication=True)
	
	listarticle = Articles.objects.order_by("-created")[:5]
	
	site = Site.objects.get_current()	
	return render_to_response('files.html', locals())	

def announcement(request, slug):
	announcement = get_object_or_404(Announcements, slug=slug)
	categories = Categories.objects.order_by("title")
	mcategories = mCategories.objects.order_by("title")
	articles = Articles.objects.filter(home_hard=True).order_by("-created")[:5]
	files = Files.objects.filter(hidden=False).order_by("-created")[:5]
	pages = Pages.objects.order_by("title")
	announcements = Announcements.objects.order_by("-created")[:5]
	demonstrations = Demonstrations.objects.filter(publication=True).order_by("-created")[:5]
	textlink = TextLink.objects.filter(publication=True)
	banner	= Banner.objects.filter(publication=True)
	
	site = Site.objects.get_current()	
	return render_to_response('announcement.html', locals())	

def demonstration(request, slug):
	demonstration = get_object_or_404(Demonstrations, slug=slug)
	categories = Categories.objects.order_by("title")
	mcategories = mCategories.objects.order_by("title")
	articles = Articles.objects.filter(home_hard=True).order_by("-created")[:5]
	files = Files.objects.filter(gizli=False).order_by("-olusturulma")[:5]
	pages = Pages.objects.order_by("baslik")
	demonstrations = Demonstrations.objects.filter(publication=True).order_by("-created")[:5]
	announcements = Announcements.objects.order_by("-created")[:5]
	textlink = TextLink.objects.filter(publication=True)
	banner	= Banner.objects.filter(publication=True)
	
	site = Site.objects.get_current()	
	return render_to_response('demonstration.html', locals())		
