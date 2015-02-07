from django.conf.urls import patterns, url
from profiles.views import show, edit, login

urlpatterns = patterns('',
url(r'^show.html$', show),
url(r'^edit.html$', edit),
#url(r'^edit/$', ProfileEdit.as_view()), # а по URL http://имя_сайта/blog/число/ 
                                              # будет выводиться пост с определенным номером
)