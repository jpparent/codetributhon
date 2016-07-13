from django.conf.urls import patterns, url
from faq import views

urlpatterns = patterns(
    '',
    url(
        r'^list/$',
        views.FaqList.as_view(),
        name='faq_list'
    ),
)