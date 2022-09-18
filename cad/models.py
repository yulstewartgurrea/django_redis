# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CadEstimates(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField()
    formatted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created',)
        
    def __str__(self):
        return self.name
