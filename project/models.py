from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    stock_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sale_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return  self.name


class Sr(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length= 150)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name= models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    mobile_no = models.CharField(max_length=20)
    sr = models.ForeignKey(Sr)
    def __str__(self):
        return self.name

class Customer(models.Model):
    name= models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    mobile_no = models.CharField(max_length=20)
    sr = models.ForeignKey(Sr)
    def __str__(self):
        return self.name


class SaleItem(models.Model):
    quantity= models.IntegerField()
    free= models.IntegerField()

    item = models.ForeignKey(Item)
    def item_total(self):
        return (self.quantity- self.free)*self.item.sale_rate

class Memo(models.Model):
    date = models.DateField()
    party = models.ForeignKey(Customer)
    sale_item = models.ManyToManyField(SaleItem)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    paid = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def get_total(self):
        return sum(i.item_total() for i in self.sale_item.all())


class PurchaseItem(models.Model):
    quantity= models.IntegerField()
    free= models.IntegerField()

    item = models.ForeignKey(Item)
    def item_total(self):
        return (self.quantity- self.free)*self.item.sale_rate

class PurchaseMemo(models.Model):
    date = models.DateField()
    party = models.ForeignKey(Supplier)
    purchase_item = models.ManyToManyField(PurchaseItem)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    paid = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def get_total(self):
        return sum(i.item_total() for i in self.purchase_item.all())




    





    
