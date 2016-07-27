from django.conf.urls import patterns, ulr

contact_urls = patterns('',
    url(r'^$', 'crmapp.contacts.views.contact_detail', name='contact_detail'),
)