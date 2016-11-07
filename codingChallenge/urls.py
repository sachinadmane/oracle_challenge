"""codingChallenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from log.forms import LoginForm
from oracle.views import add
from recipe.views import view,delete,edit,update

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'', include('log.urls')),
    url(r'^login/?$', auth_views.login, {'template_name': 'login.html', 'authentication_form': LoginForm},name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}),
    url(r'^oracle/add.html$',add, name='add'),
    url(r'^recipe/view$',view, name='view'),
    url(r'^recipe/edit$', edit, name='edit'),
    url(r'^recipe/update$',update),
    url(r'^recipe/delete$', delete)

]
