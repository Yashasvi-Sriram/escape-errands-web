from django.conf.urls import url
from . import views

app_name = 'restapi'

urlpatterns = [
    # host/rest/goal/read/regex/?search=PATTERN
    url(r'^goal/read/regex/$', views.read_regex, name='goal_read_regex'),
    # host/rest/goal/read/family/pk
    url(r'^goal/read/family/(?P<pk>[1-9][0-9]*)/$', views.read_family, name='goal_read_family'),

    # host/rest/goal/toggle/is_achieved/pk
    url(r'^goal/toggle/is_achieved/(?P<pk>[1-9][0-9]*)/$', views.toggle_is_achieved, name='goal_toggle_is_achieved'),
]