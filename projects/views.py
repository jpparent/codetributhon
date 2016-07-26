# coding: utf-8

from django.views import generic
from projects.models import Project, Contribution
from django.shortcuts import render, redirect, get_object_or_404
from projects.forms import ContributionForm
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
import markdown
from django.db import connection


class ProjectList(generic.ListView):
    # List all project
    template_name = 'projects/list.html'
    context_object_name = 'projects'

    def dispatch(self, *args, **kwargs):
        return super(ProjectList, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        # cursor = connection.cursor()

        list_project_tmp = Project.objects.filter(organization__enabled=True, enabled=True).order_by('-create_date')
        list_project = []

        for project in list_project_tmp:
            project.nb_contrib =  Contribution.objects.filter(project_id = project.id).count()
            list_project.append(project)

        # meilleur methode.
        # probleme lors de la receptiondes donnees dans le template
        '''cursor.execute("SELECT "
                           "pp.id as prj_id, pp.name, pp.description, pp.logo, po.name as org_name, po.id as org_id, po.url, "
                           "(SELECT count(pc.id) FROM projects_contribution pc "
                           "WHERE pc.project_id == pp.id AND pc.enabled == 1) AS nb_contrib "
                           "FROM projects_project pp "
                           "INNER JOIN projects_organization po ON po.id = pp.id "
                           "WHERE po.enabled == 1 AND pp.enabled == 1")

        list_project = cursor.fetchall()'''

        return  list_project


class ProjectDetail(generic.DetailView):
    # List all project
    model = Project
    template_name = 'projects/detail.html'

    def dispatch(self, *args, **kwargs):
        project = get_object_or_404(
            Project,
            id=self.kwargs['pk']
        )
        return super(ProjectDetail, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProjectDetail, self).get_context_data(**kwargs)
        md = markdown.Markdown()
        context['content_html'] = md.convert(self.object.description)
        return context


class ContributionCreate(generic.CreateView):
    model = Contribution
    template_name = 'contributions/create.html'
    form_class = ContributionForm

    def dispatch(self, *args, **kwargs):
        return super(ContributionCreate, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        messages.add_message(
                self.request,
                messages.SUCCESS,
                'Votre ontribution a bien été envoyée'
        )

        return reverse_lazy('projects:contribution_create')
