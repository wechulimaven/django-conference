from django.conf.urls import *
from django.conf import settings
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^admin_docs/', include('django.contrib.admindocs.urls')),
    (r'^conference/', include('django_conference.urls')),
    (r'^accounts/login/', 'django.contrib.auth.views.login', {
        'template_name': 'admin/login.html'
    }),
)

#allow static serve only for development work 
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True}),
    )
