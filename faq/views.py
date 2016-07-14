# coding: utf-8

from django.views import generic
from faq.models import Faq
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy


class FaqList(generic.ListView):
    # List all project
    template_name = 'faq/list.html'
    context_object_name = 'faq'
    model = Faq
    ordering = "-create_date"
