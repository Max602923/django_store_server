# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class BasBasItem(models.Model):
    bi_id = models.CharField(primary_key=True, max_length=5)
    bi_value = models.CharField(max_length=10)
    bi_cate = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'bas$bas_item'
        unique_together = (('bi_id', 'bi_cate'),)


class CusDepot(models.Model):
    id = models.BigAutoField(primary_key=True)
    depot_name = models.CharField(max_length=48, blank=True, null=True)
    depot_user_name = models.CharField(max_length=255, blank=True, null=True)
    depot_user_pwd = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cus$depot'


class CusDistrict(models.Model):
    district_name = models.CharField(max_length=24, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cus$district'


class CusFeedback(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.CharField(max_length=200)
    shop_id = models.CharField(max_length=10)
    createon = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cus$feedback'


class CusForecastOrder(models.Model):
    forecast_id = models.BigAutoField(primary_key=True)
    shop_id = models.CharField(max_length=10, blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    createon = models.DateTimeField(blank=True, null=True)
    createby = models.CharField(max_length=15, blank=True, null=True)
    modifyon = models.DateTimeField(blank=True, null=True)
    modifyby = models.CharField(max_length=15, blank=True, null=True)
    order_weekday = models.SmallIntegerField(blank=True, null=True)
    is_item_by_tmpl = models.CharField(max_length=1, blank=True, null=True)
    is_deleted = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cus$forecast_order'


class CusForecastOrder1115(models.Model):
    forecast_id = models.BigAutoField(primary_key=True)
    shop_id = models.BigIntegerField(blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    createon = models.DateTimeField(blank=True, null=True)
    createby = models.CharField(max_length=15, blank=True, null=True)
    modifyon = models.DateTimeField(blank=True, null=True)
    modifyby = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cus$forecast_order_1115'


class CusForecastOrderItem(models.Model):
    item_id = models.BigAutoField(primary_key=True)
    forecast_id = models.CharField(max_length=10)
    goods_id = models.CharField(max_length=16, blank=True, null=True)
    goods_name = models.CharField(max_length=40, blank=True, null=True)
    sales_unit = models.CharField(max_length=3, blank=True, null=True)
    sales_quantity = models.DecimalField(max_digits=13, decimal_places=0, blank=True, null=True)
    sales_price = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=5, blank=True, null=True)
    forecast_item_type = models.SmallIntegerField()
    goods_type_no = models.CharField(max_length=10, blank=True, null=True)
    goods_type_name = models.CharField(max_length=24, blank=True, null=True)
    sales_in_week_pkg_qty = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_in_period_bas_qty = models.DecimalField(max_digits=13, decimal_places=6, blank=True, null=True)
    sales_in_week_bas_qty = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_price_bas = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_price_pkg = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    goods_level = models.CharField(max_length=1, blank=True, null=True)
    sales_unit_bas = models.CharField(max_length=50, blank=True, null=True)
    sales_unit_pkg = models.CharField(max_length=50, blank=True, null=True)
    stock_qty = models.DecimalField(max_digits=13, decimal_places=0, blank=True, null=True)
    goods_type_parent_no = models.CharField(max_length=10, blank=True, null=True)
    goods_type_parent_name = models.CharField(max_length=24, blank=True, null=True)
    sales_unit_code = models.CharField(max_length=5, blank=True, null=True)
    sales_price_max = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_price_min = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_price_avg = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_vol = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    discount_rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cus$forecast_order_item'


class CusForecastOrderItem1115(models.Model):
    item_id = models.BigAutoField(primary_key=True)
    forecast_id = models.BigIntegerField()
    goods_id = models.CharField(max_length=16, blank=True, null=True)
    goods_name = models.CharField(max_length=40, blank=True, null=True)
    goods_type_no = models.CharField(max_length=10, blank=True, null=True)
    goods_type_name = models.CharField(max_length=24, blank=True, null=True)
    goods_type_parent_no = models.CharField(max_length=10, blank=True, null=True)
    goods_type_parent_name = models.CharField(max_length=24, blank=True, null=True)
    sales_unit = models.CharField(max_length=3, blank=True, null=True)
    sales_quantity = models.DecimalField(max_digits=13, decimal_places=0, blank=True, null=True)
    sales_price = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=5, blank=True, null=True)
    goods_specs = models.CharField(max_length=24, blank=True, null=True)
    sales_unit_code = models.CharField(max_length=10, blank=True, null=True)
    ispromotion = models.SmallIntegerField(blank=True, null=True)
    sales_price_std = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    order_no = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cus$forecast_order_item_1115'


class CusForecastOrderItemLog(models.Model):
    log_id = models.BigAutoField(primary_key=True)
    total_log_id = models.BigIntegerField()
    shop_id = models.BigIntegerField()
    item_id = models.BigIntegerField()
    forecast_id = models.BigIntegerField()
    goods_id = models.CharField(max_length=16, blank=True, null=True)
    goods_name = models.CharField(max_length=40, blank=True, null=True)
    sales_unit = models.CharField(max_length=3, blank=True, null=True)
    sales_quantity = models.DecimalField(max_digits=13, decimal_places=0, blank=True, null=True)
    sales_price = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    goods_weekday = models.SmallIntegerField(blank=True, null=True)
    log_datetime = models.DateTimeField(blank=True, null=True)
    stock_qty = models.DecimalField(max_digits=13, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cus$forecast_order_item_log'


class CusForecastOrderItemTmpl(models.Model):
    item_id = models.BigAutoField(primary_key=True)
    forecast_id = models.CharField(max_length=10)
    goods_id = models.CharField(max_length=16, blank=True, null=True)
    goods_name = models.CharField(max_length=40, blank=True, null=True)
    sales_unit = models.CharField(max_length=3, blank=True, null=True)
    sales_quantity = models.DecimalField(max_digits=13, decimal_places=0, blank=True, null=True)
    sales_price = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=5, blank=True, null=True)
    goods_type_no = models.CharField(max_length=10, blank=True, null=True)
    goods_type_name = models.CharField(max_length=24, blank=True, null=True)
    sales_in_week_pkg_qty = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_in_period_bas_qty = models.DecimalField(max_digits=13, decimal_places=6, blank=True, null=True)
    sales_in_week_bas_qty = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_price_bas = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_price_pkg = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    goods_level = models.CharField(max_length=1, blank=True, null=True)
    sales_unit_bas = models.CharField(max_length=50, blank=True, null=True)
    sales_unit_pkg = models.CharField(max_length=50, blank=True, null=True)
    goods_type_parent_no = models.CharField(max_length=10, blank=True, null=True)
    goods_type_parent_name = models.CharField(max_length=24, blank=True, null=True)
    sales_unit_code = models.CharField(max_length=5, blank=True, null=True)
    sales_price_max = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_price_min = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_price_avg = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_vol = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    forecast_item_type = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cus$forecast_order_item_tmpl'


class CusForecastOrderSourceTotal(models.Model):
    total_log_id = models.BigAutoField(primary_key=True)
    shop_id = models.BigIntegerField()
    source_type = models.SmallIntegerField()
    source_datetime_from = models.DateTimeField(blank=True, null=True)
    source_datetime_to = models.DateTimeField(blank=True, null=True)
    source_sku_type_qty = models.DecimalField(max_digits=13, decimal_places=0, blank=True, null=True)
    source_sku_unit_qty = models.DecimalField(max_digits=13, decimal_places=0, blank=True, null=True)
    source_sku_amt = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    source_sku_barcode_ok_type_qty = models.DecimalField(max_digits=13, decimal_places=0, blank=True, null=True)
    source_sku_idc_type_qty = models.DecimalField(max_digits=13, decimal_places=0, blank=True, null=True)
    source_sku_idc_unit_qty = models.DecimalField(max_digits=13, decimal_places=0, blank=True, null=True)
    source_sku_idc_amt = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    lev1qty = models.DecimalField(max_digits=13, decimal_places=0, blank=True, null=True)
    lev2qty = models.DecimalField(max_digits=13, decimal_places=0, blank=True, null=True)
    lev3qty = models.DecimalField(max_digits=13, decimal_places=0, blank=True, null=True)
    lev4qty = models.DecimalField(max_digits=13, decimal_places=0, blank=True, null=True)
    lev5qty = models.DecimalField(max_digits=13, decimal_places=0, blank=True, null=True)
    create_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cus$forecast_order_source_total'


class CusGoodsType(models.Model):
    shop_id = models.CharField(primary_key=True, max_length=10)
    goods_type_id = models.SmallIntegerField()
    goods_type_name = models.CharField(max_length=24)
    goods_type_parentid = models.SmallIntegerField()
    levelid = models.IntegerField(db_column='LevelId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cus$goods_type'
        unique_together = (('shop_id', 'goods_type_id'),)


class CusSaleInfoAll(models.Model):
    shop_id = models.CharField(max_length=30, blank=True, null=True)
    sale_time = models.CharField(max_length=30, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    barcode_id = models.CharField(max_length=96, blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cus$sale_info_all'


class CusSaleRecord100000006(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_100000006'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101010009(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101010009'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101010050(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101010050'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101010080(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101010080'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101010082(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101010082'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101010146(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101010146'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101010156(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101010156'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101010181(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101010181'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101010260(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101010260'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101010313(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101010313'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101010374(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101010374'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101011336(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101011336'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101020044(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101020044'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101020084(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101020084'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101020121(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101020121'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101020129(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101020129'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101020139(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101020139'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101020140(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101020140'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101020150(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101020150'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101020264(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101020264'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101020265(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101020265'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101020289(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101020289'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101020339(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101020339'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101020345(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101020345'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101020398(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101020398'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101020768(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101020768'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101020921(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101020921'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101021234(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101021234'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101021358(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101021358'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101030076(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101030076'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101030083(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101030083'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101030085(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101030085'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101030086(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101030086'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101030155(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101030155'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101030178(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101030178'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101030191(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101030191'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101030243(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101030243'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101030312(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101030312'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101030346(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101030346'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101030506(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101030506'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101030581(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101030581'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101030582(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101030582'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101030584(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101030584'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101030585(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101030585'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101030586(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101030586'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101030588(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101030588'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101030590(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101030590'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101030591(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101030591'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101030592(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101030592'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101030599(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101030599'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101030805(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101030805'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101030813(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101030813'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101030930(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101030930'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101031283(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101031283'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050017(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050017'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050019(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050019'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050023(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050023'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050024(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050024'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050031(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050031'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050046(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050046'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050047(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050047'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050048(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050048'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050051(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050051'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050053(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050053'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050056(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050056'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050057(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050057'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050058(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050058'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050059(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050059'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050060(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050060'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050061(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050061'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050074(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050074'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050077(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050077'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050088(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050088'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050103(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050103'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050105(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050105'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050106(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050106'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050113(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050113'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050114(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050114'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050117(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050117'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050118(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050118'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050119(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050119'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050120(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050120'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050123(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050123'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050130(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050130'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050131(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050131'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050133(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050133'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050135(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050135'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050138(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050138'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050141(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050141'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050142(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050142'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050143(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050143'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050149(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050149'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050151(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050151'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050160(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050160'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050163(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050163'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050164(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050164'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050165(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050165'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050166(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050166'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050167(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050167'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050168(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050168'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050186(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050186'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050187(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050187'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050198(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050198'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050204(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050204'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050207(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050207'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050216(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050216'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050219(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050219'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050220(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050220'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050240(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050240'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050245(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050245'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050246(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050246'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050248(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050248'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050249(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050249'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050250(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050250'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050256(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050256'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050259(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050259'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050261(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050261'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050262(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050262'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050268(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050268'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050271(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050271'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050272(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050272'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050273(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050273'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050274(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050274'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050284(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050284'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050286(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050286'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050288(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050288'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050293(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050293'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050300(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050300'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050311(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050311'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050322(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050322'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050343(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050343'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050348(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050348'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050359(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050359'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050391(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050391'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050404(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050404'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050414(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050414'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050424(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050424'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050434(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050434'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050441(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050441'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050466(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050466'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050485(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050485'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050488(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050488'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050494(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050494'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050496(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050496'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050505(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050505'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050507(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050507'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050513(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050513'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050516(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050516'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050518(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050518'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050533(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050533'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050627(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050627'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050639(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050639'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050722(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050722'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050723(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050723'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050724(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050724'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050725(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050725'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050734(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050734'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050736(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050736'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050771(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050771'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050775(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050775'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050777(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050777'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050798(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050798'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050815(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050815'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050842(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050842'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050843(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050843'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050844(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050844'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050845(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050845'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050848(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050848'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050854(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050854'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050876(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050876'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050997(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050997'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101050998(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101050998'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101051000(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101051000'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101051006(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101051006'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101051011(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101051011'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101051054(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101051054'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101051074(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101051074'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101051086(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101051086'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101051091(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101051091'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101051092(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101051092'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101051095(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101051095'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101051162(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101051162'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101051164(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101051164'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101051183(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101051183'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101051231(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101051231'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060005(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060005'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060012(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060012'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060021(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060021'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060028(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060028'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060029(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060029'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060032(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060032'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060036(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060036'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060037(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060037'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060063(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060063'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060065(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060065'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060071(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060071'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060073(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060073'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060075(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060075'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060078(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060078'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060090(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060090'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060091(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060091'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060094(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060094'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060095(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060095'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060096(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060096'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060102(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060102'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060109(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060109'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060157(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060157'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060169(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060169'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060170(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060170'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060173(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060173'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060174(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060174'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060195(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060195'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060197(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060197'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060200(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060200'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060201(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060201'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060208(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060208'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060210(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060210'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060212(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060212'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060213(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060213'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060215(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060215'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060222(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060222'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060227(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060227'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060231(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060231'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060234(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060234'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060235(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060235'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060237(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060237'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060238(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060238'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060266(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060266'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060295(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060295'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060301(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060301'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060304(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060304'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060305(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060305'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060307(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060307'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060308(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060308'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060315(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060315'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060320(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060320'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060324(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060324'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060325(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060325'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060326(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060326'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060327(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060327'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060334(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060334'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060336(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060336'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060338(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060338'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060342(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060342'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060344(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060344'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060347(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060347'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060349(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060349'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060350(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060350'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060355(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060355'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060360(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060360'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060367(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060367'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060369(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060369'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060373(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060373'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060376(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060376'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060378(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060378'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060382(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060382'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060384(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060384'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060389(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060389'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060397(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060397'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060401(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060401'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060405(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060405'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060415(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060415'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060417(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060417'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060419(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060419'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060431(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060431'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060432(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060432'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060437(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060437'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060438(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060438'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060458(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060458'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060461(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060461'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060467(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060467'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060469(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060469'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060475(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060475'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060476(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060476'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060480(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060480'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060481(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060481'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060519(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060519'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060525(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060525'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060648(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060648'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060649(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060649'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060653(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060653'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060656(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060656'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060659(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060659'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060738(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060738'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060741(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060741'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060742(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060742'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060743(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060743'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060750(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060750'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060752(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060752'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060783(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060783'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060785(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060785'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060786(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060786'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060788(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060788'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060791(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060791'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060793(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060793'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060794(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060794'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060817(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060817'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060822(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060822'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060824(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060824'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060828(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060828'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060830(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060830'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060831(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060831'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060833(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060833'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060836(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060836'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060858(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060858'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060860(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060860'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060863(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060863'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060869(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060869'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060891(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060891'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060892(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060892'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060898(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060898'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060900(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060900'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060922(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060922'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060956(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060956'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101060959(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101060959'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101061061(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101061061'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101061063(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101061063'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101061068(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101061068'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101061069(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101061069'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101061079(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101061079'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101061081(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101061081'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101061107(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101061107'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101061188(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101061188'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101061267(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101061267'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101061343(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101061343'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101061344(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101061344'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101061345(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101061345'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070001(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070001'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070003(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070003'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070007(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070007'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070013(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070013'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070022(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070022'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070027(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070027'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070038(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070038'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070039(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070039'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070041(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070041'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070042(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070042'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070049(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070049'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070064(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070064'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070068(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070068'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070069(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070069'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070070(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070070'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070099(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070099'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070110(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070110'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070112(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070112'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070134(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070134'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070145(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070145'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070175(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070175'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070176(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070176'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070184(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070184'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070185(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070185'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070189(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070189'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070190(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070190'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070194(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070194'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070196(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070196'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070209(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070209'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070242(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070242'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070244(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070244'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070280(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070280'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070294(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070294'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070319(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070319'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070362(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070362'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070426(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070426'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070427(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070427'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070436(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070436'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070442(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070442'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070456(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070456'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070471(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070471'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070478(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070478'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070479(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070479'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070665(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070665'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070671(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070671'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070680(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070680'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070746(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070746'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070754(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070754'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070760(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070760'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070764(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070764'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070766(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070766'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070790(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070790'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070796(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070796'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070862(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070862'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070868(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070868'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070889(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070889'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070894(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070894'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070896(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070896'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070941(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070941'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070965(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070965'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070968(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070968'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101070970(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101070970'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101080033(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101080033'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101080054(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101080054'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101080055(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101080055'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101080097(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101080097'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101080154(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101080154'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101080177(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101080177'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101080188(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101080188'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101080228(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101080228'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101080229(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101080229'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101080364(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101080364'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101080365(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101080365'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101080407(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101080407'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101080451(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101080451'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101080452(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101080452'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101080482(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101080482'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord1010888888(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_1010888888'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord101090701(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_101090701'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord119(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_119'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000011(models.Model):
    sale_id = models.CharField(max_length=20)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000011'


class CusSaleRecord9800000017(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000017'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000045(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000045'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000047(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000047'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000053(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000053'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000054(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000054'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000068(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000068'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000098(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000098'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000100(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000100'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000103(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000103'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000112(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000112'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000113(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000113'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000117(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000117'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000120(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000120'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000124(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000124'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000126(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000126'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000131(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000131'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000146(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000146'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000149(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000149'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000150(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000150'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000160(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000160'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000168(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000168'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000170(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000170'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000171(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000171'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000181(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000181'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000182(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000182'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000188(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000188'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000191(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000191'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000193(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000193'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000203(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000203'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000223(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000223'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000226(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000226'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000234(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000234'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000245(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000245'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000250(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000250'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000322(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000322'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000344(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000344'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000453(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000453'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000550(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000550'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800000570(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800000570'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800001028(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800001028'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800001046(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800001046'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800001082(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800001082'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800001250(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800001250'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800001540(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800001540'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800001558(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800001558'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800001695(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800001695'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800001777(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800001777'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800001904(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800001904'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800001908(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800001908'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800001994(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800001994'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800002285(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800002285'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800002588(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800002588'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800002780(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800002780'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800003335(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800003335'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800003424(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800003424'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800003507(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800003507'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord9800005024(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_9800005024'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecord999999999(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_999999999'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusSaleRecordStock(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cus$sale_record_stock'
        unique_together = (('sale_id', 'record_no', 'barcode_id', 'sale_time'),)


class CusShop(models.Model):
    shop_id = models.CharField(primary_key=True, max_length=10)
    shop_name = models.CharField(max_length=30, blank=True, null=True)
    shop_addr = models.CharField(max_length=100, blank=True, null=True)
    shop_type = models.CharField(max_length=5, blank=True, null=True)
    shop_level = models.CharField(max_length=10, blank=True, null=True)
    shop_area = models.CharField(max_length=20, blank=True, null=True)
    busidisc_type_name = models.CharField(max_length=16, blank=True, null=True)
    salesman_name = models.CharField(max_length=20, blank=True, null=True)
    boss_name = models.CharField(max_length=20, blank=True, null=True)
    boss_tel_no = models.CharField(max_length=30, blank=True, null=True)
    sign_mode = models.CharField(max_length=16, blank=True, null=True)
    sign_status = models.CharField(max_length=8, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    createon = models.DateTimeField(blank=True, null=True)
    createby = models.CharField(max_length=5, blank=True, null=True)
    modifyon = models.DateTimeField(blank=True, null=True)
    modifyby = models.CharField(max_length=5, blank=True, null=True)
    link_to_shop_id = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    register_status = models.IntegerField(blank=True, null=True)
    distr_site = models.BigIntegerField(blank=True, null=True)
    subarea_id = models.CharField(max_length=16, blank=True, null=True)
    shop_streetid = models.IntegerField(db_column='shop_streetId', blank=True, null=True)  # Field name made lowercase.
    shop_streetname = models.CharField(db_column='shop_streetName', max_length=48, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cus$shop'


class CusShopGiverebate(models.Model):
    shop_id = models.CharField(max_length=10, blank=True, null=True)
    createon = models.DateTimeField(blank=True, null=True)
    modifyon = models.DateTimeField(blank=True, null=True)
    enable = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cus$shop_giverebate'


class CusShopOrdersInfo1115(models.Model):
    info_id = models.BigAutoField(primary_key=True)
    shop_id = models.BigIntegerField(blank=True, null=True)
    is_pay_deposit = models.SmallIntegerField(blank=True, null=True)
    sku_quantity = models.DecimalField(max_digits=13, decimal_places=0, blank=True, null=True)
    amount = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    dis_amount = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    deposit = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    createon = models.DateTimeField(blank=True, null=True)
    createby = models.CharField(max_length=15, blank=True, null=True)
    modifyon = models.DateTimeField(blank=True, null=True)
    modifyby = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cus$shop_orders_info_1115'


class CusShopSaletable(models.Model):
    shop_id = models.CharField(primary_key=True, max_length=10)
    sale_tablename = models.CharField(max_length=40)
    sale_recordcount = models.BigIntegerField(blank=True, null=True)
    upload_recenttime = models.CharField(max_length=40, blank=True, null=True)
    saletime_min = models.CharField(max_length=40, blank=True, null=True)
    saletime_max = models.CharField(max_length=40, blank=True, null=True)
    saletime_max_pos = models.CharField(max_length=40, blank=True, null=True)
    data_level = models.IntegerField(blank=True, null=True)
    data_source = models.CharField(max_length=1, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    isclear = models.CharField(db_column='isClear', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cus$shop_saletable'


class CusShopSubarea(models.Model):
    shop_id = models.CharField(max_length=16, blank=True, null=True)
    subarea_id = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cus$shop_subarea'


class CusStreet(models.Model):
    street_name = models.CharField(max_length=48, blank=True, null=True)
    depot_id = models.BigIntegerField(blank=True, null=True)
    district_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cus$street'


class CusSubarea(models.Model):
    subarea_name = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cus$subarea'


class CusUserTrajectory(models.Model):
    id = models.BigAutoField(primary_key=True)
    shop_id = models.CharField(max_length=10)
    operation = models.CharField(max_length=30)
    parent_menu = models.CharField(max_length=50, blank=True, null=True)
    operating_platform = models.CharField(max_length=200)
    operating_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cus$user_trajectory'


class DistributionSite(models.Model):
    site_id = models.BigAutoField(primary_key=True)
    site_name = models.CharField(max_length=100, blank=True, null=True)
    site_addr = models.CharField(max_length=150, blank=True, null=True)
    login_pwd = models.CharField(max_length=16, blank=True, null=True)
    site_area = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'distribution_site'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class GoodsSaleDetail(models.Model):
    detail_id = models.AutoField(primary_key=True)
    goodsid = models.CharField(db_column='goodsId', max_length=12, blank=True, null=True)  # Field name made lowercase.
    goodsname = models.CharField(db_column='goodsName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ordercount = models.IntegerField(db_column='orderCount', blank=True, null=True)  # Field name made lowercase.
    shopcount = models.IntegerField(db_column='shopCount', blank=True, null=True)  # Field name made lowercase.
    goodscount = models.IntegerField(db_column='goodsCount', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(blank=True, null=True)
    goodssort = models.CharField(db_column='goodsSort', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ordercreatedate = models.DateTimeField(db_column='orderCreateDate', blank=True, null=True)  # Field name made lowercase.
    ordersenddate = models.DateTimeField(db_column='orderSendDate', blank=True, null=True)  # Field name made lowercase.
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_sale_detail'


class Hh(models.Model):
    shop_id = models.CharField(primary_key=True, max_length=10)
    shop_name = models.CharField(max_length=30, blank=True, null=True)
    shop_addr = models.CharField(max_length=100, blank=True, null=True)
    shop_type = models.CharField(max_length=5, blank=True, null=True)
    shop_level = models.CharField(max_length=10, blank=True, null=True)
    shop_area = models.CharField(max_length=20, blank=True, null=True)
    busidisc_type_name = models.CharField(max_length=16, blank=True, null=True)
    salesman_name = models.CharField(max_length=20, blank=True, null=True)
    boss_name = models.CharField(max_length=20, blank=True, null=True)
    boss_tel_no = models.CharField(max_length=30, blank=True, null=True)
    sign_mode = models.CharField(max_length=16, blank=True, null=True)
    sign_status = models.CharField(max_length=8, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    createon = models.DateTimeField(blank=True, null=True)
    createby = models.CharField(max_length=5, blank=True, null=True)
    modifyon = models.DateTimeField(blank=True, null=True)
    modifyby = models.CharField(max_length=5, blank=True, null=True)
    link_to_shop_id = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    register_status = models.IntegerField(blank=True, null=True)
    distr_site = models.BigIntegerField(blank=True, null=True)
    subarea_id = models.CharField(max_length=16, blank=True, null=True)
    shop_streetid = models.IntegerField(db_column='shop_streetId', blank=True, null=True)  # Field name made lowercase.
    shop_streetname = models.CharField(db_column='shop_streetName', max_length=48, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hh'


class ItgSaleInfo(models.Model):
    barcode = models.CharField(primary_key=True, max_length=16)
    goods_name = models.CharField(max_length=24)
    goods_grade = models.SmallIntegerField()
    weeksalenum = models.IntegerField(db_column='weekSaleNum')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'itg_sale_info'


class PrdExchangeRule(models.Model):
    id = models.BigAutoField(primary_key=True)
    goods_exchange_id = models.BigIntegerField(blank=True, null=True)
    goods_id = models.CharField(max_length=16, blank=True, null=True)
    is_online = models.CharField(max_length=1, blank=True, null=True)
    per_order_limit = models.IntegerField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    exchange_type = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)
    ordinal = models.SmallIntegerField(blank=True, null=True)
    is_top = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prd$exchange_rule'


class PrdExchangeRuleRate(models.Model):
    id = models.BigAutoField(primary_key=True)
    exchange_rule_id = models.BigIntegerField(blank=True, null=True)
    exchange_qty = models.IntegerField(blank=True, null=True)
    goods_qty = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prd$exchange_rule_rate'


class PrdGoods(models.Model):
    goods_id = models.CharField(primary_key=True, max_length=16)
    goods_barcode = models.CharField(max_length=16, blank=True, null=True)
    goods_name = models.CharField(max_length=40, blank=True, null=True)
    brand_name = models.CharField(max_length=40, blank=True, null=True)
    spr_name = models.CharField(max_length=24, blank=True, null=True)
    quality_period = models.CharField(max_length=6, blank=True, null=True)
    goods_type_id = models.CharField(max_length=10, blank=True, null=True)
    unit_bas_name = models.CharField(max_length=8, blank=True, null=True)
    unit_pkg_name = models.CharField(max_length=8, blank=True, null=True)
    unit_cnvs_rate = models.IntegerField(blank=True, null=True)
    sale_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    sale_price_display = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    goods_rough_weight = models.DecimalField(max_digits=11, decimal_places=3, blank=True, null=True)
    goods_net_weight = models.DecimalField(max_digits=11, decimal_places=3, blank=True, null=True)
    unit_wgt_name = models.CharField(max_length=4, blank=True, null=True)
    goods_model = models.CharField(max_length=56, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    createon = models.DateTimeField(blank=True, null=True)
    createby = models.CharField(max_length=5, blank=True, null=True)
    modifyon = models.DateTimeField(blank=True, null=True)
    modifyby = models.CharField(max_length=5, blank=True, null=True)
    unit_pkg_code = models.CharField(max_length=8, blank=True, null=True)
    goods_pic_url = models.CharField(max_length=255, blank=True, null=True)
    goods_vol = models.DecimalField(max_digits=11, decimal_places=3)
    unit_bas_code = models.CharField(max_length=8, blank=True, null=True)
    goods_weekday = models.CharField(max_length=100, blank=True, null=True)
    goods_status = models.SmallIntegerField()
    goods_rough_weight_bas = models.DecimalField(max_digits=11, decimal_places=3)
    goods_net_weight_bas = models.DecimalField(max_digits=11, decimal_places=3)
    unit_wgt_bas = models.CharField(max_length=4, blank=True, null=True)
    goods_vol_bas = models.DecimalField(max_digits=11, decimal_places=3)
    unit_vol_bas = models.CharField(max_length=4, blank=True, null=True)
    goods_rough_weight_pkg = models.DecimalField(max_digits=11, decimal_places=3)
    goods_net_weight_pkg = models.DecimalField(max_digits=11, decimal_places=3)
    unit_wgt_pkg = models.CharField(max_length=4, blank=True, null=True)
    goods_vol_pkg = models.DecimalField(max_digits=11, decimal_places=3)
    unit_vol_pkg = models.CharField(max_length=4, blank=True, null=True)
    unit_cnvs_rate_purchase = models.IntegerField(blank=True, null=True)
    sales_limit = models.IntegerField()
    goods_type_id_v2 = models.CharField(max_length=10, blank=True, null=True)
    stock_qty = models.BigIntegerField(blank=True, null=True)
    subarea_id = models.CharField(max_length=16, blank=True, null=True)
    link_goods_id = models.CharField(max_length=18, blank=True, null=True)
    is_top = models.CharField(max_length=4, blank=True, null=True)
    goods_sale_ratio = models.IntegerField(blank=True, null=True)
    locator = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prd$goods'


class PrdGoodsAttrMap(models.Model):
    goods_id = models.CharField(max_length=16)
    goods_barcode = models.CharField(max_length=16)
    goods_name = models.CharField(max_length=32)
    goods_attr_no = models.CharField(max_length=10)
    goods_attr_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'prd$goods_attr_map'


class PrdGoodsBas(models.Model):
    goods_id = models.BigAutoField(primary_key=True)
    goods_barcode = models.CharField(max_length=20)
    goods_name = models.CharField(max_length=40)
    goods_type = models.ForeignKey('PrdGoodsType', models.DO_NOTHING, blank=True, null=True)
    brand_name = models.CharField(max_length=16, blank=True, null=True)
    goods_model = models.CharField(max_length=56, blank=True, null=True)
    unit_bas_name = models.CharField(max_length=8, blank=True, null=True)
    purchase_price = models.DecimalField(max_digits=11, decimal_places=5, blank=True, null=True)
    sale_price = models.DecimalField(max_digits=11, decimal_places=5, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    createon = models.DateTimeField(blank=True, null=True)
    createby = models.CharField(max_length=5, blank=True, null=True)
    modifyon = models.DateTimeField(blank=True, null=True)
    modifyby = models.CharField(max_length=5, blank=True, null=True)
    goods_type_name_top = models.CharField(max_length=8, blank=True, null=True)
    goods_type_name_mid = models.CharField(max_length=8, blank=True, null=True)
    goods_type_name_sml = models.CharField(max_length=8, blank=True, null=True)
    goods_attr_no = models.CharField(max_length=10, blank=True, null=True)
    goods_attr_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prd$goods_bas'


class PrdGoodsBasBac(models.Model):
    goods_id = models.BigIntegerField()
    goods_barcode = models.CharField(max_length=20)
    goods_name = models.CharField(max_length=40)
    goods_type_id = models.CharField(max_length=10, blank=True, null=True)
    brand_name = models.CharField(max_length=16, blank=True, null=True)
    goods_model = models.CharField(max_length=56, blank=True, null=True)
    unit_bas_name = models.CharField(max_length=8, blank=True, null=True)
    purchase_price = models.DecimalField(max_digits=11, decimal_places=5, blank=True, null=True)
    sale_price = models.DecimalField(max_digits=11, decimal_places=5, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    createon = models.DateTimeField(blank=True, null=True)
    createby = models.CharField(max_length=5, blank=True, null=True)
    modifyon = models.DateTimeField(blank=True, null=True)
    modifyby = models.CharField(max_length=5, blank=True, null=True)
    goods_type_name_top = models.CharField(max_length=8, blank=True, null=True)
    goods_type_name_mid = models.CharField(max_length=8, blank=True, null=True)
    goods_type_name_sml = models.CharField(max_length=8, blank=True, null=True)
    goods_attr_no = models.CharField(max_length=10, blank=True, null=True)
    goods_attr_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prd$goods_bas_bac'


class PrdGoodsBasExt(models.Model):
    goods_barcode = models.CharField(max_length=20)
    goods_name = models.CharField(max_length=40)
    goods_type_id = models.CharField(max_length=10)
    brand_name = models.CharField(max_length=16, blank=True, null=True)
    goods_model = models.CharField(max_length=56, blank=True, null=True)
    unit_bas_name = models.CharField(max_length=8, blank=True, null=True)
    purchase_price = models.DecimalField(max_digits=11, decimal_places=5, blank=True, null=True)
    sale_price = models.DecimalField(max_digits=11, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prd$goods_bas_ext'


class PrdGoodsCheck(models.Model):
    check_id = models.BigAutoField(primary_key=True)
    goods_id = models.CharField(max_length=20, blank=True, null=True)
    goods_barcode = models.CharField(max_length=20, blank=True, null=True)
    goods_barcode_upd = models.CharField(max_length=20, blank=True, null=True)
    goods_name = models.CharField(max_length=50, blank=True, null=True)
    goods_name_upd = models.CharField(max_length=50)
    goods_price = models.CharField(max_length=20, blank=True, null=True)
    goods_price_upd = models.CharField(max_length=20)
    goods_unit_name = models.CharField(max_length=10, blank=True, null=True)
    goods_unit_name_upd = models.CharField(max_length=10)
    goods_unit_code = models.CharField(max_length=10, blank=True, null=True)
    goods_unit_code_upd = models.CharField(max_length=10)
    goods_type_id = models.CharField(max_length=10, blank=True, null=True)
    goods_type_id_upd = models.CharField(max_length=10)
    goods_limit_count = models.IntegerField(blank=True, null=True)
    goods_limit_count_upd = models.IntegerField(blank=True, null=True)
    goods_week = models.CharField(max_length=100, blank=True, null=True)
    goods_week_upd = models.CharField(max_length=100, blank=True, null=True)
    goods_id_period = models.CharField(max_length=20, blank=True, null=True)
    goods_id_period_upd = models.CharField(max_length=20, blank=True, null=True)
    is_goods_on_best = models.CharField(max_length=1, blank=True, null=True)
    is_goods_on_best_upd = models.CharField(max_length=1, blank=True, null=True)
    is_goods_on_free = models.CharField(max_length=1, blank=True, null=True)
    is_goods_on_free_upd = models.CharField(max_length=1, blank=True, null=True)
    create_by = models.CharField(max_length=20, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modify_by = models.CharField(max_length=20, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    check_by = models.CharField(max_length=20, blank=True, null=True)
    check_time = models.DateTimeField(blank=True, null=True)
    is_check = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prd$goods_check'


class PrdGoodsDiscountType(models.Model):
    type_value = models.FloatField(blank=True, null=True)
    type_desc = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prd$goods_discount_type'


class PrdGoodsExchange(models.Model):
    id = models.BigAutoField(primary_key=True)
    pname = models.CharField(max_length=40, blank=True, null=True)
    pname_abbr = models.CharField(max_length=40, blank=True, null=True)
    img_url = models.CharField(max_length=200, blank=True, null=True)
    exchange_unit = models.CharField(max_length=2, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)
    logo_type = models.IntegerField(blank=True, null=True)
    is_top = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prd$goods_exchange'


class PrdGoodsForecast(models.Model):
    goods_id = models.CharField(primary_key=True, max_length=16)
    goods_barcode = models.CharField(max_length=16, blank=True, null=True)
    goods_name = models.CharField(max_length=50, blank=True, null=True)
    goods_order = models.SmallIntegerField(blank=True, null=True)
    is_tmpl = models.CharField(max_length=1)
    is_tmpl_ext = models.CharField(max_length=1)
    tmpl_ext_order = models.IntegerField()
    tmpl_sale_qty = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prd$goods_forecast'


class PrdGoodsPriceCompare(models.Model):
    goods_barcode = models.CharField(max_length=16)
    goods_id = models.CharField(max_length=16, blank=True, null=True)
    goods_name = models.CharField(max_length=50, blank=True, null=True)
    sale_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    sale_unit_code = models.CharField(max_length=8)
    sale_unit_name = models.CharField(max_length=8)
    compare_shop_name = models.CharField(max_length=50)
    createon = models.DateTimeField(blank=True, null=True)
    createby = models.CharField(max_length=15, blank=True, null=True)
    modifyon = models.DateTimeField(blank=True, null=True)
    modifyby = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prd$goods_price_compare'


class PrdGoodsSaleInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    goods_id = models.CharField(max_length=16)
    sale_info_type = models.IntegerField()
    sale_info_value = models.CharField(max_length=500, blank=True, null=True)
    sale_sort = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prd$goods_sale_info'


class PrdGoodsType(models.Model):
    goods_type_id = models.SmallIntegerField(primary_key=True)
    goods_type_no = models.CharField(max_length=10)
    goods_type_name = models.CharField(max_length=24)
    goods_type_parent = models.SmallIntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    createon = models.DateTimeField(blank=True, null=True)
    createby = models.CharField(max_length=5, blank=True, null=True)
    modifyon = models.DateTimeField(blank=True, null=True)
    modifyby = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prd$goods_type'


class PrdGoodsTypeV2(models.Model):
    pkid = models.BigAutoField(primary_key=True)
    goods_type_no_l1 = models.CharField(max_length=10, blank=True, null=True)
    goods_type_name_l1 = models.CharField(max_length=20, blank=True, null=True)
    goods_type_no_l2 = models.CharField(max_length=10, blank=True, null=True)
    goods_type_name_l2 = models.CharField(max_length=20, blank=True, null=True)
    goods_type_no_l3 = models.CharField(max_length=10, blank=True, null=True)
    goods_type_name_l3 = models.CharField(max_length=20, blank=True, null=True)
    goods_type_no_l4 = models.CharField(max_length=10, blank=True, null=True)
    goods_type_name_l4 = models.CharField(max_length=20, blank=True, null=True)
    goods_type_no_old = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prd$goods_type_v2'


class PrdGoodsTypeV2Copy(models.Model):
    pkid = models.BigAutoField(primary_key=True)
    goods_type_no_l1 = models.CharField(max_length=10, blank=True, null=True)
    goods_type_name_l1 = models.CharField(max_length=20, blank=True, null=True)
    goods_type_no_l2 = models.CharField(max_length=10, blank=True, null=True)
    goods_type_name_l2 = models.CharField(max_length=20, blank=True, null=True)
    goods_type_no_l3 = models.CharField(max_length=10, blank=True, null=True)
    goods_type_name_l3 = models.CharField(max_length=20, blank=True, null=True)
    goods_type_no_l4 = models.CharField(max_length=10, blank=True, null=True)
    goods_type_name_l4 = models.CharField(max_length=20, blank=True, null=True)
    goods_type_no_old = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prd$goods_type_v2_copy'


class PrdShopStock(models.Model):
    shop_id = models.CharField(max_length=10)
    goods_name = models.CharField(max_length=50, blank=True, null=True)
    bar_code = models.CharField(max_length=20)
    stock_qty = models.IntegerField(blank=True, null=True)
    stock_qty_real = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=5, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifyon = models.DateTimeField(blank=True, null=True)
    goods_id = models.CharField(max_length=16, blank=True, null=True)
    type_no = models.CharField(max_length=10, blank=True, null=True)
    stock_updata_time = models.DateTimeField(blank=True, null=True)
    last_syn_delivery_datetime = models.DateTimeField(blank=True, null=True)
    last_syn_sale_datetime = models.DateTimeField(blank=True, null=True)
    stock_id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'prd$shop_stock'


class PrdShopStockBac20160318(models.Model):
    shop_id = models.CharField(max_length=10)
    goods_name = models.CharField(max_length=50, blank=True, null=True)
    bar_code = models.CharField(max_length=20)
    stock_qty = models.IntegerField(blank=True, null=True)
    stock_qty_real = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=5, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifyon = models.DateTimeField(blank=True, null=True)
    goods_id = models.CharField(max_length=16, blank=True, null=True)
    type_no = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prd$shop_stock_bac20160318'


class PrdShopStockLog(models.Model):
    log_id = models.BigAutoField(primary_key=True)
    stock_id = models.IntegerField()
    create_time = models.DateTimeField()
    stock_qty = models.IntegerField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    log_type = models.IntegerField(blank=True, null=True)
    log_remark = models.CharField(max_length=100, blank=True, null=True)
    log_batch = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prd$shop_stock_log'


class PrdSmartModel(models.Model):
    goods_id = models.CharField(max_length=16, blank=True, null=True)
    goods_type = models.CharField(db_column='goods_Type', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prd$smart_model'


class ReportAllshopRecorde(models.Model):
    goods_barcode = models.CharField(max_length=32)
    goods_name = models.CharField(max_length=50)
    sale_qty = models.FloatField()
    sale_price = models.FloatField()
    idc_price = models.FloatField()
    shop_id = models.CharField(max_length=16)
    create_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'report$allshop_recorde'


class ReportTop2000(models.Model):
    barcode = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report$top2000'


class SaleAliPayInfo(models.Model):
    out_trade_no = models.CharField(max_length=64, blank=True, null=True)
    notify_time = models.DateTimeField(blank=True, null=True)
    subject = models.CharField(max_length=128, blank=True, null=True)
    trade_no = models.CharField(max_length=64, blank=True, null=True)
    trade_status = models.CharField(max_length=30, blank=True, null=True)
    seller_id = models.CharField(max_length=30, blank=True, null=True)
    seller_email = models.CharField(max_length=100, blank=True, null=True)
    buyer_id = models.CharField(max_length=20, blank=True, null=True)
    buyer_email = models.CharField(max_length=100, blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    gmt_create = models.DateTimeField(blank=True, null=True)
    gmt_payment = models.DateTimeField(blank=True, null=True)
    is_total_fee_adjust = models.CharField(max_length=1, blank=True, null=True)
    use_coupon = models.CharField(max_length=1, blank=True, null=True)
    discount = models.CharField(max_length=10, blank=True, null=True)
    refund_status = models.CharField(max_length=20, blank=True, null=True)
    gmt_refund = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale$ali_pay_info'


class SaleCoupons(models.Model):
    coupons_id = models.BigIntegerField(primary_key=True)
    coupons_name = models.CharField(max_length=20, blank=True, null=True)
    coupons_desc = models.CharField(max_length=200, blank=True, null=True)
    explain = models.CharField(max_length=255, blank=True, null=True)
    coupons_value = models.IntegerField(blank=True, null=True)
    valid_days = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale$coupons'


class SaleOrderCoupons(models.Model):
    oc_id = models.BigAutoField(primary_key=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    shop_coupons_id = models.BigIntegerField(blank=True, null=True)
    isdelete = models.CharField(max_length=1)
    createon = models.DateTimeField(blank=True, null=True)
    modifyon = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale$order_coupons'


class SaleOrders(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    forecast_id = models.BigIntegerField(blank=True, null=True)
    order_type = models.CharField(max_length=4, blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    shop_id = models.CharField(max_length=10, blank=True, null=True)
    order_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    order_amount_pay = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    order_channel = models.CharField(max_length=10, blank=True, null=True)
    order_status = models.CharField(max_length=5, blank=True, null=True)
    pay_type = models.CharField(max_length=10, blank=True, null=True)
    is_paid = models.CharField(max_length=1, blank=True, null=True)
    createon = models.DateTimeField(blank=True, null=True)
    createby = models.CharField(max_length=10, blank=True, null=True)
    modifyon = models.DateTimeField(blank=True, null=True)
    modifyby = models.CharField(max_length=10, blank=True, null=True)
    order_id_sap = models.CharField(max_length=128, blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    shop_addr = models.CharField(max_length=100, blank=True, null=True)
    shop_tel_no = models.CharField(max_length=30, blank=True, null=True)
    shop_contacts = models.CharField(max_length=20, blank=True, null=True)
    remarks = models.CharField(max_length=200, blank=True, null=True)
    order_id_scm = models.CharField(max_length=15, blank=True, null=True)
    distr_site = models.BigIntegerField(blank=True, null=True)
    subarea_id = models.IntegerField(db_column='subarea_Id')  # Field name made lowercase.
    check_order_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    check_order_amount_pay = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    send_amount = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    send_amount_pay = models.DecimalField(max_digits=13, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale$orders'


class SaleOrdersExchangeItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    exchange_rule_id = models.BigIntegerField(blank=True, null=True)
    exchange_qty = models.IntegerField(blank=True, null=True)
    goods_qty = models.IntegerField(blank=True, null=True)
    is_top = models.CharField(max_length=4, blank=True, null=True)
    sale_order_sap = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale$orders_exchange_item'


class SaleOrdersItem(models.Model):
    order_item_id = models.BigAutoField(primary_key=True)
    order_id = models.CharField(max_length=10)
    goods_id = models.CharField(max_length=16, blank=True, null=True)
    sale_unit = models.CharField(max_length=3, blank=True, null=True)
    sale_qty = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sale_price = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    dis_price = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sale_amt = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=5, blank=True, null=True)
    createon = models.DateTimeField(blank=True, null=True)
    createby = models.CharField(max_length=10, blank=True, null=True)
    modifyon = models.DateTimeField(blank=True, null=True)
    modifyby = models.CharField(max_length=10, blank=True, null=True)
    goods_type_no = models.CharField(max_length=10, blank=True, null=True)
    order_id_sap = models.CharField(max_length=18, blank=True, null=True)
    is_top = models.CharField(max_length=4, blank=True, null=True)
    order_id_scm = models.CharField(max_length=16, blank=True, null=True)
    subarea_id = models.IntegerField(db_column='subarea_Id')  # Field name made lowercase.
    check_sales_quantity = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    is_check = models.CharField(max_length=1, blank=True, null=True)
    send_qty = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale$orders_item'


class SaleOrdersRebate(models.Model):
    pkid = models.BigAutoField(primary_key=True)
    shop_id = models.CharField(max_length=10)
    order_id_from = models.BigIntegerField()
    order_id_to = models.BigIntegerField()
    rebate_type = models.IntegerField()
    order_amt = models.DecimalField(max_digits=11, decimal_places=2)
    rebate_amt = models.DecimalField(max_digits=11, decimal_places=2)
    exp_date = models.DateField()
    isdelete = models.CharField(max_length=1)
    createon = models.DateTimeField()
    createby = models.CharField(max_length=5)
    modifyon = models.DateTimeField(blank=True, null=True)
    modifyby = models.CharField(max_length=5, blank=True, null=True)
    replace_order_id = models.CharField(max_length=20, blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale$orders_rebate'


class SaleOrdersRebateLog(models.Model):
    log_id = models.BigAutoField(primary_key=True)
    shop_id = models.CharField(max_length=10, blank=True, null=True)
    order_id = models.BigIntegerField()
    rebate_type = models.IntegerField(blank=True, null=True)
    rebate_amt = models.DecimalField(max_digits=11, decimal_places=2)
    createon = models.DateTimeField(blank=True, null=True)
    createby = models.CharField(max_length=5, blank=True, null=True)
    modifyon = models.DateTimeField(blank=True, null=True)
    modifyby = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale$orders_rebate_log'


class SaleOrdersRebateLogBac20160507(models.Model):
    log_id = models.BigIntegerField()
    shop_id = models.CharField(max_length=10, blank=True, null=True)
    order_id = models.BigIntegerField()
    rebate_type = models.IntegerField(blank=True, null=True)
    rebate_amt = models.DecimalField(max_digits=11, decimal_places=2)
    createon = models.DateTimeField(blank=True, null=True)
    createby = models.CharField(max_length=5, blank=True, null=True)
    modifyon = models.DateTimeField(blank=True, null=True)
    modifyby = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale$orders_rebate_log_bac20160507'


class SaleOrdersRebateTotal(models.Model):
    shop_id = models.CharField(primary_key=True, max_length=10)
    total_amt = models.DecimalField(max_digits=11, decimal_places=2)
    exp_date = models.DateField()
    createon = models.DateTimeField(blank=True, null=True)
    createby = models.CharField(max_length=5, blank=True, null=True)
    modifyon = models.DateTimeField(blank=True, null=True)
    modifyby = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale$orders_rebate_total'


class SaleRecommendGoods(models.Model):
    id = models.BigAutoField(primary_key=True)
    goods_barcode = models.CharField(max_length=16, blank=True, null=True)
    goods_name = models.CharField(max_length=200, blank=True, null=True)
    shop_id = models.CharField(max_length=10)
    createon = models.DateTimeField(blank=True, null=True)
    modifyon = models.DateTimeField(blank=True, null=True)
    error_desc = models.CharField(max_length=200, blank=True, null=True)
    error_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale$recommend_goods'


class SaleRecommendGoodsSmoke(models.Model):
    id = models.BigAutoField(primary_key=True)
    goods_barcode = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale$recommend_goods_smoke'


class SaleRecommendGoodsWinners(models.Model):
    id = models.BigAutoField(primary_key=True)
    shop_id = models.CharField(max_length=10)
    shop_name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'sale$recommend_goods_winners'


class SaleShopCoupons(models.Model):
    id = models.BigAutoField(primary_key=True)
    coupons_id = models.CharField(max_length=20)
    from_shop_id = models.BigIntegerField(blank=True, null=True)
    shop_id = models.BigIntegerField()
    createon = models.DateTimeField(blank=True, null=True)
    expre_date_from = models.DateField(blank=True, null=True)
    modifyon = models.DateTimeField(blank=True, null=True)
    expre_date_to = models.DateField(blank=True, null=True)
    isused = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'sale$shop_coupons'


class SaleShopIntegral(models.Model):
    id = models.BigAutoField(primary_key=True)
    shop_id = models.CharField(unique=True, max_length=10, blank=True, null=True)
    begin_weekday = models.IntegerField(blank=True, null=True)
    dis_sub_amount = models.FloatField(blank=True, null=True)
    dis_sub_amount20160420 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale$shop_integral'


class SaleShopIntegralAddTmp(models.Model):
    shop_id = models.CharField(primary_key=True, max_length=10)
    dis_sub_amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale$shop_integral_add_tmp'


class SaleShopIntegralBac20160317(models.Model):
    id = models.BigIntegerField(primary_key=True)
    shop_id = models.CharField(max_length=10, blank=True, null=True)
    begin_weekday = models.IntegerField(blank=True, null=True)
    dis_sub_amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale$shop_integral_bac20160317'


class SaleShopIntegralBac20160413(models.Model):
    id = models.BigIntegerField(primary_key=True)
    shop_id = models.CharField(max_length=10, blank=True, null=True)
    begin_weekday = models.IntegerField(blank=True, null=True)
    dis_sub_amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale$shop_integral_bac20160413'


class SaleShopIntegralLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    shop_id = models.CharField(max_length=10, blank=True, null=True)
    dis_sub_amount = models.FloatField(blank=True, null=True)
    create_datetime = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)
    dis_sub_amount_old = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale$shop_integral_log'


class SaleShopRebateLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    previous_id = models.BigIntegerField(blank=True, null=True)
    shop_id = models.CharField(max_length=10)
    index = models.IntegerField(blank=True, null=True)
    start_order_date = models.DateField(blank=True, null=True)
    end_order_date = models.DateField(blank=True, null=True)
    max_delivery_date = models.DateField(blank=True, null=True)
    is_generated = models.IntegerField(blank=True, null=True)
    is_generate_success = models.IntegerField(blank=True, null=True)
    generete_remark = models.TextField(blank=True, null=True)
    order_id_scms = models.TextField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    modify_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale$shop_rebate_log'


class SaleWxPayInfo(models.Model):
    create_time = models.DateTimeField(blank=True, null=True)
    appid = models.CharField(max_length=32, blank=True, null=True)
    mch_id = models.CharField(max_length=32, blank=True, null=True)
    device_info = models.CharField(max_length=100, blank=True, null=True)
    nonce_str = models.CharField(max_length=32, blank=True, null=True)
    sign = models.CharField(max_length=32, blank=True, null=True)
    result_code = models.CharField(max_length=20, blank=True, null=True)
    err_code = models.CharField(max_length=40, blank=True, null=True)
    err_code_des = models.CharField(max_length=140, blank=True, null=True)
    openid = models.CharField(max_length=140, blank=True, null=True)
    is_subscribe = models.CharField(max_length=2, blank=True, null=True)
    trade_type = models.CharField(max_length=16, blank=True, null=True)
    bank_type = models.CharField(max_length=16, blank=True, null=True)
    total_fee = models.IntegerField(blank=True, null=True)
    fee_type = models.CharField(max_length=140, blank=True, null=True)
    cash_fee = models.CharField(max_length=140, blank=True, null=True)
    cash_fee_type = models.CharField(max_length=8, blank=True, null=True)
    coupon_fee = models.IntegerField(blank=True, null=True)
    coupon_count = models.CharField(max_length=140, blank=True, null=True)
    coupon_id_n = models.CharField(db_column='coupon_id_$n', max_length=140, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    coupon_fee_n = models.CharField(db_column='coupon_fee_$n', max_length=140, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    transaction_id = models.CharField(max_length=32, blank=True, null=True)
    out_trade_no = models.CharField(max_length=32, blank=True, null=True)
    attach = models.CharField(max_length=140, blank=True, null=True)
    time_end = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale$wx_pay_info'


class SalesOrderITemp(models.Model):
    order_id = models.CharField(max_length=20)
    goods_id = models.CharField(max_length=20)
    goods_name = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField()
    order_qty = models.FloatField(blank=True, null=True)
    goods_unit = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_order_i_temp'


class Sequence(models.Model):
    seq_name = models.CharField(primary_key=True, max_length=50)
    current_val = models.BigIntegerField()
    increment_val = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sequence'


class ServLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    log_date = models.CharField(max_length=30)
    shop_id = models.CharField(max_length=20, blank=True, null=True)
    log_content = models.CharField(max_length=50, blank=True, null=True)
    log_detail = models.TextField(blank=True, null=True)
    log_error = models.TextField(blank=True, null=True)
    log_remark = models.TextField(blank=True, null=True)
    log_level = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serv$log'


class ShopRemark(models.Model):
    create_time = models.DateTimeField(blank=True, null=True)
    creator = models.CharField(max_length=15, blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)
    shop_id = models.CharField(max_length=10, blank=True, null=True)
    creatorid = models.CharField(db_column='creatorId', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shop_remark'


class SiteContacter(models.Model):
    contacter_id = models.BigAutoField(primary_key=True)
    site_id = models.BigIntegerField(blank=True, null=True)
    contacter_name = models.CharField(max_length=10, blank=True, null=True)
    contact_phone = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'site_contacter'


class SupGoods(models.Model):
    goods_id = models.CharField(max_length=16)
    goods_barcode = models.CharField(max_length=16)
    goods_name = models.CharField(max_length=50)
    sup_id = models.CharField(max_length=10)
    sup_orgid = models.CharField(max_length=10)
    status = models.CharField(max_length=1, blank=True, null=True)
    createon = models.DateTimeField(blank=True, null=True)
    createby = models.CharField(max_length=5, blank=True, null=True)
    modifyon = models.DateTimeField(blank=True, null=True)
    modifyby = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sup$goods'


class SupPurchase(models.Model):
    order_id = models.CharField(primary_key=True, max_length=10)
    forecast_id = models.BigIntegerField(blank=True, null=True)
    order_type = models.CharField(max_length=4, blank=True, null=True)
    company_code = models.CharField(max_length=4, blank=True, null=True)
    company_name = models.CharField(max_length=40, blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True)
    order_confirm_status = models.CharField(max_length=1, blank=True, null=True)
    order_confirm_date = models.DateTimeField(blank=True, null=True)
    vendor_id = models.CharField(max_length=10, blank=True, null=True)
    vendor_name = models.CharField(max_length=40, blank=True, null=True)
    currency = models.CharField(max_length=5, blank=True, null=True)
    order_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    purchaser = models.CharField(db_column='Purchaser', max_length=8, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=1, blank=True, null=True)
    createon = models.DateTimeField(blank=True, null=True)
    createby = models.CharField(max_length=5, blank=True, null=True)
    modifyon = models.DateTimeField(blank=True, null=True)
    modifyby = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sup$purchase'


class SupPurchaseItem(models.Model):
    order_id = models.CharField(max_length=10)
    order_item_id = models.CharField(max_length=6)
    goods_id = models.CharField(max_length=16, blank=True, null=True)
    order_qty = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    order_unit = models.CharField(max_length=3, blank=True, null=True)
    item_base_qty = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    item_base_unit = models.CharField(max_length=3, blank=True, null=True)
    price = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    price_tax = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    item_amount = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=5, blank=True, null=True)
    confirm_qty = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    confirm_date = models.DateTimeField(blank=True, null=True)
    is_delivery = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sup$purchase_item'


class SupSupplier(models.Model):
    sup_id = models.CharField(primary_key=True, max_length=10)
    sup_name = models.CharField(max_length=20)
    sup_linkman = models.CharField(max_length=5)
    sup_phone = models.CharField(max_length=16)
    sup_country = models.CharField(max_length=8, blank=True, null=True)
    sup_region = models.CharField(max_length=8, blank=True, null=True)
    sup_addr = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    createon = models.DateTimeField(blank=True, null=True)
    createby = models.CharField(max_length=5, blank=True, null=True)
    modifyon = models.DateTimeField(blank=True, null=True)
    modifyby = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sup$supplier'


class TBarcodeNosale(models.Model):
    barcode_id = models.CharField(max_length=20)
    goods_name = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_barcode_nosale'


class TBehaviorDescription(models.Model):
    bd_id = models.AutoField(primary_key=True)
    bd_content = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_behavior_description'


class TBehaviorMonitoring(models.Model):
    bm_id = models.AutoField(primary_key=True)
    bd_id = models.IntegerField(blank=True, null=True)
    bm_url = models.TextField(blank=True, null=True)
    bm_target = models.CharField(max_length=50, blank=True, null=True)
    bm_remark = models.CharField(max_length=100, blank=True, null=True)
    bm_user_name = models.CharField(max_length=20, blank=True, null=True)
    bm_time = models.DateTimeField(blank=True, null=True)
    bm_ip = models.CharField(max_length=20, blank=True, null=True)
    bm_source = models.CharField(max_length=10, blank=True, null=True)
    bm_device = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_behavior_monitoring'


class TLog(models.Model):
    datetime = models.DateTimeField(db_column='DateTime')  # Field name made lowercase.
    operdesc = models.CharField(db_column='OperDesc', max_length=50)  # Field name made lowercase.
    recordcount = models.IntegerField(db_column='RecordCount')  # Field name made lowercase.
    usetimes = models.CharField(db_column='UseTimes', max_length=10)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_log'


class TSaleAll(models.Model):
    sale_id = models.CharField(max_length=40)
    record_no = models.IntegerField()
    barcode_id = models.CharField(max_length=32)
    sale_qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    item_amount = models.DecimalField(max_digits=11, decimal_places=2)
    shop_id = models.CharField(max_length=10)
    sale_time = models.DateTimeField()
    data_source = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 't_sale_all'


class TSaleRecordCount(models.Model):
    shopid = models.CharField(max_length=20, blank=True, null=True)
    recordcount = models.IntegerField(db_column='recordCount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sale_record_count'


class TSaleTop(models.Model):
    shopid = models.CharField(max_length=20, blank=True, null=True)
    barcodeid = models.CharField(max_length=30, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_sale_top'


class TSaleTop2000(models.Model):
    shopid = models.CharField(max_length=15, blank=True, null=True)
    barcodeid = models.CharField(max_length=40, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    sale_price = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    days = models.IntegerField(blank=True, null=True)
    qtyoneday = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_sale_top2000'


class TSaleTopsku(models.Model):
    barcodeid = models.CharField(max_length=40, blank=True, null=True)
    qtyoneday = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    price_avg = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_sale_topsku'


class Temp(models.Model):
    barcode = models.CharField(max_length=100, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    sale_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp'


class TempDiscountForecast2(models.Model):
    forecast_id_tag = models.BigIntegerField()
    goods_id_tag = models.CharField(max_length=8)
    forecast_id_copy_from = models.CharField(max_length=40,blank=True, null=True)
    item_id = models.BigIntegerField(blank=True, null=True)
    forecast_id = models.CharField(max_length=10, blank=True, null=True)
    goods_id = models.CharField(max_length=16, blank=True, null=True)
    goods_name = models.CharField(max_length=40, blank=True, null=True)
    sales_unit = models.CharField(max_length=3, blank=True, null=True)
    sales_quantity = models.DecimalField(max_digits=13, decimal_places=0, blank=True, null=True)
    sales_price = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=5, blank=True, null=True)
    goods_type_no = models.CharField(max_length=10, blank=True, null=True)
    goods_type_name = models.CharField(max_length=24, blank=True, null=True)
    sales_in_week_pkg_qty = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_in_period_bas_qty = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_in_week_bas_qty = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_price_bas = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_price_pkg = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    goods_level = models.CharField(max_length=1, blank=True, null=True)
    sales_unit_bas = models.CharField(max_length=50, blank=True, null=True)
    sales_unit_pkg = models.CharField(max_length=50, blank=True, null=True)
    goods_type_parent_no = models.CharField(max_length=10, blank=True, null=True)
    goods_type_parent_name = models.CharField(max_length=24, blank=True, null=True)
    sales_unit_code = models.CharField(max_length=5, blank=True, null=True)
    sales_price_max = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_price_min = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_price_avg = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_vol = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    forecast_item_type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_discount_forecast2'


class TempDiscountForecast1016(models.Model):
    forecast_id_tag = models.BigIntegerField()
    goods_id_tag = models.CharField(max_length=8)
    forecast_id_copy_from = models.CharField(max_length=10, blank=True, null=True)
    item_id = models.BigIntegerField(blank=True, null=True)
    forecast_id = models.CharField(max_length=10, blank=True, null=True)
    goods_id = models.CharField(max_length=16, blank=True, null=True)
    goods_name = models.CharField(max_length=40, blank=True, null=True)
    sales_unit = models.CharField(max_length=3, blank=True, null=True)
    sales_quantity = models.DecimalField(max_digits=13, decimal_places=0, blank=True, null=True)
    sales_price = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=5, blank=True, null=True)
    goods_type_no = models.CharField(max_length=10, blank=True, null=True)
    goods_type_name = models.CharField(max_length=24, blank=True, null=True)
    sales_in_week_pkg_qty = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_in_period_bas_qty = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_in_week_bas_qty = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_price_bas = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_price_pkg = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    goods_level = models.CharField(max_length=1, blank=True, null=True)
    sales_unit_bas = models.CharField(max_length=50, blank=True, null=True)
    sales_unit_pkg = models.CharField(max_length=50, blank=True, null=True)
    goods_type_parent_no = models.CharField(max_length=10, blank=True, null=True)
    goods_type_parent_name = models.CharField(max_length=24, blank=True, null=True)
    sales_unit_code = models.CharField(max_length=5, blank=True, null=True)
    sales_price_max = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_price_min = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_price_avg = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_vol = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    forecast_item_type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_discount_forecast_10_16'


class TempDiscountForecast1723(models.Model):
    forecast_id_tag = models.BigIntegerField()
    goods_id_tag = models.CharField(max_length=8)
    forecast_id_copy_from = models.CharField(max_length=10, blank=True, null=True)
    item_id = models.BigIntegerField(blank=True, null=True)
    forecast_id = models.CharField(max_length=10, blank=True, null=True)
    goods_id = models.CharField(max_length=16, blank=True, null=True)
    goods_name = models.CharField(max_length=40, blank=True, null=True)
    sales_unit = models.CharField(max_length=3, blank=True, null=True)
    sales_quantity = models.DecimalField(max_digits=13, decimal_places=0, blank=True, null=True)
    sales_price = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=5, blank=True, null=True)
    goods_type_no = models.CharField(max_length=10, blank=True, null=True)
    goods_type_name = models.CharField(max_length=24, blank=True, null=True)
    sales_in_week_pkg_qty = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_in_period_bas_qty = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_in_week_bas_qty = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_price_bas = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_price_pkg = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    goods_level = models.CharField(max_length=1, blank=True, null=True)
    sales_unit_bas = models.CharField(max_length=50, blank=True, null=True)
    sales_unit_pkg = models.CharField(max_length=50, blank=True, null=True)
    goods_type_parent_no = models.CharField(max_length=10, blank=True, null=True)
    goods_type_parent_name = models.CharField(max_length=24, blank=True, null=True)
    sales_unit_code = models.CharField(max_length=5, blank=True, null=True)
    sales_price_max = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_price_min = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_price_avg = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    sales_vol = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    forecast_item_type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_discount_forecast_17_23'


class TestGoodsExcel(models.Model):
    goods_barcode = models.CharField(max_length=16, blank=True, null=True)
    goods_id = models.CharField(max_length=32, blank=True, null=True)
    goods_name = models.CharField(max_length=32, blank=True, null=True)
    goods_spec = models.CharField(max_length=32, blank=True, null=True)
    unit_name_bas = models.CharField(max_length=8, blank=True, null=True)
    cost_price = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    unit_name_cost_price = models.CharField(max_length=8, blank=True, null=True)
    sale_price = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    unit_name_sale_price = models.CharField(max_length=8, blank=True, null=True)
    trans_ratio = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    shop_name = models.CharField(max_length=30, blank=True, null=True)
    shop_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_goods_excel'


class TmpExchangeDepot(models.Model):
    ge_id = models.CharField(max_length=16, blank=True, null=True)
    depot_id = models.BigIntegerField(blank=True, null=True)
    goods_status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_exchange_depot'


class TmpGoods(models.Model):
    goods_id = models.CharField(max_length=16)
    goods_barcode = models.CharField(max_length=16)
    goods_name = models.CharField(max_length=40)
    brand_name = models.CharField(max_length=16)
    spr_name = models.CharField(max_length=24)
    quality_period = models.SmallIntegerField(blank=True, null=True)
    goods_type_id = models.CharField(max_length=10)
    unit_bas_name = models.CharField(max_length=8)
    unit_pkg_name = models.CharField(max_length=8)
    unit_cnvs_rate = models.IntegerField()
    sale_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    goods_rough_weight = models.DecimalField(max_digits=11, decimal_places=3, blank=True, null=True)
    goods_net_weight = models.DecimalField(max_digits=11, decimal_places=3, blank=True, null=True)
    unit_wgt_name = models.CharField(max_length=4, blank=True, null=True)
    goods_model = models.CharField(max_length=56, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    createon = models.DateTimeField(blank=True, null=True)
    createby = models.CharField(max_length=5, blank=True, null=True)
    modifyon = models.DateTimeField(blank=True, null=True)
    modifyby = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_goods'


class TmpGoodsAttr(models.Model):
    goods_id = models.CharField(max_length=16)
    goods_barcode = models.CharField(max_length=16)
    goods_name = models.CharField(max_length=32)
    goods_attr_no = models.CharField(max_length=10)
    goods_attr_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tmp_goods_attr'


class TmpGoodsDepot(models.Model):
    id = models.BigAutoField(primary_key=True)
    goods_id = models.CharField(max_length=16, blank=True, null=True)
    goods_limit = models.IntegerField(blank=True, null=True)
    goods_stock = models.IntegerField(blank=True, null=True)
    depot_id = models.BigIntegerField(blank=True, null=True)
    goods_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    goods_status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_goods_depot'


class TmpGoodsOrder(models.Model):
    order_no = models.IntegerField(primary_key=True)
    goods_barcode = models.CharField(max_length=20, blank=True, null=True)
    order_amt = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_goods_order'


class TmpGoodsPurchase(models.Model):
    goods_id = models.CharField(primary_key=True, max_length=20)
    goods_name = models.CharField(max_length=40)
    goods_type_desc = models.CharField(max_length=20)
    sale_unit = models.CharField(max_length=2)
    sale_price = models.DecimalField(max_digits=8, decimal_places=2)
    dis_price = models.DecimalField(max_digits=8, decimal_places=2)
    period = models.CharField(max_length=12)
    remark = models.CharField(max_length=4, blank=True, null=True)
    status = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'tmp_goods_purchase'


class TmpProductNew(models.Model):
    goods_no = models.CharField(max_length=10, blank=True, null=True)
    goods_barcode = models.CharField(max_length=16, blank=True, null=True)
    goods_name = models.CharField(max_length=50, blank=True, null=True)
    goods_id = models.CharField(max_length=16, blank=True, null=True)
    goods_attr_no = models.CharField(max_length=10, blank=True, null=True)
    goods_attr_name = models.CharField(max_length=20, blank=True, null=True)
    is_order = models.CharField(max_length=2, blank=True, null=True)
    is_300 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_product_new'
