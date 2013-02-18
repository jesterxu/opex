from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from opex.feeds import RSS_URLS
from opex.sitemaps import SITEMAPS_URLS
from opex.settings import DIZIN

admin.autodiscover()

urlpatterns = patterns('',
    	# Examples:
    	url(r'^$', 'blog.views.home', name='home'),
	
    	url(r'^fillrelease/success', 'automation.views.upload_success', name='upload success'), 
    	url(r'^fillrelease/$', 'automation.views.upload_file', name='fill release'),
	url(r'^seleniumlog/$', 'automation.views.seleniumlog', name='selenium logs'),	
	url(r'^automation/$', 'automation.views.seleniums', name='seleniums'),	
	url(r'^seleniumlog/(?P<slug>.*)$', 'automation.views.iselenium2', name='iselenium2'),
	url(r'^blog/$', 'blog.views.blog', name='blog'),
	url(r'^(?P<slug>.*).html$', 'blog.views.post', name='post'),
	url(r'^blog/label/(?P<tag_name>.*)/$', 'blog.views.label', name='label'),
	url(r'^blog/category/(?P<slug>.*)/$', 'blog.views.category', name='category'),

	url(r'^articles/$', 'blog.views.articles', name='articles'),
	url(r'^article/(?P<kat_slug>.*)/(?P<slug>.*)/$', 'blog.views.article', name='article'),
	url(r'^article/(?P<kat_slug>.*)/$', 'blog.views.mcategory', name='mcategories'),		
	url(r'^articles/(?P<tag_name>.*)/$', 'blog.views.mlabel', name='mlabel'),
	
	url(r'^page/(?P<slug>.*)/$', 'blog.views.pages', name='pages'),
	
	url(r'^files/$', 'blog.views.files', name='files'),
        url(r'^file/(?P<slug>.*)/(?P<file_source1>.*)/(?P<file_source>.*)/$','file.views.download2', name='download files2'),
	url(r'^files/(?P<file_source>.*)/$','file.views.download', name='download files'),
 
	url(r'^file/(?P<slug>.*)/$', 'blog.views.ifile', name='file'),
	
	url(r'^link/$', 'link.views.linkolustur'),
        url(r'^link/(?P<id>\w+)/$', 'link.views.link'),
        url(r'^link/(?P<id>\w+)/stats$', 'link.views.stats'),
	
	url(r'^announcement/(?P<slug>.*)/$', 'blog.views.announcement', name='announcement'),
	
	url(r'^demonstration/(?P<slug>.*)/$', 'blog.views.demonstration', name='description'),
	
	#url(r'^iletisim/', include('django_contactme.urls')),

    	# url(r'^hdblog/', include('hdblog.foo.urls')),
    	url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += SITEMAPS_URLS 
urlpatterns += RSS_URLS

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': DIZIN + 'media/' }),
		(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': DIZIN + 'static/' }),
    )
