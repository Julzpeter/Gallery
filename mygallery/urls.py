from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name='welcome'),
    # url(r'^category/(\w+)', views.get_category, name='get_category'),
    # url(r'^location/(\w+)', views.get_location, name='get_location'),

 ]
