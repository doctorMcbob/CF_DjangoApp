from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', 'usradmin.views.home', name='home'),
    url(r'edit/(\d+)', 'usradmin.views.edit', name='edit'),
    url(r'edit_user/', 'usradmin.forms.edit_user', name='edit_user'),
    url(r'delete_user/', 'usradmin.forms.delete_user', name='delete_user'),
    url(r'new/', 'usradmin.forms.create_user', name='new_user'),
    url(r'^admin/', include(admin.site.urls)),
    
)


