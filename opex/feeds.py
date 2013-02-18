from django.contrib.syndication.views import Feed
from django.conf.urls.defaults import patterns, url

from django.shortcuts import get_object_or_404

from blog.models import Blogs
from article.models import Articles
from file.models import Files
from announcement.models import Announcements


class LastArticles(Feed):
    
    title = "Jesterxu.Com - Last Articles"
    link = "/"
    description = "Opex programming for welocalize"


    def items(self):
        return Articles.objects.order_by("-created").filter(home_hard=True)[:5]


    def item_title(self, item):
        return item.chef_title


    def item_description(self, item):
        return item.description_chef

    
    def item_pubdate(self, item):
        return item.created


class LastBlogs(Feed):
    
    title = "welocalize.Com - Last Blog"
    link = "/"
    description = "Opex programming for welocalize"


    def items(self):
        return Blogs.objects.order_by("-created").filter(home_hard=True)[:5]


    def item_title(self, item):
        return item.chef_title


    def item_description(self, item):
        return item.description_chef

    
    def item_pubdate(self, item):
        return item.created

class LastAnnouncements(Feed):
    
    title = "Welocalize.Com - Last Announcements"
    link = "/"
    description = "Opex programming for welocalize"


    def items(self):
        return Announcements.objects.order_by("-created")[:5]


    def item_title(self, item):
        return item.chef_title


    def item_description(self, item):
        return item.description_chef

    
    def item_pubdate(self, item):
        return item.created
class LastFiles(Feed):
    
    baslik = "welocalize.Com - Last Files"
    link = "/"
    description = "Opex programming for welocalize"


    def items(self):
        return Files.objects.order_by("-created").filter(hidden=False)[:5]


    def item_title(self, item):
        return item.chef_title 


    def item_description(self, item):
        return item.description_chef

    
    def item_pubdate(self, item):
        return item.created 

RSS_URLS = patterns('',
                    url(r'^rss/$', LastBlogs()),
                    url(r'^rss/articles/$', LastArticles()),
                    url(r'^rss/blogs/$', LastBlogs()),
                    url(r'^rss/announcements/$', LastAnnouncements()),
		    url(r'^rss/files/$', LastFiles()),
)
