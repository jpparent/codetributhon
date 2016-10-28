from django.conf.urls import patterns, url
from events import views

urlpatterns = [
    url(
        r'^list/$',
        views.EventsList.as_view(),
        name='events_list'
    ),
    url(
        r'^detail/(?P<pk>\d+)$',
        views.EventDetail.as_view(),
        name='event_detail'
    ),
]
