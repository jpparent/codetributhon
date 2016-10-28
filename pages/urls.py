from django.conf.urls import url, patterns
from pages import views
import django.contrib.auth.views

urlpatterns = [

    url(
        r'^$',
        views.Home.as_view(),
        name='home'
    ),

    url(
        r'^login/$',
        django.contrib.auth.views.login,
        name='login'
    ),

    url(
        r'^logout$',
        views.LogoutView.as_view(),
        name='logout'
    ),

    url(
        r'^contact/$',
        views.Contact.as_view(),
        name='contact'
    ),

    url(
        r'^calendar/$',
        views.Calendar.as_view(),
        name='calendar'
    ),

    url(
        r'^reward/$',
        views.Reward.as_view(),
        name='reward'
    ),

    url(
        r'^settlement/$',
        views.Settlement.as_view(),
        name='settlement'
    ),
]
