from django.db import models
from codetributhon.behaviors import Timestampable


class Category(Timestampable, models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    list_faq = []

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
            blank=False,
            null=False
    )

    enabled = models.BooleanField(
        verbose_name='Activer',
        null=False,
        blank=False,
        default=False,

    )

    category = models.ForeignKey(
            Category,
            verbose_name='Categories',
            related_name='FAQ',
            on_delete=models.CASCADE
    )

    def __str__(self):
        return self.question
