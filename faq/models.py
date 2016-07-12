from django.db import models
from codetributhon.behaviors import Timestampable


class Category(Timestampable, models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    label = models.CharField(
            verbose_name='Label',
            max_length=255
    )

    def __str__(self):
        return self.label

class Faq(Timestampable, models.Model):
    class Meta:
        verbose_name_plural = 'FAQ'

    question = models.CharField(
            verbose_name='Question',
            max_length=255,
            blank=False,
            null=False
    )

    response = models.TextField(
            verbose_name='Reponse',
            max_length=255,
            blank=False,
            null=False
    )
    category = models.ForeignKey(
            Category,
            verbose_name='Categories',
            related_name='FAQ'
    )

    def __unicode__(self):
        return self.question
