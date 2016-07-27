"""crmapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin

from crmapp.marketing.views import HomePage
from crmapp.accounts.views import AccountList
from crmapp.accounts.urls import account_urls
from crmapp.contacts.urls import contact_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$',
        'crmapp.subscribers.views.subscriber_new',
        name='sub_new'),

    url(r'^login/$',
        'django.contrib.auth.views.login', {'template_name': 'login.html'}),

    url(r'^logout/$',
        'django.contrib.auth.views.logout', {'next_page': '/login/'}),
    
    url(r'^account/new/$',
        'crmapp.accounts.views.account_cru', name='account_new'),
    
    url(r'^account/list/$',
        AccountList.as_view(), name='account_list'),

    url(r'^account/(?P<uuid>[\w-]+)/', include(account_urls)),

    # Contact related URLs
    url(r'^contact/(?P<uuid>[\w-]+)/', include(contact_urls)),

    url(r'^$', HomePage.as_view(), name="home"),
]
