# coding: utf-8
from django.views import generic
from django.db.models import Q
from faq.models import Category, Faq
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy


class FaqList(generic.ListView):
    # List all FAQ
    template_name = 'faq/list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        # list_faq = Faq.objects.filter(enabled=True).order_by('-create_date')
        categories = Category.objects.order_by('-create_date')

        for cat in categories:
            cat.list_faq = Faq.objects.filter(Q(enabled=True) & Q(category = cat.id) ).order_by('-create_date')

        return categories
