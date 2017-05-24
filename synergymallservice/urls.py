# Author:max
from django.conf.urls import url
from synergymallservice import models,views


urlpatterns = [
    url(r'^info/', views.get_saleInfo),
]