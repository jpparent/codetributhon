# coding: utf-8

from django.views import generic
from faq.models import Faq
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy


class FaqList(generic.ListView):
    # List all FAQ
    template_name = 'faq/list.html'
    context_object_name = 'faqs'

    def get_queryset(self):
        list_faq = Faq.objects.filter(enabled=True).order_by('-create_date')

        return list_faq
