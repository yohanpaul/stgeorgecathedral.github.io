# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.apps import apps
for model in apps.get_app_config('youth').models.values():
    admin.site.register(model)
