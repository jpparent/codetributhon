# coding: utf-8

from django.views import generic
from events.models import Events
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from datetime import date
import markdown
from lxml import etree
from django.conf import settings

class EventsList(generic.ListView):
    # List all event
    template_name = 'events/list.html'
    context_object_name = 'events'

    def dispatch(self, *args, **kwargs):
        return super(EventsList, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        today = date.today();
        eventsList = Events.objects.filter(enabled=True, dateEvent__gte=date.today() )\
            .order_by('-dateEvent', '-time').reverse()

        return eventsList

class EventDetail(generic.DetailView):
    # List all project
    model = Events
    template_name = 'events/detail.html'

    def dispatch(self, *args, **kwargs):
        project = get_object_or_404(
            Events,
            id=self.kwargs['pk']
        )
        return super(EventDetail, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EventDetail, self).get_context_data(**kwargs)

        tree = etree.parse(open(settings.STATIC_ROOT+"/API_KEYS.xml"))

        key_google_map = tree.xpath("/apis/api/key")[0]
        md = markdown.Markdown()
        context['content_html'] = md.convert(self.object.description)
        context['key_google_map'] = key_google_map.text

        return context