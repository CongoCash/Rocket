from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'cards.views.home', name='home'),
    url(r'^filters/$', 'cards.views.filters', name='filters'),
    url(r'^tags/$', 'cards.views.template_tags', name='tags'),
    url(r'^first/filter/$', 'cards.views.first_filter', name='tags'),
    url(r'^suit/filter/$', 'cards.views.suit_filter', name='suits'),
    url(r'^profile/$', 'cards.views.profile', name='profile'),
    url(r'^faq/$', 'cards.views.faq', name='faq'),
    url(r'^blackjack/$', 'cards.views.blackjack', name='blackjack'),
    url(r'^poker/$', 'cards.views.poker', name='poker'),
    url(r'^war/$', 'cards.views.war', name='war'),


    url(r'^register/$', 'cards.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),

    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
)