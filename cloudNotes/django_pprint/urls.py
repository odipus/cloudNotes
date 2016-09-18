from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_pprint.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^fileupload','the_pprint.views.fileUpload_page',name="fileupload_page"),
    url(r'^$','the_pprint.views.fileUpload_page',name="fileupload_page"),
    # url(r'^fileupload/fileupload$','the_pprint.views.fileUpload',name="fileupload"),
    url(r'^disk/', 'the_pprint.views.register'),

)
