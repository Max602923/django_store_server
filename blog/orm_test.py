# Author:max

import os
# import sys
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'untitled_django.settings'
import django
django.setup()

from blog import models

entry = models.Entry.objects.get(pk=1)


tech_blog = models.Blog.objects.get(name = '科技')

entry.blog = tech_blog

entry.save()

print(entry,tech_blog)