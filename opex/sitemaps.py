from blog.models import Blogs, Categories
from article.models import Articles, mCategories
from pages.models import Pages
from ifile.models import Files
from announcement.models import Announcements
from advertising.models import Demonstrations

from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.conf.urls.defaults import patterns, url

blogs_dict = {
    'queryset': Blogs.objects.order_by("-created").filter(home_hard=True),
    'date_field': 'created',
}
categories_dict = {
    'queryset': Categories.objects.all(),
}
articles_dict = {
    'queryset': Articles.objects.order_by("-created").filter(home_hard=True),
    'date_field': 'created',
}
mcategories_dict = {
    'queryset': mCategories.objects.all(),
}
pages_dict = {
    'queryset': Pages.objects.all(),
    'date_field': 'created',
}
files_dict = {
              'queryset': Files.objects.filter(hidden=False).order_by("-created"),
              'date_field': 'created',
}
announcements_dict = {
              'queryset': Announcements.objects.all(),
              'date_field': 'created',
}
demonstrations_dict = {
              'queryset': Demonstrations.objects.filter(publication=True).all(),
              'date_field': 'created',

}
sitemaps = {
    'blogs': GenericSitemap(blogs_dict, priority=0.5),
    'categories': GenericSitemap(categories_dict, priority=1),
	'articles': GenericSitemap(articles_dict, priority=0.5),
	'article-catgories': GenericSitemap(mcategories_dict, priority=1),
    'pages': GenericSitemap(pages_dict, priority=0.5),
	'files': GenericSitemap(files_dict, priority=0.5),
    'announcements': GenericSitemap(announcements_dict, priority=0.5),
	'demonstrations': GenericSitemap(demonstrations_dict, priority=0.5),
}


SITEMAPS_URLS = patterns('django.contrib.sitemaps.views',
    url(r'^sitemap\.xml$', 'index', {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap', {'sitemaps': sitemaps}),
)
