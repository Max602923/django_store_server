from django.shortcuts import render,HttpResponse
from django.core import serializers
from synergymallservice import models

# Create your views here.



def get_saleInfo(request):
    # sale_infos = models.CusSaleInfoAll.objects.filter(shop_id__contains=100000006)

    shops = models.CusShop.objects.all()[:100]


    sale_data = serializers.serialize('json',shops)


    return HttpResponse(sale_data)
