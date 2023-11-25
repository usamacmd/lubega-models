from django.db import models

class EquipmentCategory(models.Model):
    Category_id=models.AutoField(primary_key = True)
    Category_name=models.CharField(unique=True, max_length = 45)
    data_created = models.DateField(auto_now = True)
    class Meta:
         Verbose_name_plural = "Equipment Categories"
    def __str__(self) :
        return self.category_name
    
class Product(models.Model):
    Product_id = models.AutoField(primary_key=True)
    category_id=models.ForeignKey(EquipmentCategory, on_delete=models.CASCADE)
    Product_name=models.CharField(unique=True,max_length=45)
    unit_price=models.IntegerField(default=0)
    sale_price=models.IntegerField(default=0)
    available_stock=models.IntegerField(default=0)
    unit_measure=models.CharField(max_length=45)
    date_update=models.DateField(auto_now=True)

    
class Transaction(models.Model):
    Transaction_id=models.AutoField(primary_key=True)
    Product_id=models.ForeignKey(Product, on_delete=models.CASCADE)
    Transaction_type=models.CharField(max_length=89)
    stock_taken=models.IntegerField(default=0)
    transaction_amount=models.IntegerField(default=0)
    transaction_data=models.DateField(auto_now=True)



