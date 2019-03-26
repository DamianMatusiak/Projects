from django.contrib import admin

from .models import Entry, Tag, UserProfile


admin.site.register([Entry, Tag, UserProfile])