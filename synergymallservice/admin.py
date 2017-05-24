from django.contrib import admin
from synergymallservice import models

class ShopAdmin(admin.ModelAdmin):
    list_display = ('shop_id','shop_name','shop_addr','salesman_name','boss_name','boss_tel_no','status')
    search_fields = ('shop_id','shop_name','salesman_name','boss_name','boss_tel_no')
    list_per_page = 20



class SaleInfoAdmin(admin.ModelAdmin):
    list_display = ('shop_id','sale_time','count','barcode_id','qty','amount')
    search_fields = ('shop_id','sale_time','barcode_id')
    list_per_page = 30


class PrdGoodsAdmin(admin.ModelAdmin):
    list_display = ('goods_id', 'goods_barcode', 'goods_name', 'brand_name', 'unit_bas_name', 'unit_pkg_name','sale_price')
    search_fields = ('goods_id','goods_barcode','goods_name')
    list_per_page = 25

# Register your models here.
# admin.site.register(models.CusSaleInfoAll,SaleInfoAdmin)
admin.site.register(models.CusShop,ShopAdmin)

admin.site.register(models.PrdGoods,PrdGoodsAdmin)