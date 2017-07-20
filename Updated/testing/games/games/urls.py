from django.conf.urls import patterns, include, url
from django.contrib import admin
import cards

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'games.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'cards.views.home', name='home'),
    url(r'^filter/adv/suit$', 'cards.views.suit_filter', name='new_filter'),
    url(r'^faq/$', 'cards.views.faq', name='faq', ),
    url(r'^profile/$', 'cards.views.profile', name='profile'),
    url(r'^blackjack/$', 'cards.views.blackjack', name='blackjack'),
    url(r'^poker/$', 'cards.views.poker', name='poker'),
    url(r'^register/$', 'cards.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^war/$', 'cards.views.war', name='war'),

)
