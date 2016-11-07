from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^(?P<recipe_id>\d+)/$', views.edit, name='edit')
]