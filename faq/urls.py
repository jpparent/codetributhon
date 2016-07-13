from django.conf.urls import patterns, url
from faq import views

urlpatterns = patterns(
    '',
    url(
        r'^list/$',
        views.FaqList,
        name='faq_list'
    ),

)